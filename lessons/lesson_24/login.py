import requests

resp = requests.post('http://127.0.0.1:8080/auth',
                    auth=requests.auth.HTTPBasicAuth(username='test_user', password='test_pass')).json()

print(requests.get(url='http://127.0.0.1:8080/cars',
                   headers={'Authorization': f'Bearer {resp["access_token"]}'}).json())