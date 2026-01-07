import csv
import mysql.connector as mysql
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='/Users/Sidorskiy/sydorska.l/homework/Sydorska_Homework/HW_Lesson_16/.env')

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)
cursor.execute('''Select
s.name,
s.second_name,
g.title as group_title,
b.title as book_title,
subjects.title as subject_title,
l.title as lesson_title,
m.value as mark_value
from students s
JOIN `groups` g on s.group_id = g.id
JOIN books b on s.id = b.taken_by_student_id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjects on l.subject_id = subjects.id''')

data = cursor.fetchall()
db_row_set = set()
for x in data:
    db_row = (
        x['name'],
        x['second_name'],
        x['group_title'],
        x['book_title'],
        x['subject_title'],
        x['lesson_title'],
        str(x['mark_value'])
    )
    db_row_set.add(db_row)

my_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(my_path))
hw_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

with open(hw_file_path, newline='', encoding="utf-8") as csv_file:
    file_data = list(csv.reader(csv_file))

for row in file_data:
    if tuple(row) not in db_row_set:
        print(row)
