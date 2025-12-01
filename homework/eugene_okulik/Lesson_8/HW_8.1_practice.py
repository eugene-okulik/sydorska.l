import random
def pay_sum(salary):
        if salary in range(1, 10001):
            bonus = True
            bonus_to_pay = int(random.randint(250, 750))
            total_pay = salary + bonus_to_pay
            print(f'{salary}, {bonus}, - $\'{total_pay}\'')
        else:
            bonus = False
            print(f'{salary}, {bonus}, - $\'{salary}\'')


while True:                
    salary = int(input('Enter your salary here: '))
    pay_sum(salary)
