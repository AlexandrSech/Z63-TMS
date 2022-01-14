# 2022-01-14
# shlom41k


import requests


url = "http://127.0.0.1:5000/"

# login
response = requests.post(url + "login", json={"login": "user", "password": "12345"})
print(response, response.text)

token = response.text

response = requests.get(url + "message")
print(response.text)

m_format = response.json()


#send message
m_format["message"] = "AAFDkgskjfhsdf"
m_format["token"] = token
response = requests.post(url + "message", json=m_format)
print(response)

response = requests.get(url + "message_list", json={"token": token})
print(response.text)