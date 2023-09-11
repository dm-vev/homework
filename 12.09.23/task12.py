from typing import Tuple
from time import time

random.seed(time()) # Инициализируем генератор случайных чисел текущим временем. Это повысит случайность чисел

def get_interval() -> Tuple[int, int]:
  while True:
    try:
      a = int(input('Введите число a: '))
      b = int(input('Введите число b (> a): '))
      if a >= b:
        print('Некорректный ввод')
        continue  
      return a, b
    except ValueError:
      print('Ошибка ввода данных. Введите целые числа.')
      
def generate_numbers(a: int, b: int) -> None:
  for _ in range(5):
    print(random.randint(a, b), end=' ')

a, b = get_interval()
generate_numbers(a, b)
