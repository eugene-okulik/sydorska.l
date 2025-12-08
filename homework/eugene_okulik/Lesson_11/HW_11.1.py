class Book:
    material = 'paper'
    text = True

    def __init__(self, name_of_the_book, autor, total_pages, _ISBN, reserved):
        self.name_of_the_book = name_of_the_book
        self.autor = autor
        self.total_pages = total_pages
        self._ISBN = _ISBN
        self.reserved = reserved

    def __str__(self):
        if self.reserved:
            return f'Book name: {self.name_of_the_book}, Autor: {self.autor}, Total pages: {self.total_pages}, n\
                Material: {self.material}, reserved'
        else:
            return f'Book name: {self.name_of_the_book}, Autor: {self.autor}, Total pages: {self.total_pages}, n\
                Material: {self.material}'


class School_Books(Book):
    subject = 'math'
    grade = 4
    exercises = bool

    def __init__(self, name_of_the_book, autor, total_pages, _ISBN, reserved, subject, grade, exercises):
        super().__init__(name_of_the_book, autor, total_pages, _ISBN, reserved)
        self.subject = subject
        self.grade = grade
        self.exercises = exercises

    def __str__(self):
        if self.reserved:
            return f'Name: {self.subject}, Autor: {self.autor}, Total pages: {self.total_pages}, n\
                Subject: {self.subject}, reserved'
        else:
            return f'Name: {self.subject}, Autor: {self.autor}, Total pages: {self.total_pages}, n\
                Subject: {self.subject}'


first_book = Book('Story of my life', 'Shevchenko', 234, 'OS1435328', True)
second_book = Book('Story of his life', 'Shevchenko', 454, 'OS2335328', False)
third_book = Book('Story of her life', 'Shevchenko', 134, 'OS1435348', False)
fourth_book = Book('Story of life', 'Shevchenko', 224, 'OS1435329', True)
fifth_book = Book('Story of ...', 'Shevchenko', 334, 'OS1435330', False)

school_book_1 = School_Books('Stady', 'Dachenko', 67, 'OS142523v', True, 'Math', 5, True)
school_book_2 = School_Books('Stady', 'Myzichenko', 87, 'OS142523v', False, 'Botanic', 7, False)
school_book_3 = School_Books('Staty', 'Polik', 125, 'OS142523v', True, 'Reading', 5, False)

books = [first_book, second_book, third_book, fourth_book, fifth_book]
school_books = [school_book_1, school_book_2, school_book_3]

all_books = books + school_books

for books in all_books:
    print(books)
