__author__ = "Стиврина Мария"

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Figure:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def side_length(self):
        side1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        side2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        side3 = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return side1, side2, side3

    def perimeter(self):
        perimeter_of_the_figure = side1 + side2 + side3
        return perimeter_of_the_figure

    def area(self):
        p = perimeter_of_the_figure / 2
        figure_area = sqrt(p * (p - side1) * (p - side2) * (p - side3))
        return figure_area

    def height(self):
        triangle_height = (2 * figure_area) / side1
        return triangle_height

triangle = Figure(-5, -2, 4, 5, 6, -1)
print(triangle.perimeter())
print(triangle.area())
print(triangle.height())


"""class Student(People):
    def __init__(self, name, surname, birth_date, school, class_room):
        # Явно вызываем конструктор родительского класса
        People.__init__(self, name, surname, birth_date, school)
        # Добавляем уникальные атрибуты
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}

    # И уникальные методы
    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(People):
    def __init__(self, name, surname, birth_date, school, teach_classes):
        People.__init__(self, name, surname, birth_date, school)
        self.teach_classes = list(map(self.convert_class, teach_classes))

    # Уникальный метод Учителя
    def convert_class(self, class_room):
        
        '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
        
        return {'class_num': int(class_room.split()[0]),
                'class_char': class_room.split()[1]}
"""
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

