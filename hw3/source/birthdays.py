from typing import List, Dict, Any, Optional
import datetime as dt
from collections import defaultdict
from source.address_book import AddressBook

# Weekdays
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def get_birthdays_per_week(
    users: AddressBook, input_date: Optional[dt.datetime] = None
) -> None:
    """Prints in the console users with bithdays at current week.
    Takes as input AddressBook object.

    Output: None
    Args:
        users AddressBook: Object that handles users data.
        input_date (Optional[dt.datetime]): Input date. Defaults to None. Uses current date if None.
    """
    # Preparing output dict
    output = defaultdict(list)

    # Current date
    today = input_date if input_date is not None else dt.datetime.today().date()

    for user in users.get_records():
        name = user.name
        birthday = user.get_birthday()
        if birthday is None:
            continue
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year >= today:
                weekday = birthday_this_year.weekday()
                # Add check for wekend

                if weekday > 4:  # Saturday or Sunday
                    output[WEEKDAYS[0]].append(name)
                else:
                    output[WEEKDAYS[birthday_this_year.weekday()]].append(name)
    # Sort output and print by weekdays
    # for day in WEEKDAYS:
    #     if output[day]:
    #         print(f"{day}: {', '.join(output[day])}")
    formatted_output = []
    for day, names in sorted(output.items(), key=lambda x: WEEKDAYS.index(x[0])):
        formatted_output.append(f"{day}: {', '.join(names)}")
    return formatted_output
