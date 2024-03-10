from bot.utils import parse_input, require_args, suggest_closest_match, user_confirm
from source.address_book import AddressBook
from source.record import Record
from bot.diff import closest_match
from source.birthdays import get_birthdays_per_week

@require_args(2)
def add_contact(args, contacts: AddressBook):
    """Adds new contact.

    Usage: add [name] [phone]

    """
    name, phone = args
    record = Record(name=name)
    record.add_phone(phone)

    if contacts.get(name):
        print(f"Contact {name} already exists. It will be overwritten.")
        if user_confirm():
            print("Contact will be overwritten.")
        else:
            return "Operation canceled."
    contacts.add_record(record)
    return "Contact added."


@require_args(3)
def change_contact(args, contacts: AddressBook):
    """Updates contact.

    Usage: change [name] [old phone] [new phone]

    """
    name, old_phone, new_phone = args

    if contacts.get(name):
        record = contacts.find(name)
        if record.edit_phone(old_phone, new_phone):
            return "Contact updated."
        return f"Phone {old_phone} was not found in the contact {name}."
    return suggest_closest_match(name, contacts.data)


@require_args(1)
def get_phone(args, contacts: AddressBook):
    """Returns a phone number, given username.

    Usage: get [name]

    """
    name = args[0]
    if contacts.get(name):
        return contacts[name]
    return suggest_closest_match(name, contacts.data)

@require_args(2)
def add_birthday(args, contacts: AddressBook):
    """Adds birthday to contact.

    Usage: add-birthday [name] [date]

    """
    name, birthday = args

    if contacts.get(name):
        record = contacts.find(name)
        record.add_birthday(birthday)
        return "Birthday added."
    return suggest_closest_match(name, contacts.data)

@require_args(1)
def show_birthday(args, contacts: AddressBook):
    """Returns birthday of contact.

    Usage: show-birthday [name]

    """
    name = args[0]
    if contacts.get(name):
        record = contacts.find(name)
        return record.birthday
    return suggest_closest_match(name, contacts.data)

def birthdays(args, contacts: AddressBook):
    """Returns birthdays for the upcoming week.

    Usage: birthdays
    """
    return get_birthdays_per_week(contacts)
    

def get_all_contacts(*args):
    """Returns all available contacts.

    Usage: all

    """
    contacts = args[1]
    return contacts.data


def greeting(*args):
    """Greets user with welcome message.

    Usage: hello
    """
    return "Hello!"

def help(*args):
    """Returns list of available commands.

    Usage: help
    """
    print("here")
    available_functions = [
        f"\n -- {name}: {f.__doc__}\n" for name, f in COMMAND_MAPPING.items()
    ]
    return f"""
    As Assistant bot I can run following functions:
            {"".join(available_functions)}
    """

require_args(1)
def save(args, contacts: AddressBook):
    """
    Saves contacts to file.
    
    Usage: save [path]
    """
    path = args[0]
    contacts.save_to_file(path)
    return f"Contacts saved to {path}."

require_args(1)
def load(args, contacts: AddressBook):
    """
    Loads contacts from file.

    Usage: load [path]
    
    """
    path = args[0]
    contacts.load_from_file(path)
    return f"Contacts loaded from {path}."

def wrong_input(command):
    match = closest_match(command, COMMAND_MAPPING.keys())
    if match:
        return f"Command {command} is not recongized. Did you mean {match}?"
    return f"Command {command} is not recongized. Use one of the following: {', '.join(COMMAND_MAPPING.keys())}"


COMMAND_MAPPING = {
    "hello": greeting,
    "add": add_contact,
    "phone": get_phone,
    "change": change_contact,
    "all": get_all_contacts,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "save": save,
    "load": load,
    "help": help,
}
