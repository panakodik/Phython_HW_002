# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите количество монеток '))
# reshko = 0
# orel = 0

# x = 0
# while x < n:
#     side = int(input('Введите (1) - это орел или (0) - это решка '))
#     x += 1
#     if side == 0:
#         reshko += 1
#     else:
#         orel += 1

# if orel > reshko:
#     print(f'Нужно перевернуть {reshko} решек')
# else:
#     print(f'Нужно перпевернуть {orel} орлов')




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# S = int(input('Введите сумму чисел X и Y '))
# P = int(input('Введите произведение чисел X и Y '))
# for X in range(S):
#     for Y in range(P):
#         if S == X + Y and P == X * Y:
#             print('Задуманные Петей Числа: ', X, "и" ,Y)





# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Введите целое число '))
k = 0
while 2 ** k <= N:
    print(2 ** k)
    k += 1