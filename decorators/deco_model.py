from decorators import my_decorator


@my_decorator
def just_some_function():
    print("Wheeee!")


just_some_function()
