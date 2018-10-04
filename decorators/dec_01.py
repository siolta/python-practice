def get_hello_function(punctuation):
    """Returns a hello world function, with or without puncuation"""

    def hello_world():
        print("hello world")

    def hello_world_punctuated():
        print("Hello, world!")

    if punctuation:
        return hello_world_punctuated
    else:
        return hello_world


if __name__ == '__main__':
    ready_to_call = get_hello_function(punctuation=True)

    ready_to_call()
    # "Hello, world!" is printed
