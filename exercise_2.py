# Задание №2 Пользователь вводит время в секундах.
# Перевести время в часы, минуты, секунды чч.мм.сс.
# Форматирование строк использовать.
import datetime, time

time = int(input("Введите время в секундах"))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс {hours:02d} : {minutes:02d} : {seconds:02d}")
