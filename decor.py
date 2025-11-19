"""
in that file i want to apply my little knowledge about decorator


"""


def decorator_function(originial_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed before {originial_function.__name__}.")
        return originial_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("display function run and learn this topic")


@decorator_function
def display_info(name, age):
    print("display_into run   with argument ({},{})".format(name, age))


display_info("john", 47)


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"wrapper executed before {self.originial_function.__name__}.")
        return self.originial_function(*args, **kwargs)


@decorator_class
def display():
    print("display function run and learn this topic")


@decorator_class
def display_info(name, age):
    print("display_into run   with argument ({},{})".format(name, age))
