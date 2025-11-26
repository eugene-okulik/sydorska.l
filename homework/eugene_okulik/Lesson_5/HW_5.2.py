line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'
inc_by = 10
start_index_1 = int(line_1[line_1.index(':') + 1:].strip())
start_index_2 = int(line_2[line_2.index(':') + 1:].strip())
start_index_3 = int(line_3[line_3.index(':') + 1:].strip())
print(start_index_1 + inc_by)
print(start_index_2 + inc_by)
print(start_index_3 + inc_by)
