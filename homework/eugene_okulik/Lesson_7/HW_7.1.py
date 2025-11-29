while True:
    comp_number = 10
    users_number = int(input('Gues what the number: '))
    if users_number == comp_number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
        continue
