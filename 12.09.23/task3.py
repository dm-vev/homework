def get_number() -> int:
  while True:
    try:
      return int(input('Введите число: '))  
    except ValueError:
      print('Ошибка ввода, введите целое число')

def is_three_digit(number: int) -> bool:
  if 100 <= number <= 999:
    return True
  else:
    return False
  
print('Трехзначное число' if (100 <= get_number() <= 999) else 'Не трехзначное число') # Через тернарный оператор значительно лаконичнее.
