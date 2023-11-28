# decorator with parameters / args
def param_dec(name):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(
                f"param_dec: get name from args as tuple :{args[0]}\nand lastname from kwargs as dict: {kwargs['lastname']}"
            )
            return func(*args, **kwargs)

        return wrapper

    return my_decorator


# decorator without parameters / args
def decorator(func):
    def init(*args, **kwargs):
        print("running decorator()")
        return func(*args, **kwargs)

    return init


@param_dec("ali")
@decorator
def say_hello(name, lastname):
    print("Hello!")


# Calling the decorated functions
say_hello(
    "Ali sina",
    lastname="Hussaini",
)
