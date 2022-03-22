import requests


host = "http://127.0.0.1:5000/"
url = host + "data"


class Client:

    @staticmethod
    def get_all_records():
        r = requests.get(url)
        return r.text

    @staticmethod
    def add_new_record(payload):
        r = requests.post(url, json=payload)
        return r.text


if __name__ == "__main__":

    client = Client()

    all_records = client.get_all_records()
    print(f"User gets all records: \n{all_records}")
    print("---------------------")

    payload = {
        "column_one": "cat",
        "column_two": "fat"
    }
    new_record = client.add_new_record(payload)
    print(f"User creates a new record: \n{new_record}")
    print("---------------------")

    all_records = client.get_all_records()
    print(f"User gets all records again: \n{all_records}")
    print("---------------------")
