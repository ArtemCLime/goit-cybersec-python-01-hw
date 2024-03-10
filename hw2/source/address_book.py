from source.exceptions import NameNotFundException
from source.record import EmptyRecord, BaseRecord
from collections import UserDict
from source.diff import closest_match
from typing import Union

class AddressBook(UserDict):
    def add_record(self, record: BaseRecord) -> None:
        self.data[record.name] = record

    def delete(self, name: str) -> None:
        if self.data.get(name):
            return self.data.pop(name)
        raise NameNotFundException(name=name)
    
    def find(self, name) -> BaseRecord:
        """ Searches over exact match and returns record.
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
        similar_name = closest_match(input_text=name, search_list=search_list, threshold=0.8)
        if similar_name is not None:
            return self.data[similar_name]
        return EmptyRecord()

            