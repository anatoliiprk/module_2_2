print('Введите три числа:')
first = int(input('-'))
second = int(input('-'))
third = int(input('-'))
print('Колличество одинаковых чисел:')
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
