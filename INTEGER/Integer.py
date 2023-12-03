# импортируем модуль Natural для работы с натуральными числами
from Natural import Natural

# определяем класс Integer для работы с целыми числами
class Integer:

    # конструктор класса Integer
    def __init__(self, s):
        # принимает на вход строку s, представляющую целое число
        # если строка пустая или содержит недопустимые символы, то создает пустой объект
        # иначе создает объект с атрибутами sign и number, где sign - знак числа, number - натуральное число
        self.sign = 0 # по умолчанию знак равен нулю
        self.number = Natural("") # по умолчанию число равно нулю
        if s == "": # если строка пустая
            return # возвращаем пустой объект
        if s[0] == "-": # если строка начинается с минуса
            self.sign = 1 # устанавливаем знак равным единице
            s = s[1:] # отбрасываем минус из строки
        try: # пытаемся создать натуральное число из оставшейся строки
            self.number = Natural(s) # если успешно, то присваиваем его атрибуту number
        except: # если возникла ошибка
            self.sign = 0 # обнуляем знак
            self.number = Natural("") # обнуляем число
            return # возвращаем пустой объект

    # переопределяем вывод
    def __str__(self):
        # проходимся по массиву в обратном порядке и объединяем его в строчку
        out = ''.join([str(el) for el in self.number.Arr[::-1]])
        # Проверяем наличие знака
        if self.sign == 1:  # Если sign = 1, значит знак отрицательный, добавляем его к строке
            out = '-' + out
        return out

    # метод для копирования объекта класса Integer
    @staticmethod
    def copy(x):
        # принимает на вход объект класса Integer x
        # возвращает новый объект класса Integer, равный x
        res = Integer("") # создаем пустой объект
        res.sign = x.sign # копируем знак
        res.number = Natural.copy(x.number) # копируем число
        return res # возвращаем копию

    # метод для модуля целого числа
    def ABS_Z_N(self):
        # возвращает натуральное число, равное модулю данного целого числа
        return Natural.copy(self.number) # возвращаем копию числа

    # метод для определения положительности целого числа
    def POZ_Z_D(self):
        # возвращает:
        # 2, если число положительное
        # 0, если число равно нулю
        # 1, если число отрицательное
        if self.number.n == 1 and self.number.Arr[0] == 0: # если число равно нулю
            return 0 # возвращаем 0
        elif self.sign == 0: # если знак равен нулю
            return 2 # возвращаем 2
        else: # если знак равен единице
            return 1 # возвращаем 1

    # метод для умножения целого числа на (-1)
    def MUL_ZM_Z(self):
        # возвращает целое число, равное данному, умноженному на (-1)
        res = Integer.copy(self) # копируем данное число
        if res.number.n == 1 and res.number.Arr[0] == 0: # если число равно нулю
            return res # возвращаем его же
        else: # если число не равно нулю
            res.sign = 1 - res.sign # меняем знак на противоположный
            return res # возвращаем результат

    # метод для преобразования натурального числа в целое
    @staticmethod
    def TRANS_N_Z(x):
        # принимает на вход объект класса Natural x
        # возвращает объект класса Integer, равный x
        res = Integer("") # создаем пустой объект
        res.sign = 0 # устанавливаем знак равным нулю
        res.number = Natural.copy(x) # копируем натуральное число
        return res # возвращаем результат

    # метод для преобразования целого неотрицательного числа в натуральное
    def TRANS_Z_N(self):
        # возвращает натуральное число, равное данному целому неотрицательному числу
        # если число отрицательное, то возвращает пустой объект
        if self.sign == 0: # если знак равен нулю
            return Natural.copy(self.number) # возвращаем копию числа
        else: # если знак равен единице
            return Natural("") # возвращаем пустой объект

    # метод для сложения двух целых чисел
    def ADD_ZZ_Z(self, other):
        # принимает на вход объект класса Integer other
        # возвращает объект класса Integer, равный сумме данного и other
        res = Integer("") # создаем пустой объект
        if self.sign == other.sign: # если знаки совпадают
            res.sign = self.sign # устанавливаем знак равным одному из них
            res.number = self.number.ADD_NN_N(other.number) # складываем числа как натуральные
        else: # если знаки различаются
            if self.number.COM_NN_D(other.number) == 2: # если первое число больше второго
                res.sign = self.sign # устанавливаем знак равным знаку первого числа
                res.number = self.number.SUB_NN_N(other.number) # вычитаем из первого числа второе как натуральные
            elif self.number.COM_NN_D(other.number) == 1: # если второе число больше первого
                res.sign = other.sign # устанавливаем знак равным знаку второго числа
                res.number = other.number.SUB_NN_N(self.number) # вычитаем из второго числа первое как натуральные
            else: # если числа равны
                res.sign = 0 # устанавливаем знак равным нулю
                res.number = Natural("0") # устанавливаем число равным нулю
        return res # возвращаем результат

    # метод для вычитания одного целого числа из другого
    def SUB_ZZ_Z(self, other):
        # принимает на вход объект класса Integer other
        # возвращает объект класса Integer, равный разности данного и other
        res = Integer("") # создаем пустой объект
        if self.sign == other.sign: # если знаки совпадают
            if self.number.COM_NN_D(other.number) == 2: # если первое число больше второго
                res.sign = self.sign # устанавливаем знак равным знаку одного из них
                res.number = self.number.SUB_NN_N(other.number) # вычитаем из первого числа второе как натуральные
            elif self.number.COM_NN_D(other.number) == 1: # если второе число больше первого
                res.sign = 1 - self.sign # устанавливаем знак равным противоположному знаку одного из них
                res.number = other.number.SUB_NN_N(self.number) # вычитаем из второго числа первое как натуральные
            else: # если числа равны
                res.sign = 0 # устанавливаем знак равным нулю
                res.number = Natural("0") # устанавливаем число равным нулю
        else: # если знаки различаются
            res.sign = self.sign # устанавливаем знак равным знаку первого числа
            res.number = self.number.ADD_NN_N(other.number) # складываем числа как натуральные
        return res

    # метод для умножения двух целых чисел
    def MUL_ZZ_Z(self, other):
        # принимает на вход объект класса Integer other
        # возвращает объект класса Integer, равный произведению данного и other
        res = Integer("")  # создаем пустой объект
        # если хотя бы один ноль, то возвращаем ноль
        # (чтобы не проходить по всем функциям и не париться по поводу знака)
        if self.number.n == 1 and self.number.Arr[0] == 0 or other.number.n == 1 and other.number.Arr[0] == 0:
            return res  # возвращаем пустой объект
        # определяем знак результата
        if (self.sign == 1 and other.sign == 1) or (self.sign == 0 and other.sign == 0):
            res.sign = 0  # знак равен нулю
        else:
            res.sign = 1  # знак равен единице
        # вычисляем модуль результата
        res.number = self.number.MUL_NN_N(other.number)  # умножаем числа как натуральные
        return res  # возвращаем результат

    # метод для частного от деления целого на целое
    def DIV_ZZ_Z(self, other):
        # принимает на вход объект класса Integer other
        # возвращает объект класса Integer, равный частному от деления данного на other
        # если other равен нулю, то возвращает пустой объект
        res = Integer("")  # создаем пустой объект
        if other.number.n == 1 and other.number.Arr[0] == 0:  # если other равен нулю
            return res  # возвращаем пустой объект
        # находим частное вне зависимости от знаков
        res.number = self.number.DIV_NN_N(other.number)  # делим числа как натуральные
        # если хотя бы один знак отрицателен, прибавляем к частному 1
        if self.sign == 1 or other.sign == 1:
            # если остаток не равен нулю, то действуем
            if self.number.MOD_NN_N(other.number).n > 1 or self.number.MOD_NN_N(other.number).Arr[0] != 0:
                res.number = res.number.ADD_1N_N()  # прибавляем к частному 1
            # если отрицательно только одно число, делаем частное отрицательным
            if (self.sign == 1 and other.sign == 0) or (self.sign == 0 and other.sign == 1):
                res.sign = 1  # знак равен единице
        return res  # возвращаем результат

    # метод для остатка от деления целого на целое
    def MOD_ZZ_Z(self, other):
        # принимает на вход объект класса Integer other
        # возвращает объект класса Integer, равный остатку от деления данного на other
        # если other равен нулю, то возвращает пустой объект
        res = Integer("")  # создаем пустой объект
        if other.number.n == 1 and other.number.Arr[0] == 0:  # если other равен нулю
            return res  # возвращаем пустой объект
        # сразу делаем остаток положительным
        res.sign = 0  # знак равен нулю
        # находим остаток вне зависимости от знаков
        res.number = self.number.MOD_NN_N(other.number)  # делим числа как натуральные
        # если остаток не равен нулю
        if res.number.n > 1 or res.number.Arr[0] != 0:
            # если хотя бы одно число отрицательно, то действуем по формуле
            # res = other - (self mod other)
            if self.sign == 1 or other.sign == 1:
                res.number = other.number.SUB_NN_N(res.number)  # вычитаем из other остаток
        return res  # возвращаем результат
