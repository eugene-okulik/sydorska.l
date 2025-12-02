import random


def pay_sum(salary, bonus):
    if bonus is True:
        bonus_to_pay = int(random.randint(250, 750))
        total_pay = salary + bonus_to_pay
        print(f'{salary}, {bonus} - \'${total_pay}\'')
    else:
        print(f'{salary}, {bonus} - \'${salary}\'')


while True:
    salary = int(input('Enter your salary here: '))
    bonus = random.choice([True, False])
    pay_sum(salary, bonus)
