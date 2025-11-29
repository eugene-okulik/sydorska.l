def func (line):
    for num in line:
        return int(line[line.index(':') + 1:].strip()) + 10

line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'

print(func(line_1))
print(func(line_2))
print(func(line_3))
