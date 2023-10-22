class Student:
    # Поля класса
    name = ''
    birthyear = 2000
    grades = []

    # Конструктор (метод, вызываемый при создании объекта на основе класса)
    def __init__(self, name, birthyear, grades):
        # Инициализация полей класса входящими параметрами функции __init__
        self.name = name
        self.birthyear = birthyear
        self.grades = grades
    def get_gpa(self):
        return round(sum(self.grades) / len(self.grades), 1)

    def __str__(self):
        # Вывод полей класса
        return f'{self.name} {self.birthyear} GPA:{self.get_gpa()} {self.grades}'


# Создание объекта (экземпляра класса)
students = [
    Student('Ivan', 2008, [8, 9, 10, 10, 8, 7]),
    Student('Anatoliy', 2009, [9, 9, 8, 10, 11]),
    Student('Victor', 2008, [7, 6, 6, 7, 5]),
    Student('Denis', 2007, [7, 4, 6, 8, 6, 5]),
    Student('Egor', 2009, [8, 10, 10, 9, 10, 11])
]
for student in students:
    print(student)

'''
    Создать список из 5 студентов (объектов класса Student). Вывести данные всех созданных студентов.
'''


'''
students_names = ['Ivan', 'Anatoliy', 'Victor']
students_birthyears = [2008, 2009, 2008]
students_gpa = [9.3, 8.1, 10.6]


print(students[0]['name'])

for i in range(len(students_names)):
    print(f'{students_names[i]} {students_birthyears[i]} {students_gpa[i]}')

best_student_id = 0

for i in range(len(students_names)):
    if students_gpa[i] > students_gpa[best_student_id]:
        best_student_id = i

print('Student with best GPA:')
print(f'{students_names[best_student_id]} {students_birthyears[best_student_id]} {students_gpa[best_student_id]}')
'''