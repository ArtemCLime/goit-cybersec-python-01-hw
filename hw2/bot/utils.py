### Utility functions for bot
from diff import closest_match


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def require_args(n_args):
    def decorator(func):
        def wrapper(args, *args_passed, **kwargs_passed):
            if len(args) != n_args:
                return f"You need to provide exactly {n_args} argument(s) to {func.__name__}."
            return func(args, *args_passed, **kwargs_passed)

        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator


def suggest_closest_match(name, contacts):
    best_closest = closest_match(name, contacts.keys())
    if best_closest:
        return f"Username {name} was not found in the Contacts. Do you mean {best_closest}?"
    return f"Username {name} was not found in the Contacts."


def user_confirm():
    user_input = input("Do you confirm operation? [y/n]")
    return user_input.lower() == "y"
