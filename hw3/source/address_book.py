from source.exceptions import NameNotFundException
from source.record import EmptyRecord, BaseRecord, Record
from collections import UserDict
from source.diff import closest_match
from typing import Union
import json


class AddressBook(UserDict):
    def load(self, data: dict) -> None:
        self.data = data

    def save_to_file(self, path: str) -> None:
        with open(path, "w") as f:
            json.dump(self.to_json(), f)

    def to_json(self) -> dict:
        json_data = {}
        for key, record in self.data.items():
            json_data[key] = record.to_json()
            print(json_data)
        return json_data
        
    def load_from_file(self, path: str) -> None:
        with open(path, "r") as f:
            records = json.load(f)
            for key, record in records.items():
                print(key, record)
                self.data[key] = Record.from_json(record)
                print(self.data[key])
        

    def add_record(self, record: BaseRecord) -> None:
        self.data[record.name] = record

    def delete(self, name: str) -> None:
        if self.data.get(name):
            return self.data.pop(name)
        raise NameNotFundException(name=name)

    def find(self, name) -> BaseRecord:
        """Searches over exact match and returns record.
        Returns EmptyRecord if nothing was found.
        """
        record = self.data.get(name, EmptyRecord())
        return record

    def search(self, name) -> BaseRecord:
        """
        This differs from find that it not only looks for exact name,
        but for similar names too.
        """
        search_list = self.data.keys()
        similar_name = closest_match(
            input_text=name, search_list=search_list, threshold=0.8
        )
        if similar_name is not None:
            return self.data[similar_name]
        return EmptyRecord()
    
    def get_records(self):
        return self.data.values()
