from source.fields import Name, Phone, Birthday
from typing import Union
from source.exceptions import DuplicatedValueException


class BaseRecord:
    def __str__(self):
        return f"Base acstract class for record"


class EmptyRecord(BaseRecord):
    """
    EmptyRecord class.
    Used for consistency when searching over AdressBook.
    Returned if no matching results were found.
    """
    def __bool__(self):
        return False

    def __str__(self):
        return f"Empty record."


class Record(BaseRecord):
    def __init__(self, name: str):
        self._name = Name(name)
        self.phones = []
        self.birthday = None

    def __bool__(self):
        return True
    
    def to_json(self) -> dict:
        return {
            "name": self._name.value,
            "phones": [p.value for p in self.phones],
            "birthday": self.birthday.value.strftime('%d.%m.%Y') if self.birthday else None
        }
    
    @classmethod
    def from_json(cls, data: dict):
        record = cls(data["name"])
        record.phones = [Phone(p) for p in data["phones"]]
        record.birthday = Birthday(data["birthday"]) if data["birthday"] else None
        return record
    
    def __repr__(self) -> str:
        return f"Contact name: {self._name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def __str__(self):
        return f"Contact name: {self._name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    @property
    def name(self):
        return self._name.value

    def add_phone(self, input_phone: str):
        phone = Phone(input_phone)
        if phone in self.phones:
            raise DuplicatedValueException(input_phone)
        self.phones.append(phone)

    def find_phone(self, phone: str) -> Union[Phone, None]:
        # Convert input to Phone class so it will support equality check
        phone = Phone(phone)
        if phone in self.phones:
            return phone

    def remove_phone(self, phone: str) -> bool:
        phone = Phone(phone)
        if phone in self.phones:
            index = self.phones.index(phone)
            return True
        return False

    def edit_phone(self, current_phone: str, new_phone: str) -> bool:
        phone = Phone(current_phone)
        if phone in self.phones:
            index = self.phones.index(phone)
            self.phones[index] = Phone(new_phone)
            return True
        return False
    
    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        if self.birthday:
            return self.birthday.value
