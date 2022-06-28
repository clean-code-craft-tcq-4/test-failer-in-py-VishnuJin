from exception_handlers import get_error_type


def size(cms):
    if cms > 34 and cms <= 38:
        return "S"
    elif cms > 38 and cms <= 42:
        return "M"
    elif cms > 42 and cms <= 46:
        return "L"
    else:
        raise ValueError("Invalid input")


assert size(37) == "S"
assert size(40) == "M"
assert size(43) == "L"

assert get_error_type(size, -1) == ValueError
assert get_error_type(size, 1) == ValueError
assert get_error_type(size, "A") == TypeError

print("All is well \n")
