import requests

url = " http://127.0.0.1:5000/"
url_login = url + "login"
url_logout = url + "logout"


login = ""
password = ""


response = requests.get(url) # смотрим дом страницу
print(response.text)

response_login = requests.post(url_login, json={"login": login,
                                                "password": password})
print(response_login.text)