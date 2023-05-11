class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def _average_rating_student(self):
        res_list = []
        res_average = 0
        for course, grades in self.grades.items():
            res = 0
            for el in grades:
                res += el
            res_list.append(res / len(grades))
        for el in res_list:
            res_average += el
        return (res_average / len(self.grades.keys()))

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_rating_student()}" \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def rate_hw_lector(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_lecture:
                lecturer.grades_lecture[course] += [grade]
            else:
                lecturer.grades_lecture[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
        else:
            return(self._average_rating_student() < other._average_rating_student())

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecture = {}


class Lecturer(Mentor):

    def _average_rating_lecturer(self):
        res_list = []
        res_average = 0
        for course, grades in self.grades_lecture.items():
            res = 0
            for el in grades:
                res += el
            res_list.append(res / len(grades))
        for el in res_list:
            res_average += el
        return (res_average / len(self.grades_lecture.keys()))

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_rating_lecturer()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
        else:
            return(self._average_rating_lecturer() < other._average_rating_lecturer())


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"



best_student = Student('Ivan', 'Ivanov', 'Men')
best_student_2 = Student('Oleg', 'Sidorov', 'Men')

cool_mentor = Mentor('Ivan', 'Petrov')
cool_mentor_2 = Mentor('Vasiliy', 'Fadeev')

super_lecturer = Lecturer('Petr', 'Ivanov')
super_lecturer_2 = Lecturer('Denis', 'Petrov')

reviewer = Reviewer('Vladimir', 'Isaev')
reviewer_2 = Reviewer('Vlasiliy', 'Mamontov')

best_student.finished_courses += ['Python']
best_student_2.finished_courses += ['Python']
best_student.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Python']

reviewer.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']

super_lecturer.courses_attached += ['Python']
super_lecturer_2.courses_attached += ['Python']

best_student.rate_hw_lector(super_lecturer, 'Python', 9)
best_student.rate_hw_lector(super_lecturer, 'Python', 10)
best_student.rate_hw_lector(super_lecturer_2, 'Python', 7)
best_student.rate_hw_lector(super_lecturer_2, 'Python', 8)

reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student_2, 'Python', 8)
reviewer.rate_hw(best_student_2, 'Python', 9)

print(best_student.grades)
print('---------------------')
print(best_student_2.grades)
print('')
print(super_lecturer.grades_lecture)
print('---------------------')
print(super_lecturer_2.grades_lecture)
print('')
print(reviewer)
print('---------------------')
print(reviewer_2)
print('')
print(super_lecturer)
print('---------------------')
print(super_lecturer_2)
print('')
print(best_student)
print('---------------------')
print(best_student_2)
print('')
print(best_student < best_student_2)
print('')
print(super_lecturer < super_lecturer_2)


student_list = []
student_list.append(best_student)
student_list.append(best_student_2)

lecturer_list = []
lecturer_list.append(lector)
lecturer_list.append(lector_2)

def average_student(student_list, course):
  res = 0
  res_len = 0
  for student in student_list:
    for el in student.grades[course]:
      res += el
    res_len += len(student.grades[course])
  print(res/res_len)


def average_lecturer(lecturer_list, course):
  res = 0
  res_len = 0
  for lecturer in lecturer_list:
    for el in lecturer.grades_lecture[course]:
      res += el
    res_len += len(lecturer.grades_lecture[course])  
  print(res/res_len)
    
  
average_student(student_list, 'Python')
average_lecturer(lecturer_list, 'Python')

