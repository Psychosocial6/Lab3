import constants, checker
from methods import trapezoid, rectangles, simpson
def read():
    while True:
        while True:
            print("Выберите функцию:")
            for key in constants.functions:
                print(f"{key} - {(constants.functions[key]).f_string}")
            num = input().strip()
            if num in constants.functions:
                function = constants.functions[num]
                break
            else:
                print("Неверный выбор, повторите попытку")
        while True:
            print("Выберите промежуток интегрирования: границы через пробел")
            try:
                a, b = map(float, input().split())
                if (a < b):
                    break
                else:
                    print("Неверный промежуток, левая граница должна быть меньше")
            except Exception:
                print("Ошибка, повторите ввод")
        while True:
            print("Укажите точность интегрирования:")
            try:
                eps = float(input())
                if eps > 0:
                    break
                else:
                    print("Неверное значение, повторите ввод")
            except Exception:
                print("Неверное значение, повторите ввод")
        if not checker.check(function, a, b):
            print("Интеграл расходится")
        else:
            while True:
                print("Выберите метод:\n1 - Метод прямоугольников\n2 - Метод трапеций\n3 - Метод Симпсона")
                try:
                    num = int(input())
                    if num == 1:
                        while True:
                            print("Выберите версию метода:\n1 - Средних прямоугольников\n2 - Левых прямоугольников\n3 - Правых прямоугольников")
                            try:
                                x = int(input())
                                if x == 1:
                                    mode = "mid"
                                    break
                                elif x == 2:
                                    mode = "left"
                                    break
                                elif x == 3:
                                    mode = "right"
                                    break
                                else:
                                    print("Ошибка, повторите выбор")
                            except Exception:
                                print("Ошибка, повторите выбор")
                        I, n = rectangles.solve(mode, function, a, b, eps)
                        print(f"Значение интеграла: {I}\nЧисло разбиения: {n}")
                        break
                    if num == 2:
                        I, n = trapezoid.solve(function, a, b, eps)
                        print(f"Значение интеграла: {I}\nЧисло разбиения: {n}")
                        break
                    if num == 3:
                        I, n = simpson.solve(function, a, b, eps)
                        print(f"Значение интеграла: {I}\nЧисло разбиения: {n}")
                        break
                    else:
                        print("Ошибка, повторите выбор")
                except Exception:
                    print("Ошибка, повторите выбор")