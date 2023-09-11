from typing import Tuple

def get_points(x_msg, y_msg) -> Tuple[float, float]: # Хоть аннотации типов и не влияют на проверку типов, это значительно упростит жизнь с использованием IDE
  while True:
    try:
      x = float(input(f'{x_msg}: '))
      y = float(input(f'{y_msg}Y: '))
      return x, y
    except ValueError:
      print('Некорректный ввод. Введите числа.')

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1, y1 = get_points("Введите координату x первой точки", "Введите координату y первой точки")
x2, y2 = get_points("Введите координату x второй точки", "Введите координату y второй точки")

distance = round(calculate_distance(x1, y1, x2, y2), 2) # Нежелательно использовать так переменную distance, лучше сразу ее выводить.
print(f'Расстояние между точками: {distance}')
