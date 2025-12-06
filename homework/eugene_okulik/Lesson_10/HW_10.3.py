def calc_main(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            op = '*'
        elif first == second:
            op = '+'
        elif first > second:
            op = '-'
        elif first < second:
            op = '/'
        return func(first, second, op)

    return wrapper


@calc_main
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input('Enter first number here: '))
second = int(input('Enter second number here: '))

print(calc(first, second))
