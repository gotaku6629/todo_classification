import requests
import json


# ログイン画面
user_name = 'gotaku'
print(type(user_name)) # string
password = 'ttttest55510'

header = {user_name: password}
response = requests.post('https://~~~~~.com', data=json.dumps(header))

print(response.status_code)
print(response.text)