import requests

url = "http://127.0.0.1:5000/"

# login
response = requests.post(url + "login", json={"login": "user2", "password": "1111"})
print(response, response.text)

token = response.text

# send message
# get format
response = requests.get(url + "get_message")
print(response, response.text)

m_format = response.json()
# send message
m_format["message"] = "TEXT FROM USER"
m_format["token"] = token
response = requests.post(url + "get_message", json=m_format)
print(response, response.text)

# get message list
response = requests.get(url + "message_list", json={"token": token})
print(response, response.text)