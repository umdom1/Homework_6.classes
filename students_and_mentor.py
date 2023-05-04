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


class Lecturer(Mentor):
    grades_lecture = {}

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



