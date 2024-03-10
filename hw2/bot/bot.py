from diff import closest_match
from utils import parse_input, require_args, suggest_closest_match, user_confirm


@require_args(2)
def add_contact(args, contacts):
    """Adds new contact.

    Usage: add [name] [phone]

    """
    name, phone = args
    if contacts.get(name):
        print(f"Contact {name} already exists. It will be overwritten.")
        if user_confirm():
            print("Contact will be overwritten.")
        else:
            return "Operation canceled."
    contacts[name] = phone
    return "Contact added."


@require_args(2)
def change_contact(args, contacts):
    """Updates contact.

    Usage: change [name] [phone]

    """
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    return suggest_closest_match(name, contacts)


@require_args(1)
def get_phone(args, contacts):
    """Returns a phone number, given username.

    Usage: get [name]

    """
    name = args[0]
    if contacts.get(name):
        return contacts[name]
    return suggest_closest_match(name, contacts)


def get_all_contacts(*args):
    """Returns all available contacts.

    Usage: all

    """
    contacts = args[1]
    return contacts


def greeting(*args):
    """Greets user with welcome message.

    Usage: hello
    """
    return "Hello!"


def help(*args):
    """Returns list of available commands.

    Usage: help
    """
    available_functions = [
        f"\n -- {name}: {f.__doc__}\n" for name, f in COMMAND_MAPPING.items()
    ]
    return f"""
    As Assistant bot I can run following functions:
            {"".join(available_functions)}
    """


COMMAND_MAPPING = {
    "hello": greeting,
    "add": add_contact,
    "phone": get_phone,
    "change": change_contact,
    "all": get_all_contacts,
    "help": help,
}


def wrong_input(command):
    match = closest_match(command, COMMAND_MAPPING.keys())
    if match:
        return f"Command {command} is not recongized. Did you mean {match}?"
    return f"Command {command} is not recongized. Use one of the following: {', '.join(COMMAND_MAPPING.keys())}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        else:
            command_fn = COMMAND_MAPPING.get(command)
            if command_fn:
                print(command_fn(args, contacts))
            else:
                print(wrong_input(command))


if __name__ == "__main__":
    main()
