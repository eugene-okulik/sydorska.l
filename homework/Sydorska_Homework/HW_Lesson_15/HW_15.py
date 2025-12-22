import mysql.connector as mysql


db = mysql.connect(
    host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port = 25060,
    user = 'st-onl',
    passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
    database = 'st-onl'
)

cursor = db.cursor()
cursor.execute("SELECT * from students where id = '21931'")
print(cursor.fetchone())

create_student = '''INSERT INTO students(name, second_name, group_id) VALUES (%$, %$, %$)'''
values = ('Liubov', 'Syd', )
cursor.execute('''INSERT INTO books(title, taken_by_student_id) VALUES('SQL', 21931)''')
cursor.execute('''INSERT INTO `groups`(title, start_date, end_date VALUES('2025Dec', 'December 1, 2025', 'December 31, 2025')''')



# INSERT INTO subjects(title) VALUES('sub_1_LS');
# Select * from subjects s where title = 'sub_2_LS'

# INSERT INTO subjects(title) VALUES('sub_2_LS');

# INSERT INTO lessons(title, subject_id)
# VALUES('less1LS', 13335);

# INSERT INTO lessons(title, subject_id)
# VALUES('less2LS', 13335);

# INSERT INTO lessons(title, subject_id)
# VALUES('less3LS', 13336);

# INSERT INTO lessons(title, subject_id)
# VALUES('less4LS', 13336);

# Select * from lessons l where l.subject_id = 13335

# Select * from lessons l where l.subject_id = 13336

# INSERT INTO marks(value, lesson_id, student_id)
# VALUES('A', 74008, 21931);

# INSERT INTO marks(value, lesson_id, student_id)
# VALUES('A', 74009, 21931);

# INSERT INTO marks(value, lesson_id, student_id)
# VALUES('A', 74010, 21931);

# INSERT INTO marks(value, lesson_id, student_id)
# VALUES('A', 74011, 21931);

# Select * from marks m where student_id = 21931

# Select * from books b where taken_by_student_id = 21931

# Select * from students s 
# JOIN `groups` g on s.group_id = g.id
# JOIN books b on s.id = b.taken_by_student_id
# JOIN marks m on s.id = m.student_id
# JOIN lessons l on m.lesson_id = l.id
# JOIN subjects on l.subject_id = subjects.id
# where name = 'Liuba'

db.close()