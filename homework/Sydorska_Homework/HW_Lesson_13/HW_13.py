import os
import datetime


my_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(my_path))
hw_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(hw_file_path, 'r') as data_file:
    line1 = data_file.readline().split(' ', 1)[1].split(' - ')[0]
    line2 = data_file.readline().split(' ', 1)[1].split(' - ')[0]
    line3 = data_file.readline().split(' ', 1)[1].split(' - ')[0]

date1 = datetime.datetime.strptime(line1, '%Y-%m-%d %H:%M:%S.%f')
date2 = datetime.datetime.strptime(line2, '%Y-%m-%d %H:%M:%S.%f')
date3 = datetime.datetime.strptime(line3, '%Y-%m-%d %H:%M:%S.%f')
date_now = datetime.datetime.now()

print(date1 + datetime.timedelta(days=7))
print(date2.strftime('%A'))
print((date_now - date3).days)
