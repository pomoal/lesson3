# # #Задача 1
# # Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# # Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#
# def num_delete(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Деление на нуль!")
#         result=0
#     return result
#
# a=int(input("Введите число A:\n"))
# b=int(input("Введите число B:\n"))
#
# print(num_delete(a,b))


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# def my_func(user_name="", surname="", year_of_born="", city="", email="", phone=""):
#     user_string = str(user_name)+' '+str(surname)+' '+str(year_of_born)+' '+str(city)+' '+str(email)+' '+str(phone)
#     return user_string
#
# user_list = my_func(user_name="Иван", surname="Иванов", year_of_born=1990,city="Москва",email="iviv@iv.iv", phone="+7xx0xx0x")
#
# print(user_list)

# #3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# # и возвращает сумму наибольших двух аргументов.
#
# def sum_of_2(a,b,c):
#     sum_list=[a,b,c]
#     sum_list.sort()
#     return int(sum_list[1])+int(sum_list[2])
#
# num=0
# number_array=[]
# while num<3:
#     number_array.append(input("Введите число:\n"))
#     num+=1
# print(number_array)
#
# final_sum=sum_of_2(number_array[0],number_array[1],number_array[2])
#
# print(final_sum)



# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#
# def my_pow(num, pokazatel):
#   return (num**pokazatel)
#
# def my_pow2(num, pokazatel):
#     num_pow=1
#     for i in range(abs(pokazatel)):
#         num_pow=num_pow*num
#     if pokazatel<0:
#         num_pow=1/(num_pow)
#     return num_pow
#
# num = int(input("Введите число:\n"))
# pokazatel = int(input("Введите показатель степени:\n"))
#
# print("Первый способ:"+str(my_pow(num,pokazatel)))
# print("Второй способ:"+str(my_pow2(num,pokazatel)))


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# # Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# # к полученной ранее сумме и после этого завершить программу.
#
# cycle =0
# amount = 0
# answ="строка"
# print("Вводите числа, разделенные пробелом. Кнопка 'Enter' - определение суммы, кнопка 'Q' - выход.")
#
# def string_sum(a):
#     loc_amount=0
#     a = list(a.split(" "))
#     for i in range(len(a)):
#         loc_amount = loc_amount + int(a[i - 1])
#     return loc_amount
#
# while True:
#     cycle+=1
#     answ = input().upper()
#     try:
#         pos=answ.index("Q")
#         amount+=string_sum(answ[0:pos-1])
#         print("Сумма:" + str(amount))
#         break
#     except ValueError:
#         amount += string_sum(answ)
#         print("Сумма:" + str(amount))




#
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def my_cap(s):
    s= s.capitalize()
    return s

print("Введите слово:")
s = str(input())

print(my_cap(s))
print("Введите строку:")
s = str(input())
s = list(s.split(" "))

for i in range(len(s)):
    s[i]=my_cap(s[i])
s = ' '.join(s)
print(s)

