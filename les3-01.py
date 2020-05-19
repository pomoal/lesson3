# # #Задача 1
# # Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# # Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
def num_delete(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Деление на нуль!")
        result=0
    return result

a=int(input("Введите число A:\n"))
b=int(input("Введите число B:\n"))

print(num_delete(a,b))