from typing import List, Dict, Any, Optional
import datetime as dt
from collections import defaultdict

# Weekdays
WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


def get_birthdays_per_week(
    users: List[Dict[str, Any]], input_date: Optional[dt.datetime] = None
) -> None:
    """Prints in the console users with bithdays at current week.
    Example input [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}]

    Output: None
    Args:
        users (List[Dict[str, Any]]): List of users with their birthdays
        input_date (Optional[dt.datetime]): Input date. Defaults to None. Uses current date if None.
    """
    # Preparing output dict
    output = defaultdict(list)

    # Current date
    today = input_date if input_date is not None else dt.datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
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
    for day in WEEKDAYS:
        if output[day]:
            print(f"{day}: {', '.join(output[day])}")
    return output


if __name__ == "__main__":
    input_date = dt.datetime(2024, 3, 10).date()  # Today, 10th March 2024, Sunday

    # Simple test
    users = [
        {
            "name": "Winry Rockbell",
            "birthday": dt.datetime(1955, 3, 8),
        },  # 8th March (Friday / Past)
        {
            "name": "Edward Elric",
            "birthday": dt.datetime(1955, 3, 10),
        },  # 10th March (Sunday)
        {"name": "Alphonse Elric", "birthday": dt.datetime(1955, 3, 13)},
        # Wednesday
        {
            "name": "Roy Mustang",
            "birthday": dt.datetime(1955, 3, 28),
            # Later then next week
        },
    ]

    expected_output = {
        "Monday": ["Edward Elric"],
        "Tuesday": [],
        "Wednesday": ["Alphonse Elric"],
        "Thursday": [],
        "Friday": [],
    }
    assert get_birthdays_per_week(users, input_date) == expected_output
