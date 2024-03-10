from bot.diff import closest_match
from bot.utils import parse_input, require_args, suggest_closest_match, user_confirm
from typing import Optional
from source.address_book import AddressBook
import json
from bot.bot_functions import COMMAND_MAPPING, wrong_input




class Bot:
    def __init__(self) -> None:
        self.contacts = AddressBook()

    def idle(self) -> None:
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
                    print(command_fn(args, self.contacts))
                else:
                    print(wrong_input(command))

def main():
    bot = Bot()
    bot.idle()

if __name__ == "__main__":
    main()
