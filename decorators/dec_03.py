from time import sleep

def delayed_func(func):
    """Return `func`, delayed by 10 seconds."""
    def wrapper():
        print("Waiting for ten seconds...")
        sleep(10)
        # Call the function that was passed in
        func()

    return wrapper


@delayed_func
def print_phrase():
    print("Fresh Hacks Every Day")


if __name__ == '__main__':
    print_phrase()
