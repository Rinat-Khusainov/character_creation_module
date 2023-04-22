from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Сравнивает значения."""
    if your_number <= 0:
        return
    sqrt_numb = calculate_square_root(your_number)

    print('Мы вычислили квадратный корень из введённого вами числа. Это будет',
          sqrt_numb)


calc(25.5)
