# определяем класс Natural для натуральных чисел
class Natural:
    # конструктор, принимающий строку
    def __init__(self, number):
        # считается, что строка подана уже пройдя валидацию и в ней нет всякого рода "мусора"
        self.n = len(number)  # длина числа
        self.Arr = [int(digit) for digit in number[::-1]]  # список цифр в обратном порядке

    # конструктор, принимающий список и длину
    @classmethod
    def from_list(cls, lst, n):
        # присваиваем старшему разряду число n, переданное в функцию
        self = cls.__new__(cls)
        self.n = n
        self.Arr = lst.copy()
        return self

    # конструктор, копирующий другое натуральное число
    @classmethod
    def copy(cls, other):
        # копирует переданное натуральное число в новое
        self = cls.__new__(cls)
        self.n = other.n
        self.Arr = other.Arr.copy()
        return self

    # оператор присваивания
    def __eq__(self, other):
        # копирует переданное натуральное число в текущее
        self.n = other.n
        self.Arr = other.Arr.copy()
        return self

    # перегрузка оператора вывода
    def __str__(self):
        return ''.join([str(el) for el in self.Arr[::-1]])

    # метод сравнения двух натуральных чисел

    # created by Berezin_Dmitry
    def COM_NN_D(self, other):
        # метод сравнивает два числа:
        # если числа равны возвращает 0
        # если первое число меньше второго возвращает 1
        # если первое число больше второго возвращает 2

        if (self.n > other.n):
            return 2  # если длина 2-го числа > длины 1 - го
        elif (self.n < other.n):
            return 1  # если длина 1-го числа < длины 2-го числа
        else:  # случай когда длины чисел одинаковые
            for i in range(self.n - 1, - 1, -1):  # проходим циклом с наибольшего элемента до наименьшего
                if (self.Arr[i] > other.Arr[
                    i]):  # если i-я цифра первого числа больше i-ой цифры 2-го числа возвращаем 2
                    return 2
                if (other.Arr[i] > self.Arr[
                    i]):  # если i-я цифра вторго числа больше i-ой цифры 1-го числа возвращаем 1
                    return 1
            return 0  # если прошли все цифры и не нашлось какой-то большей возвращаем 0

    # created by Berezin_Dmitry

    def NZER_N_B(self):
        # метод проверяет является ли число нулем или нет
        # Возвращает False - если число нуль
        # Возвращает True - если число не равно нулю
        if (self.n == 1 and self.Arr[0] == 0):
            return False

        return True

    # created by Grebennikov_Dmitry

    def ADD_1N_N(self):
        # метод добавления 1 к числу
        i = 0
        while (self.Arr[i] == 9):  # двигаем с конца числа, пока i-я цифра = 9
            self.Arr[i] = 0  # все i-е цифры = 9 делаем нулем
            if (i == self.n - 1):  # если дошли до последней цифры
                self.n += 1  # добавляем размер нашему числу
                self.Arr.append(1)  # ставим 1 на место последней цифры
                return self  # возвращем число
            i += 1  # шаг цикла

        self.Arr[i] += 1  # добавляем 1 к числу не равному 1
        return self  # возвращаем число

    # created by Ismailov_Maxim

    def ADD_NN_N(self, other):
        # метод сложения двух чисел
        # алгоритм сложения в столбик

        diff = 0  # остаток
        tmpObj = Natural("0")  # создаем новый объект класса Natural
        # выбираем максимальную длину числа
        if (self.n > other.n):  # если длина 1-го числа > длины 2-го
            max = self.n
        else:  # если длина 2-го числа > длины 1-го
            max = other.n
        for i in range(0, max, 1):
            # в созданный новый объект добавляем сумму двух i-ых цифр 1-го и 2-го числа
            tmpObj.set_arr_by_index(i, (self.get_arr_by_index(i) + other.get_arr_by_index(i) + diff) % 10)
            # поиск остатка:
            diff = ((self.get_arr_by_index(i) + other.get_arr_by_index(i) + diff) // 10)
        if (diff > 0):  # если цикл закончился а остаток не равен нулю
            tmpObj.set_arr_by_index(i + 1, diff)  # добавляем остаток на позицию i + 1
        self = tmpObj
        return self  # возвращаем число

    # created by Grebennikov_Dmitry
    def SUB_NN_N(self, other):
        # вычитает из первого числа второе и возвращает новое число
        # если числа равны, то возвращает ноль
        # если первое число меньше второго, то возвращает пустой объект
        a = Natural.copy(self)  # копируем первое число
        b = Natural.copy(other)  # копируем второе число
        res = Natural("")  # создаем пустой объект для результата
        mass = []  # создаем пустой список для цифр результата
        if a.COM_NN_D(b) == 0:  # если числа равны, то сразу возвращаем ноль
            mass.append(0)
            res.Arr = mass
            res.n = 1
            return res
        elif a.COM_NN_D(b) == 2:  # если первое число больше второго, то продолжаем
            pass
        else:  # если первое число меньше второго, то возвращаем пустой объект
            return res
        i = 0  # индекс для цифр первого числа
        j = 0  # индекс для цифр второго числа
        while j < b.n:  # пока не дойдем до старшего разряда второго числа
            if a.Arr[i] < b.Arr[j]:  # если цифра первого числа меньше цифры второго
                if a.Arr[
                    i + 1] > 0:  # если следующая цифра первого числа не равна нулю, то просто вычитаем из нее единицу
                    a.Arr[i + 1] -= 1
                    if (a.Arr[i + 1] == 0 and i == a.n - 1):
                        a.Arr.pop(i + 1)
                        a.n -= 1
                else:  # если следующая цифра первого числа равна нулю, то идем дальше по разрядам, пока не найдем ненулевую цифру
                    k = i + 1  # индекс для поиска ненулевой цифры
                    while a.Arr[k] == 0:  # пока цифра равна нулю
                        a.Arr[k] = 9  # заменяем ее на девять
                        k += 1  # идем дальше по разрядам
                    a.Arr[k] -= 1  # вычитаем единицу из ненулевой цифры
                    if (a.Arr[k] == 0):  # если k - ый элемент нуль
                        a.Arr.pop(k)  # удаляем его
                        a.n -= 1  # меняем размер на n-1
                mass.append(a.Arr[i] - b.Arr[j] + 10)
            else:  # если цифра первого числа не меньше цифры второго
                mass.append(a.Arr[i] - b.Arr[j])  # добавляем в начало списка разность цифр без заема
            i += 1  # увеличиваем индекс для первого числа
            j += 1  # увеличиваем индекс для второго числа
        while i < a.n:  # если не прошлись по всем разрядам первого числа
            if (a.Arr[i] == 0):  # если k - ый элемент нуль
                a.Arr.pop(i)  # удаляем его
                a.n -= 1  # меняем размер на n-1
            else:
                mass.append(a.Arr[i])  # добавляем в начало списка оставшиеся цифры
            i += 1  # увеличиваем индекс для первого числа
        while (mass[len(mass) - 1] == 0):
            mass.pop()
        res.Arr = mass  # присваиваем список цифр результирующему числу
        res.n = len(mass)  # присваиваем длину списка длине результирующего числа
        return res  # возвращаем результирующее число

    # created by Ismailov_Maxim

    def MUL_ND_N(self, num):
        # метод умножения натурального числа на цифру
        diff = 0  # инициализируем остаток = 0
        tmpObj = Natural("0")  # создадим временный объект класса Natural
        for i in range(0, self.n, 1):  # начнем цикл от 0 до старшего разряда с шагом 1
            # устанавливаем на i - ую позицию значение равное i- ой цифре умноженной на num
            # плюс отстаток от предыдуещей операции по модулю 10
            tmpObj.set_arr_by_index(i, (((self.get_arr_by_index(i) * num) + diff) % 10))
            # остаток равен целочисленному делению i- ой цифры умноженной на num
            # плюс отстаток от предыдуещей операции
            diff = (((self.get_arr_by_index(i) * num) + diff) // 10)
        if (diff > 0):
            # если цикл закончился а остаток не равен нулю
            # добавляем его на место старшего разряда числа + 1
            tmpObj.set_arr_by_index(i + 1, diff)

        while (tmpObj.get_arr_by_index(tmpObj.n - 1) == 0 and tmpObj.n > 1):
            #проверка на то что мы умножили на 0:
            #т.е. если мы число умножаем на 0 его размер не уменьшается во время операций
            #и в этом цикле мы его уменьшаем
            tmpObj.Arr.pop()
            tmpObj.n -= 1
        self = tmpObj
        return self     #возвращаем число

    # created by Ismailov_Maxim

    def MUL_Nk_N(self, k):
        #метод умножения натурального числа на 10^k
        tmpObj = Natural("0")           #создаем временный объект типа Natural
        if (self.NZER_N_B() == False):  #если k = 0 возвращаем наше число
            return self
        for i in range(0, k, 1):
            # цикле от 0 до k ставим на i - ую позицию
            # в созданном объекте ставим 0
            tmpObj.set_arr_by_index(i, 0)
        for i in range(k, k + self.n, 1):
            #далее в цикле от k до k + старший разряд нашего числа
            #добавляем на i - ую позицию временного объякта i - k цифру нашего числа
            tmpObj.set_arr_by_index(i, self.get_arr_by_index(i - k))

        self = tmpObj   #приравниваем временный объект к нашему числу
        return self     #возвращаем его

    # created by Ismailov_Maxim

    def MUL_NN_N(self, other):
        #метод умножения натуральных чисел
        if (self.NZER_N_B() == False):  #проверка на то что первое число равно нулю
            return Natural("0")         #возвращаем нуль
        if (other.NZER_N_B() == False): #проверка на то что второе число равно нулю
            return Natural("0")         #возвращаем нуль

        tmpObj = Natural("0")           #создаем временный объект типа Natural
        for i in range(0, other.n, 1):  #цикл от 0 до старшего разряда n с шагом 1
            #к временному объекту добавляем первое число умноженное на i - ую цифру
            #второго умноженную на 10 ^ i
            tmpObj = tmpObj.ADD_NN_N(self.MUL_ND_N(other.get_arr_by_index(i)).MUL_Nk_N(i))
        self = tmpObj   #приравниваем временный объект к нашему числу
        return self     #возвращаем его

    # created by Ismailov_Maxim

    def SUB_NDN_N(self, other, num):
        #метод вычитания из натурального числа другого натурального
        #умноженного на цифру
        if (self.COM_NN_D(other) == 1):
            return self
        else:
            other = other.MUL_ND_N(num)     #умножаем второе число на цифру
            if (self.COM_NN_D(other) == 1): #проверка на то что второе число умноженное на цифру не больше первого
                return self
            elif (self.COM_NN_D(other) == 0): #проверка на то что второе число умноженное на цифру не равно первому
                return Natural("0")
            else:                             #если ОК тогда
                self = self.SUB_NN_N(other)   #первое число равно первому числу - второе умноженное на num

            return self                       #возвращаем результат

    # created by Ismailov_Maxim
    def DIV_NN_Dk(self, other):
        #метод вычисление первой цифры деления большего натурального числа на меньшее,
        #домноженное на 10^k
        if (self.NZER_N_B() == False):    #проверка на то что 1-ое число не равно нулю
            return Natural("0")
        if (other.NZER_N_B() == False):   #проверка на то что 2-ое число не равно нулю
            return Natural("0")
        if (self.COM_NN_D(other) == 2):   #если первое число больше 2 - го
            larger = self                 #установим меньшее значение равное первому числу
            smaller = other               #установим большее значение равное второму числу
        else:                             #иначе наоборот
            larger = other
            smaller = self
        k = 1   #создаем счетчик номера позиции первой цифры
        # пока меньшее число домноженное на 10^k меньше большего, увеличиваем k
        while (larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 2 or larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 0):
            k += 1
        k -= 1
        #посчитали k, при котором меньшее, домноженное на 10^k,
        # стало больше большего, и вычли из k единицу
        smaller = smaller.MUL_Nk_N(k)   #домножили меньшее на 10^k
        first_digit = Natural("0")      #объект класса Natural для подсчета старшего разряда частного

        while (larger.COM_NN_D(smaller) == 2 or larger.COM_NN_D(smaller) == 0):
            #цикл вычитания из большего меньшего пока большее не станет меньше чем меньшее
            larger = larger.SUB_NN_N(smaller)
            first_digit = first_digit.ADD_1N_N()    #добавляем 1 к нашему начальному значению
        #возвращаем старший разряд умноженный на 10^k, где k - номер позиции этой цифры
        return first_digit.MUL_Nk_N(k)

    # created by Ismailov_Maxim

    def DIV_NN_N(self, other):
        # вычисляет частное от деления и возвращает новое число
        quotient = Natural("")  # объект для хранения первой цифры деления с помощью функции DIV_NN_Dk
        result = Natural("0")  # объект для хранения целой части от деления (результат)

        # необходимо, чтобы self было большим
        if self.NZER_N_B() == False:    #если первое число равно нулю возвращаем нуль
            return Natural("0")
        if self.COM_NN_D(other) == 1:   #если второе число больше первого возвращаем нуль
            return Natural("0")
        elif self.COM_NN_D(other) == 0: #если первое число равно второму вовзращаем 1
            return Natural("1")
        else:
            # делим в первый раз и до тех пор, пока не получим младший разряд
            # также необходимо удостовериться, что мы не будем делить ноль на число
            while (quotient.n > 0 or quotient.Arr == []) and self.Arr[self.n - 1] != 0 and (
                    self.COM_NN_D(other) == 2 or self.COM_NN_D(other) == 0):
                quotient = self.DIV_NN_Dk(other)  # вычисляем первую цифру деления
                self = self.SUB_NN_N(other.MUL_NN_N(quotient))
                result = result.ADD_NN_N(quotient)  # добавляем разряд в конечный результат

        return result  # возвращаем результирующее число

    # created by Berezin_Dmitry

    def MOD_NN_N(self, other):
        #метод поиска отстака от деления двух чисел
        #из первого числа вычитаем ( (первое число поделено целочисленно на второе ) умноженное на второе )
        return self.SUB_NN_N(self.DIV_NN_N(other).MUL_NN_N(other))

    # created by Grebennikov_Dmitry

    def GCF_NN_N(self, other):
        #метод нахождения НОД натуральных чисел
        while (self.NZER_N_B() == True and other.NZER_N_B() == True):   #цикл пока первое и второе число != 0
            if (self.COM_NN_D(other) == 2):                             #если первое число больше второго
                self = self.MOD_NN_N(other)                             #делим с остатком на второе
            else:                                                       #иначе
                other = other.MOD_NN_N(self)                            #второе число делим с остатком на первое
        return self.ADD_NN_N(other)                                     #возвращаем сумму первого и второго после проведенных операций

    # created by Grebennikov_Dmitry

    def LCM_NN_N(self, other):
        #метод нахождения НОК натуральных чисел
        #возвращаем ( первое число умноженное на второе ) целочисленно поделенное на их НОД
        return self.MUL_NN_N(other).DIV_NN_N(self.GCF_NN_N(other))

    # createt by Ismailov_Maxim

    def get_arr_by_index(self, index):
        # вспомогательный метод получения элемента по индексу:
        if (index < self.n):  # если элемент по нужному индексу существует
            return self.Arr[index]  # вернет его
        else:  # иначе возвращает нуль
            return 0

    # created by Ismailov_Maxim

    def set_arr_by_index(self, index, value):
        # вспомогательный метод установки элемента по индексу:
        if (index < self.n):  # если индекс < меньше размера массива
            self.Arr[index] = value  # устанавливаем значение элемента по его индексу
        else:
            # иначе все элементы от размера списка до нужного индекса дообавляются нулями
            for i in range(self.n, index + 1, 1):
                self.Arr.insert(index, 0)
                self.n += 1
            self.Arr[index] = value  # когда дошли до нужного индекса устанавливаем его значение
        return self  # возвращаем список