class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave(self):
      total_grade = 0
      for course in self.grades:
          total_grade += sum(self.grades[course])
      return round(total_grade / len(self.grades), 2)
    
    def __str__(self):
        student_str = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.ave()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return student_str

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Невозможно сравнить с объектом не класса Student"
        return self.ave() < other.ave()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return "Невозможно сравнить с объектом не класса Student"
        return self.ave() > other.ave()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Невозможно сравнить с объектом не класса Student"
        return self.ave() == other.ave()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        

class Lecturer(Mentor):

    def ave(self):  # средняя оценка за лекции
      total_grade = 0
      for course in self.grades:
          total_grade += sum(self.grades[course])
      return round(total_grade / len(self.grades), 2)

    def ave_course(self, course):
      summ_rate = 0
      len_rate = 0
      for keys in self.grades.keys():
          if keys == course:
              summ_rate += sum(self.grades[course])
              len_rate += len(self.grades[course])
      result = round(summ_rate / len_rate, 2)
      return result
    
    def __str__(self):
        lecturer_1 = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.ave()}"
        return lecturer_1

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Невозможно сравнить с объектом не класса Lecturer"
        return self.ave() < other.ave()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return "Невозможно сравнить с объектом не класса Lecturer"
        return self.ave() > other.ave()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return "Невозможно сравнить с объектом не класса Lecturer"
        return self.ave() == other.ave()

class Reviewer(Mentor):
    
    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        some_reviewer = f"Имя: {self.name} \nФамилия: {self.surname}"
        return some_reviewer
    




student = Student('Стив', 'Джобс','Man')
student.courses_in_progress += ['Python']
student.courses_in_progress += ['Java']
student.courses_in_progress += ['C++']


some_reviewer = Reviewer('Стив', 'Возняк')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Java']
some_reviewer.courses_attached += ['C++']
print(some_reviewer)

some_reviewer.rate(student, 'Python', 10)
some_reviewer.rate(student, 'Java', 8)
some_reviewer.rate(student, 'C++', 7)



lecturer_1 = Lecturer('Джо', 'Бидонов')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['C++']

student.rate_lecturer(lecturer_1, 'Python', 9)
student.rate_lecturer(lecturer_1, 'Java', 8)
student.rate_lecturer(lecturer_1, 'C++', 2)
print(lecturer_1)


student2 = Student('Ruoy', 'Eman','Woman')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

some_reviewer.rate(student2, 'Python', 9)
some_reviewer.rate(student2, 'Python', 10)
some_reviewer.rate(student2, 'Python', 8)
print(student2)

print(f'Сравнение студентов: {student} > {student2} = {student > student2}')

lecturer_2 = Lecturer('Some', 'Buddy')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Введение в программирование']
student2.rate_lecturer(lecturer_2, 'Python', 10)
student2.rate_lecturer(lecturer_2, 'Python', 9)
student2.rate_lecturer(lecturer_2, 'Python', 10)
student2.rate_lecturer(lecturer_2, 'Git', 10)
student2.rate_lecturer(lecturer_2, 'Git', 9)
student2.rate_lecturer(lecturer_2, 'Git', 8)
student2.rate_lecturer(lecturer_2, 'Введение в программирование', 10)
student2.rate_lecturer(lecturer_2, 'Введение в программирование', 9)
student2.rate_lecturer(lecturer_2, 'Введение в программирование', 10)
print(lecturer_2)

print(f'Сравнение лекторов: {lecturer_1} > {lecturer_2} = {lecturer_1 > lecturer_2}')