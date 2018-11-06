__author__ = "Стиврина Мария"

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, *classes):
        self.classes = classes

    def get_all_classes(self):
        return self.classes

class Classrooms:
    def __init__(self, num_class, student, *teachers):
        self.num_class = num_class
        self.student = student
        self.teachers = teachers

    def get_num(self):
        return self.num_class

    def get_st(self):
        return self.student

    def get_teach(self):
        return self.teachers

class People:
    def __init__(self, name, patronymic, surname, IO):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.IO = IO

    def get_full_name(self):
        return self.name + " " + self.patronymic + " " + self.surname

    def get_short_name(self):
        return self.surname + " " + self.IO

# Сами классы наследуем
class Student(People):
    def __init__(self, name, patronymic, surname, IO, birth_date, school, class_room, mother, father, *disciplines):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, patronymic, surname, IO)
        # Добавляем уникальные атрибуты
        self.birth_date = birth_date
        self.school = school
        self.mother = mother
        self.father = father
        self.disciplines = disciplines
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1

    def get_parents(self):
        return self.mother, self.father

    def get_disciplines(self):
        return self.disciplines

class Teacher(People):
    def __init__(self, name, patronymic, surname, IO, school, discipline):
        People.__init__(self, name, patronymic, surname, IO)
        self.school = school
        self.discipline = discipline
        #self.teach_classes = list(map(self.convert_class, teach_classes))

    def get_discipline(self):
        return self.discipline

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        """
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}

clas = School("5 А", "6 Б", "7 В")

students = [Student("Александр", "Иванович", "Иванов", "А.И.", '10.11.1998', "8 гимназия", "5 А",
                    "Георгина Грациановна Иванова", "Иван Михайлович Иванов", "Литература", "Математика",
                    "Изобразительное искусство"),
            Student("Петр", "Иванович", "Сидоров", "П.И.", '10.01.1995', "8 гимназия", "6 Б",
                    "Наталья Петровна Сидорова", "Иван Михайлович Сидиров", "Литература", "Математика",
                    "Изобразительное искусство", "География"),
            Student("Иван", "Иванович", "Петров", "И.И.", '12.11.1999', "8 гимназия", "7 В",
                    "Светлана Валентиновна Петрова", "Иван Валерьевич Петров", "Литература", "Математика",
                    "Физика", "География")]

teachers = [Teacher("Виктор", "Петрович", "Астафьев", "В.П.", "8 гимназия", "Литература"),
            Teacher("Софья", "Васильевна", "Ковалевская", "С.В.", "8 гимназия", "Математика"),
            Teacher("Жорес", "Иванович", "Алфёров", "Ж.И.", "8 гимназия", "Физика"),
            Teacher("Андрей", "Петрович", "Капица", "А.П.", "8 гимназия", "География"),
            Teacher("Иван", "Константинович", "Айвазовский", "И.К.", "8 гимназия", "Изобразительное искусство")]

classroom = [Classrooms("5 А", students[0].get_short_name(), [teachers[0].get_full_name(),
                                                                teachers[0].get_discipline(),
                                                                teachers[1].get_full_name(),
                                                                teachers[1].get_discipline(),
                                                                teachers[4].get_full_name(),
                                                                teachers[4].get_discipline()]),
             Classrooms("6 Б", students[1].get_short_name(), [teachers[0].get_full_name(),
                                                                teachers[0].get_discipline(),
                                                                teachers[1].get_full_name(),
                                                                teachers[1].get_discipline(),
                                                                teachers[3].get_full_name(),
                                                                teachers[3].get_discipline(),
                                                                teachers[4].get_full_name(),
                                                                teachers[4].get_discipline()]),
             Classrooms("7 В", students[2].get_short_name(), [teachers[0].get_full_name(),
                                                                teachers[0].get_discipline(),
                                                                teachers[1].get_full_name(),
                                                                teachers[1].get_discipline(),
                                                                teachers[2].get_full_name(),
                                                                teachers[2].get_discipline(),
                                                                teachers[3].get_full_name(),
                                                                teachers[3].get_discipline()])]

print("1. Полный список всех классов школы: ", clas.get_all_classes(), "\n")

print("2. Список всех учеников в классе {}: ".format(classroom[0].get_num()), classroom[0].get_st())
print("2. Список всех учеников в классе {}: ".format(classroom[1].get_num()), classroom[1].get_st())
print("2. Список всех учеников в классе {}: ".format(classroom[2].get_num()), classroom[2].get_st(), "\n")

print("3. Ученик {} изучает следующие предметы: ".format(students[0].get_short_name()),
      students[0].get_disciplines())
print("3. Ученик {} изучает следующие предметы: ".format(students[1].get_short_name()),
      students[1].get_disciplines())
print("3. Ученик {} изучает следующие предметы: ".format(students[2].get_short_name()),
      students[2].get_disciplines(), "\n")

print("4. Родители ученика {}: ".format(students[0].get_short_name()), students[0].get_parents())
print("4. Родители ученика {}: ".format(students[1].get_short_name()), students[1].get_parents())
print("4. Родители ученика {}: ".format(students[2].get_short_name()), students[2].get_parents(), "\n")

print("5. Список всех учителей преподающих в классе {}: ".format(classroom[0].get_num()), classroom[0].get_teach())
print("5. Список всех учителей преподающих в классе {}: ".format(classroom[1].get_num()), classroom[1].get_teach())
print("5. Список всех учителей преподающих в классе {}: ".format(classroom[2].get_num()), classroom[2].get_teach())