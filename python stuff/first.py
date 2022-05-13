import requests

url='https://api.spotify.com/v1'
url_auth='https://api.spotify.com/token'

client_id = '7f4cf2a986d743ca8e3cc2114c7c596f'
client_secret = '6d4883f0ff214bc0ab5ac95e25aa874e'

response = requests.post(url_auth)
print(response.status_code)