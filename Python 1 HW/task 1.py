# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input("Введите обозначение Вашего дня недели (цифра от 1 до 7), а я скажу, выходной ли у Вас: "))

if number > 0 and number < 6:
    print("Жаль, но у Вас будний день")
elif number == 6 or number == 7:
    print("Поздравляю, у Вас выходной")
else:
    print("Кажется, Вы ввели не то, что было запрошено, повторите ещё раз")


