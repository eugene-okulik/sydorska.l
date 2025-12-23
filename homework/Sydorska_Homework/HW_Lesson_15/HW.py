import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Liuba', 'Sydorska')")
student_id = cursor.lastrowid
cursor.execute("SELECT * from students where id = %s",
               (student_id,))
print(cursor.fetchone())


querly_1 = "INSERT INTO books(title, taken_by_student_id) VALUES (%s, %s)"
values_1 = [
    ('SQL_22', student_id),
    ('SQL_23', student_id)
]
cursor.executemany(querly_1, values_1)

cursor.execute('''INSERT INTO
               `groups`(title, start_date, end_date)
               VALUES('Dec2025LS', '2025-12-01', '2025-12-31')''')
group_id = cursor.lastrowid

cursor.execute("SELECT * from `groups` g where id = %s",
               (group_id,))
print(cursor.fetchone())

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
               (group_id, student_id))

cursor.execute("INSERT INTO subjects(title) VALUES('sub7_LS')")
subject_id_1 = cursor.lastrowid

cursor.execute("INSERT INTO subjects(title) VALUES('sub8_LS')")
subject_id_2 = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
               ('less10LS', subject_id_1))
less_id_1 = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
               ('less11LS', subject_id_1))
less_id_2 = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
               ('less12LS', subject_id_2))
less_id_3 = cursor.lastrowid

cursor.execute("INSERT INTO lessons(title, subject_id) VALUES (%s, %s)",
               ('less13LS', subject_id_2))
less_id_4 = cursor.lastrowid

querly = "INSERT INTO marks(value, lesson_id, student_id) VALUES(%s, %s, %s)"
values = [
    ('A', less_id_1, student_id),
    ('A', less_id_2, student_id),
    ('A', less_id_3, student_id),
    ('A', less_id_4, student_id)
]
cursor.executemany(querly, values)

cursor.execute("Select * from marks m where student_id = %s",
               (student_id,))
print(cursor.fetchall())

cursor.execute("Select * from books b where taken_by_student_id = %s",
               (student_id,))
print(cursor.fetchall())

join_querly = '''Select *
from students s
JOIN `groups` g on s.group_id = g.id
JOIN books b on s.id = b.taken_by_student_id
JOIN marks m on s.id = m.student_id
JOIN lessons l on m.lesson_id = l.id
JOIN subjects on l.subject_id = subjects.id
where s.id = %s'''
cursor.execute(join_querly, (student_id,))
print(cursor.fetchall())

db.commit()


db.close()
