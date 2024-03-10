import re
from source.exceptions import BadPhoneNumberFormatException, RequiredFieldException


class Field:
    def __init__(self, value, required=False):
        if required and value is None:
            raise RequiredFieldException(self)
        self.value = value
        self.required = required

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value, required=True):
        super().__init__(value, required)


class Phone(Field):
    def __init__(self, value: str, required=False) -> None:
        value = self.validate(value)
        super().__init__(value, required)

    def validate(self, value: str) -> str:
        # Adding here not just validation, but fixing the number
        cleaned_number = re.sub(r"[()\s-]", "", value)
        if len(cleaned_number) != 10:
            raise BadPhoneNumberFormatException(value)
        print(f"Number cleaned: {value} -> {cleaned_number}")
        return cleaned_number
