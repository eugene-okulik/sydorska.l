def say_how_many_times_to_print(func):

    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        for _ in range(count):
            func(*args, **kwargs)
    return wrapper

@say_how_many_times_to_print
def copy_me(something):
    print(something)

@say_how_many_times_to_print
def repeat_me(some):
    print(some)

@say_how_many_times_to_print
def repeat_number(x):
    print(x)


copy_me('Hello', count = 3)
repeat_me('Ola', count = 2)
repeat_number(123, count = 5)
