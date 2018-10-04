def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child


# foo = parent(10)
# bar = parent(11)

# print(foo)
# print(bar)

# print(foo())
# print(bar())


# example 01
# def my_decorator(some_func):

#     def wrapper():

#         print("Something is happening before some_func() is called.")

#         some_func()

#         print("Something is happening after some_func() is called.")

#     return wrapper


# def just_some_func():
#     print("Wheee!")


# just_some_func = my_decorator(just_some_func)

# just_some_func()


# example 02
# def my_decorator(some_function):

#     def wrapper():

#         num = 10

#         if num == 10:
#             print("Yes!")
#         else:
#             print("No!")

#         some_function()

#         print("Something is happening after some_function() is called.")

#     return wrapper


# def just_some_function():
#     print("Wheee!")

# just_some_function = my_decorator(just_some_function)

# just_some_function()


# module 
def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper

if __name__ == "__main__":
    my_decorator()