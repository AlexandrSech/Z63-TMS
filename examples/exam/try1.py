import requests
import json


def foo(i=0):
    print(i)
    if i > 20:
        return "DAAAAAAA"
    return foo(i+1)


def printer(data, tabs="    ", col_tabs=1):
    if type(data) in [list, tuple, set]:
        for item in data:
            printer(item, col_tabs=col_tabs + 1)
    elif type(data) == dict:
        for k, v in data.items():
            print(tabs * col_tabs + "{}: ".format(k))
            printer(v, col_tabs=col_tabs + 1)
    else:
        print(tabs * col_tabs + str(data))






    '''for k, v in _json.items():
        print("{}: ".format(k))
        if type(v) in [list, tuple, set]:
            for item in v:
                print(" "*4 + str(item))
        elif type(v) is dict:
            for _k, _v in v.items():
                print(" "*4 + "{}: {}".format(_k, _v))
        else:
            print(" "*4 + str(v))'''


def printer2(data: str):
    for char_id, char in enumerate(data):
        if char == "{":
            data.split(data)
            # data = data.replace(data[0:char_id], "{}\n    ".format(data[0:char_id]))
    return data



url = "https://randomuser.me/api/"
r = requests.get(url)
# print(r, type(r.text), type(r.json()))

dd = json.loads(r.text)
# print(type(dd))

print(dd)
print(printer2(str(dd)))


"""
{'results': [
    {'gender': 'male', 'name': {'title': 'Mr', 'first': 'Angel', 'last': 'Santana'}, 'location': {'street': {'number': 2808, 'name': 'Calle de Alberto Aguilera'}, 'city': 'Albacete', 'state': 'Aragón', 'country': 'Spain', 'postcode': 35380, 'coordinates': {'latitude': '-25.1398', 'longitude': '-144.7231'}, 'timezone': {'offset': '-1:00', 'description': 'Azores, Cape Verde Islands'}}, 'email': 'angel.santana@example.com', 'login': {'uuid': '2d643004-8557-4a40-9516-fb7e9740fb8e', 'username': 'biggoose947', 'password': 'fandango', 'salt': 'ItwBQqbh', 'md5': 'a848104469e8a3255aad80d86faec38e', 'sha1': '22bdb12e01cdec0cb4b440c7ef0a142d0b89601b', 'sha256': '09364663475cd110b58cb3da9848e86b6593e0774c63a2591685d2367762bbe7'}, 'dob': {'date': '1984-12-31T15:58:18.633Z', 'age': 37}, 'registered': {'date': '2010-02-08T17:42:48.220Z', 'age': 11}, 'phone': '964-309-658', 'cell': '649-296-305', 'id': {'name': 'DNI', 'value': '47423223-L'}, 'picture': {'large': 'https://randomuser.me/api/portraits/men/90.jpg', 'medium': 'https://randomuser.me/api/portraits/med/men/90.jpg', 'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/90.jpg'}, 'nat': 'ES'}], 'info': {'seed': '10497846d5c21ed7', 'results': 1, 'page': 1, 'version': '1.3'}}"""
