__author__ = "Стиврина Мария"

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def side1_length(self):
        side1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return side1

    def side2_length(self):
        side2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        return side2

    def side3_length(self):
        side3 = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return side3

    def perimeter(self):
        perimeter_of_the_figure = triangle.side1_length() + triangle.side2_length() + triangle.side3_length()
        return perimeter_of_the_figure

    def area(self):
        p = triangle.perimeter() / 2
        figure_area = math.sqrt(p * (p - triangle.side1_length()) * (p - triangle.side2_length()) * (p -
        triangle.side3_length()))
        return figure_area

    def height(self):
        triangle_height = (2 * triangle.area()) / triangle.side1_length()
        return triangle_height

triangle = Triangle(-5, -2, 4, 5, 6, -1)
print("Периметр треугольника: ", triangle.perimeter())
print("Площадь треугольника: ", triangle.area())
print("Высота треугольника: ", triangle.height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium(Triangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        Triangle.__init__(self, x1, y1, x2, y2, x3, y3)
        self.x4 = x4
        self.y4 = y4

    def side3_length(self):
        side3 = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        return side3

    def side4_length(self):
        side4 = math.sqrt((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2)
        return side4

    def perimeter(self):
        perimeter_of_the_figure = trapezium.side1_length() + trapezium.side2_length() + trapezium.side3_length()
        + trapezium.side4_length()
        return perimeter_of_the_figure

    def area(self):
        p = triangle.perimeter() / 2
        figure_area = math.sqrt(p * (p - triangle.side1_length()) * (p - triangle.side2_length()) * (p -
        triangle.side3_length()))
        return figure_area

trapezium = Trapezium(1, 2, 3, 4, 5, 6, 7, 8)
print("Периметр трапеции: ", trapezium.perimeter())
