def decor(func):

    def wrapper():
        func()
        print('finished')

    return wrapper

@decor
def test1():
    print('First test')

@decor
def test2():
    print('Second test')

@decor
def test3():
    print('123')

test1()
test2()
test3()
