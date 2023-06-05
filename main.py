# Простое
# Принять у пользователя 2 числа и вывести результат работы простых математических операций между ними
# Числа принимаются до тех пор пока не будет введенно 0 и 0

def easy():
    print("Числа принимаются до тех пор пока не будет введенно 0 и 0")
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    boolean = True

    while boolean:
        if a == 0 and b == 0:
            print("Выход из цикла")
            break
        res_plus = a + b
        res_minus = a - b
        res_multiply = a * b
        res_divide = a / b

        print("Результат сложения -> \t" + str(a) + " + " + str(b) + " = " + str(res_plus))
        print( "Результат вычитания -> \t" + str(a)  + " - " +  str(b) + " = " + str(res_minus))
        print( "Результат умножения -> \t" + str(a)  + " * " + str(b) + " = " +str(res_multiply))
        print( "Результат деления -> \t" + str(a)  + " / " + str(b) + " = " + str(res_divide))
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))


# Среднее
# Модифицировать прошлое дз дав пользователю выбирать какую операцию между числами применять

def middle():
    plus = "+"
    minus = "-"
    multiply = "*"
    divide = "/"
    print("Числа принимаются до тех пор пока не будет введенно 0 и 0")
    a = int(input("Введите первое число  ->  "))
    operator = input("Ввыберите оператор: ' + ' ' - ' ' / ' ' * ' -> ")
    b = int(input("Введите второе число  ->  "))

    boolean = True

    while boolean:
        if a == 0 and b == 0:
            print("Выход из цикла")
            break
        if operator != plus and operator != minus and operator != multiply and operator != divide:
            operator = input("Ввыберите корректный оператор: ' + ' ' - ' ' / ' ' * ' -> ")
        else:
            if operator == plus:
                res_plus = a + b
                print("Результат сложения -> \t" + str(a) + " + " + str(b) + " = " + str(res_plus))
            elif operator == minus:
                res_minus = a - b
                print("Результат вычитания -> \t" + str(a) + " - " + str(b) + " = " + str(res_minus))
            elif operator == multiply:
                res_multiply = a * b
                print( "Результат умножения -> \t" + str(a)  + " * " + str(b) + " = " +str(res_multiply))
            elif operator == divide:
                if b != 0:
                    res_divide = a / b
                    print("Результат деления -> \t" + str(a) + " / " + str(b) + " = " + str(res_divide))
                else:
                    print("Деление на ноль недопустимо.")

            a = int(input("Введите первое число: "))
            operator = input("Ввыберите оператор: ' + ' ' - ' ' / ' ' * ' -> ")
            b = int(input("Введите второе число: "))

# Сложное
# Принять число и вывести Фибона́ччи до этого значения
#
# Fn = Fn–2 + Fn–1, где F0=0, F1=1, а n — больше или равно 2 и является целым числом.
# Рассчитанная по этой формуле последовательность выглядит так: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,

def difficult():
    a = int(input("Введите число до которого будет выведено Фибона́ччи-> "))

    F0 = 0
    F1 = 1
    Fn = 0
    fb = []

    while Fn < a:
        fb.append(str(Fn))
        Fn = F0 + F1
        F0 = F1
        F1 = Fn

    res = ",\t".join(fb)
    print("Fibonacci ->")
    print("\t" * 4 + res)


difficulty = [easy, middle, difficult]

while True:
    choice = int(input("Выберите сложность задания 1 - легкое, 2 - среднее, 3 - сложное (0 - выход) -> "))

    if choice == 0:
        print("Выход из программы")
        break
    elif choice >= 1 and choice <= 3:
        val = difficulty[choice - 1]
        val()
    else:
        print("Введите корректное значение в диапазоне от 1 до 3")



