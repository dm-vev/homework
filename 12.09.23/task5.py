def get_month() -> int:
  while True:
    try:
      month = int(input('Введите номер месяца: '))
      if 1 <= month <= 12:
        return month
      else:
        print('Номер месяца должен быть от 1 до 12')
    except ValueError:
      print('Введено неверное значение')
      
def get_days(month: int) -> None:
  if month in [1, 3, 5, 7, 8, 10, 12]:
    print('31 день')
  elif month in [4, 6, 9, 11]:
    print('30 дней')
  elif month == 2:
    print('28 или 29 дней')
  else:
    print('Ошибка в номере месяца')
    
get_days(get_month())
