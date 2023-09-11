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
            
def get_season(month: int) -> None:
    if 3 <= month <= 5:
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif 9 <= month <= 11:
        print('Осень')
    elif month == 12 or month == 1 or month == 2:
        print('Зима')
    else:
        print('Ошибка в номере месяца')

get_season(get_month())
