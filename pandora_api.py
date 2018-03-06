import requests
import json

username = 'gadaget612@aol.com'
passwrd = 'gizmos'

headers = {
    'Content-type': 'application/json;charset-utf-8',
    'X-CsrfToken': '',
    'X-AuthToken': '',
    'host': 'https://www.pandora.com'
}
data = {
    'existingAuthToken': None,
    'keppLoggedIn': False,
    'password': str(passwrd),
    'username': str(username),
}
cookies = {}

url =  'https://www.pandora.com'
main_api_endpoint = url + '/api'
auth_endpoint = url + main_api_endpoint + '/v1/auth/login'

# get csrf token
resp_csrf = requests.head(url)
cookies['csrftoken'] = resp_csrf.cookies['csrftoken']
headers['X-CsrfToken'] = resp_csrf.cookies['csrftoken']

# get auth token
try:
    resp_auth = requests.post(auth_endpoint,data=data,headers=headers,cookies=cookies)
except Exception as e:
    print(type(e))
    print(e)
headers['X-AuthToken'] = resp_auth.text['']
