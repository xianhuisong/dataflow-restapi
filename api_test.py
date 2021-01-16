import base64
import json
import requests


def get_revisions():
    az_uri = 'https://dev.azure.com/{organization}/'
    az_project = '{project}'
    # uri
    azdevopsURL = az_uri + az_project + '/_apis/wit/workItems/134259/revisions?api-version=6.1-preview.3'
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
    try:
        response = requests.get(azdevopsURL, headers=head, params=params, auth=(azdevopsUser, azdevopsPass))
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print(err)


def get_capacities():
    azdevopsURL = 'https://dev.azure.com/{}/{}/{}/_apis/work/teamsettings/iterations/d2d2841a-30a1-4469-9568-2b57cf690024/capacities?api-version=6.1-preview.2'
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
    try:
        response = requests.get(azdevopsURL, headers=head, params=params, auth=(azdevopsUser, azdevopsPass))
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print(err)


def get_iterations():
    azdevopsURL = 'https://dev.azure.com/{}/{}/{}/_apis/work/teamsettings/iterations?api-version=6.1-preview.1'
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

    try:
        response = requests.get(azdevopsURL, headers=head, params=params, auth=(azdevopsUser, azdevopsPass))
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print(err)


if __name__ == '__main__':
    # get_capacities()
    # get_iterations()
    get_revisions()
