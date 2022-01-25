from db import DBTable
import json


class Server:

    def __init__(self):
        self.DB = [
            DBTable(id=1, column_one='xxx', column_two='yyy'),
            DBTable(id=2, column_one='zzz', column_two='fff')
        ]

    @staticmethod
    def to_dict(record):
        return record.__dict__

    @property
    def set_id(self):
        return 3   #TODO implement returning of the next number after the last id among all the records

    def get_list_of_records(self):
        return [self.to_dict(_) for _ in self.DB]

    def create_record(self, json_with_data):
        dict_with_data = json.loads(json_with_data)

        new_object = DBTable(
            id=self.set_id,
            column_one=dict_with_data['column_one'],
            column_two=dict_with_data['column_two']
        )
        self.DB.append(new_object)

        return self.to_dict(new_object)

