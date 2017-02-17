import requests

url = 'https://quay.io/api/v1/'

quay_token = 'redacted'

headers={'Authorization': 'access_token {}'.format(quay_token)}

# print requests.post(url+"repository", data=data, headers=headers)
print requests.get(url+"repository?public=true&namespace=geetduggal", headers=headers).json()
