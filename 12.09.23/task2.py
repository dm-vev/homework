from typing import List

def get_numbers() -> List[int]:
  numbers = []
  for i in range(5):
    while True:
      try:
        number = int(input(f'Введите число {i+1}: '))
        break
      except ValueError:
        print('Ошибка ввода, попробуйте еще раз')
    numbers.append(number)

  return numbers

def find_min_max(numbers: List[int]) -> tuple[int, int]:
  min_num = max_num = numbers[0]
  
  for num in numbers:
    if num < min_num:
      min_num = num
    elif num > max_num:
      max_num = num

  return min_num, max_num

numbers = get_numbers()
min_num, max_num = find_min_max(numbers)

print(f'Минимальное число: {min_num}') 
print(f'Максимальное число: {max_num}')
