import argparse
import base64
import json
import apache_beam as beam
import requests
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, SetupOptions


def call_rest_api(record):
    azdevopsUser = ''
    azdevopsPass = ''
    azdevopsURL = 'https://dev.azure.com/{}/{}/_apis/wit/workItems/{}/revisions'. \
        format(record['organization'], record['projectid'], record['workitemid'])
    print(azdevopsURL)
    # query parameter
    params = {"api-version": "6.1-preview.3"}
    p64 = base64.b64encode(str(params).encode()).decode('utf-8')
    http_params = base64.b64decode(p64).decode('utf-8')
    params = json.loads(http_params.replace("'", '"'))

    # header
    head = {'Accept': 'application/json-patch+json', 'Content-Type': 'application/json-patch+json'}
    p64 = base64.b64encode(str(head).encode()).decode('utf-8')
    head = base64.b64decode(p64).decode('utf-8')
    head = json.loads(head.replace("'", '"'))
    extract = []
    try:
        response = requests.get(azdevopsURL, headers=head, params=params, auth=(azdevopsUser, azdevopsPass))
        response.raise_for_status()
        res = response.text.replace('\\', '')
        res = json.loads(res)
        for item in res['value']:
            rev = item['rev']
            fields = item['fields']
            change_date = fields['System.ChangedDate']
            state = fields['System.State']
            extract.append({'rev': rev, 'change_date': change_date, 'state': state, 'workitemid': record['workitemid']})
    except Exception as err:
        print("Error:")
        print(err)
        print("Response:")
        print(response.text)
    finally:
        return extract


def run(argv=None):
    """Constructs and runs the pipeline."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        help='BigQuery table to read from.',
        default='cf-fs-project-299907:demo_ds.input_tbl')
    parser.add_argument(
        '--output', help='BigQuery table to write to.',
        default='cf-fs-project-299907:demo_ds.output_tbl')
    parser.add_argument(
        '--save_main_session',
        default=True,
        action='store_true',
        help=
        ('Save the main session state so that pickled functions and classes '
         'defined in __main__ (e.g. interactive session) can be unpickled. '
         'Some workflows do not need the session state if for instance all '
         'their functions/classes are defined in proper modules (not __main__)'
         ' and the modules are importable in the worker. '))
    known_args, pipeline_args = parser.parse_known_args(argv)
    options = PipelineOptions(flags=argv,
                              runner='DataflowRunner',
                              project='cf-fs-project-299907',
                              job_name='dataflowrestapi',
                              temp_location='gs://bigquerytemp_dataflow',
                              region='us-east1',
                              network='acn-cio-project-vpc',
                              subnetwork='regions/us-east1/subnetworks/us-east1-public-subnet')
    google_cloud_options = options.view_as(SetupOptions)
    google_cloud_options.save_main_session = True
    with beam.Pipeline(argv=pipeline_args, options=google_cloud_options) as p:
        p | 'Read from input_tbl' >> beam.io.Read(
            beam.io.BigQuerySource(known_args.input)) \
        | 'model predict' >> beam.ParDo(call_rest_api) \
        | 'SaveToBQ' >> beam.io.WriteToBigQuery(
            known_args.output,
            schema='rev:INTEGER,change_date:STRING,state:STRING,workitemid:INTEGER',
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)


if __name__ == '__main__':
    run()
    # record = {'organization': 'accenturecio02', 'projectid': 'AIA002wCIOAnalytic_107038', 'workitemid': '134260'}
    # res = call_rest_api(record)
    # print(res)
