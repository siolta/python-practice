from time import sleep

def delayed_func(func):
    """Return a wrapper which delays `func` by 10 seconds."""
    def wrapper():
        print("Waiting for ten seconds...")
        sleep(10)
        # Call the function that was passed in
        func()

    return wrapper


def print_phrase():
    print("Fresh Hacks Every Day")


if __name__ == '__main__':
    delayed_print_function = delayed_func(print_phrase)
    delayed_print_function()
