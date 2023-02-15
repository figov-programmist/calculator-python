import math
    calc = input("Выбери знак (+,-,*,/")
if calc == "+":
    number1 = int(input("Введи первое число "))
    number2 = int(input("Введи второе число "))
    numb = number1 + number2 
    print("Ответ: ", int(numb))
if calc == "-":
    number1 = int(input("Введи первое число "))
    number2 = int(input("Введи второе число "))
    numb = number1 - number2
    print("Ответ: ", int(numb))
if calc == "*":
    number1 = int(input("Введи второе число "))
    number2 = int(input("Введи второе число "))
    numb = number1 * number2
    print("Ответ: ", int(numb))
if calc == "/":
    number1 = int(input("Введи первое число "))
    number2 = int(input("Введи второе число "))
    numb = number1 / number2 
    print("Ответ: ", int(numb))