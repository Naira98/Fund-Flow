# Simple decorator with parameters
def type_check_decorator(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(isinstance(arg, expected_type) for arg in args):
                return func(*args, **kwargs)
            return "Invalid Input"

        return wrapper

    return decorator




@type_check_decorator(str)
def string_join(*args):
    return "".join(args)


@type_check_decorator(int)
def summation(*args):
    return sum(args)


# Test the functions
print(string_join("I ", "like ", "Geeks", "for", "geeks"))
# print(summation(19, 2, 8, 533, 67, 981, 119))
