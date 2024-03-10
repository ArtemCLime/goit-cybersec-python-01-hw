class NameNotFundException(Exception):
    def __init__(self, name):
        message = f"Name {name} was not found in Contacts."
        super().__init__(message)


class BadPhoneNumberFormatException(Exception):
    def __init__(self, phone):
        message = f"Phone {phone} was not in a correct format. Make sure your number has only 10 digits."
        super().__init__(message)


class DuplicatedValueException(Exception):
    def __init__(self, value):
        message = f"Value {value} is already in the list you trying to insert in."
        super().__init__(message)


class RequiredFieldException(Exception):
    def __init__(self, obj):
        message = f"Value is required for class {obj}"
        super().__init__(message)
