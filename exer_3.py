# Задание №3. Узнать у пользователя число n.
# Найти сумму чисел n+nn+nnn. Пример: 3+33+333=369
import random
n = int(input('Введите число : '))
total = (n + int(str(n) + str(n)) + int(str(n) + str (n) + str (n)))
print("Сумма чисел n + nn + nnn = %d" % total)

