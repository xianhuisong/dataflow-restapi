# dataflow-restapi
(evn) C:\Code\df-restapi>python df-restapi.py
df-restapi.py:81: BeamDeprecationWarning: BigQuerySource is deprecated since 2.25.0. Use ReadFromBigQuery instead.
  | 'SaveToBQ' >> beam.io.WriteToBigQuery(
C:\Code\df-restapi\evn\lib\site-packages\apache_beam\io\gcp\bigquery.py:1889: BeamDeprecationWarning: options is deprecated since First stable release. References to <pipeline>.options will not be supported
  temp_location = pcoll.pipeline.options.view_as(
C:\Code\df-restapi\evn\lib\site-packages\apache_beam\io\gcp\bigquery_file_loads.py:901: BeamDeprecationWarning: options is deprecated since First stable release. References to <pipeline>.options will not be supported
  temp_location = p.options.view_as(GoogleCloudOptions).temp_location
WARNING: You are using pip version 20.3.1; however, version 20.3.3 is available.
You should consider upgrading via the 'C:\Code\df-restapi\evn\Scripts\python.exe -m pip install --upgrade pip' command.
WARNING: You are using pip version 20.3.1; however, version 20.3.3 is available.
You should consider upgrading via the 'C:\Code\df-restapi\evn\Scripts\python.exe -m pip install --upgrade pip' command.
WARNING:root:Make sure that locally built Python SDK docker image has Python 3.7 interpreter.

(evn) C:\Code\df-restapi>
