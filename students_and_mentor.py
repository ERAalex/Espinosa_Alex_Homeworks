

class Student:
    student_list = []
    student_courses_studing = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.student_list.append(self.name)
        self.student_courses_studing.append((self.courses_in_progress))
        self.grades = {}

    def add_note(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

 # много где повторяется, сделаем функцию для использования в других функциях например в str
    def middle(self):
        for key, value in self.grades.items():
            total = sum(value)
            size = len(value)
            middle_note = total / size
            return middle_note


    def __str__(self):
        middle_note = self.middle()
        result = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(middle_note,1)}\n' \
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return result


    def __eq__(self, other):
        if isinstance(other, Student):
            middle_note_sel = self.middle()
            middle_note_oth = other.middle()
            if middle_note_sel > middle_note_oth:
                compare = f'\nстудент {self.name} имеет больше баллов, чем студент {other.name}'
            else:
                compare = f'\nстудент {self.name} имеет меньше баллов, чем студент {other.name}'
            return compare





# ______________________________________  MENTOR ______________________________________ #

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


# ______________________________________SUB CLASS LECTURER______________________________________ #

class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lecturer_list.append(self.name)
        self.grades = {}

    def __str__(self):
        for key, value in self.grades.items():
            if key == 'Python':
                total = sum(value)
                size = len(value)
                middle_note = total / size
        result = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {round(middle_note,1)}\n'
        return result


# много где повторяется, сделаем функцию для использования в других функциях например в str
    def middle(self):
        for key, value in self.grades.items():
            total = sum(value)
            size = len(value)
            middle_note = total / size
            return middle_note


    def __str__(self):
        middle_note = self.middle()
        result = f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {round(middle_note,1)}\n'
        return result


    def __eq__(self, other):
        if isinstance(other, Lecturer):
            middle_note_sel = self.middle()
            middle_note_oth = other.middle()
            if middle_note_sel > middle_note_oth:
                compare = f'\nлектор {self.name} имеет больше баллов, чем лектор {other.name}'
            else:
                compare = f'\nлектор {self.name} имеет меньше баллов, чем лектор {other.name}'
            return compare



# ______________________________________SUB CLASS REVIEWER______________________________________ #

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return result





best_student1 = Student('Roy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Введение в программирование']

best_student2 = Student('Alex', 'Midd', 'male')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Введение в SQL']


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

good_lecturer1 = Lecturer('Tom', 'Bochinskiy')
good_lecturer1.courses_attached += ['Python']

good_lecturer2 = Lecturer('Jimmy', 'Tupchin')
good_lecturer2.courses_attached += ['Python']

good_reviewer = Reviewer('Mari', 'Smith')
good_reviewer.courses_attached += ['Python']

best_student1.add_note(good_lecturer1, 'Python', 6)
best_student1.add_note(good_lecturer1, 'Python', 10)

best_student1.add_note(good_lecturer2, 'Python', 9)
best_student1.add_note(good_lecturer2, 'Python', 9)

good_reviewer.rate_hw(best_student1, 'Python', 8)
good_reviewer.rate_hw(best_student2, 'Python', 10)



print('\n####################  TASK 3   #####################')

print(good_reviewer)
print(good_lecturer1)
print(best_student1)


print('\n####################  TASK 3.2 - сравнивать (через операторы сравнения)   #####################')

print(good_lecturer1 == good_lecturer2)
print(best_student1 == best_student2)




print('\n####################  TASK 4   #####################')

#First Part - choose students and course to see middle notes.

def rate_notes_st(coursess, name_st):
    total_notes_len = []
    total_sum_notes = []
    for namess in name_st:
        if isinstance(namess, Student) and coursess in namess.grades:
            for key, value in namess.grades.items():
                total = sum(value)
                size = len(value)
                total_notes_len.append(size)
                total_sum_notes.append(total)

    total_middle_note = sum(total_sum_notes) / sum(total_notes_len)
    print(f'По Вашим параметрам средняя оценка Студентов - {total_middle_note}')


rate_notes_st('Python', [best_student1, best_student2])


#Second Part - choose lecturer and course to see middle notes.

def rate_notes_lec(coursess, name_lec):
    total_notes_len = []
    total_sum_notes = []
    for namess in name_lec:
        if isinstance(namess, Lecturer) and coursess in namess.grades:
            for key, value in namess.grades.items():
                total = sum(value)
                size = len(value)
                total_notes_len.append(size)
                total_sum_notes.append(total)

    total_middle_note = sum(total_sum_notes) / sum(total_notes_len)
    print(f'По Вашим параметрам средняя оценка Лекторов - {total_middle_note}')


rate_notes_lec('Python', [good_lecturer2, good_lecturer1])