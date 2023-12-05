# определяем класс Natural для натуральных чисел
class Natural:
    # конструктор, принимающий строку
    def __init__(self, number):
        # считается, что строка подана уже пройдя валидацию и в ней нет всякого рода "мусора"
        self.n = len(number) # длина числа
        self.Arr = [int(digit) for digit in number[::-1]] # список цифр в обратном порядке


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

    # оператор равно == 
    def __eq__(self, other):
        if len(self.Arr) > len(other.Arr):
            return False
        elif len(self.Arr) < len(other.Arr):
            return False
        else:
            for i in range(len(self.Arr)):
                if self.Arr[i] > other.Arr[i]:
                    return False
                elif self.Arr[i] < other.Arr[i]:
                    return False
            return True
    
    def __gt__(self, other):
        if len(self.Arr) > len(other.Arr):
            return True
        elif len(self.Arr) < len(other.Arr):
            return False
        else:
            for i in range(len(self.Arr)):
                if self.Arr[i] > other.Arr[i]:
                    return True
                elif self.Arr[i] < other.Arr[i]:
                    return False
            return False

    def __lt__(self, other):
        if len(self.Arr) > len(other.Arr):
            return False
        elif len(self.Arr) < len(other.Arr):
            return True
        else:
            for i in range(len(self.Arr)):
                if self.Arr[i] > other.Arr[i]:
                    return False
                elif self.Arr[i] < other.Arr[i]:
                    return True
            return False

    def __str__(self):
        return ''.join([str(el) for el in self.Arr[::-1]])

    # метод сравнения двух натуральных чисел

    def COM_NN_D(self, other):
        #метод сравнивает два числа:
        #если числа равны возвращает 0
        #если первое число меньше второго возвращает 1
        #если первое число больше второго возвращает 2

        if (self.n > other.n):
            return 2                                    #если длина 2-го числа > длины 1 - го
        elif(self.n < other.n):
            return 1                                    #если длина 1-го числа < длины 2-го числа
        else: #случай когда длины чисел одинаковые
            for i in range(self.n - 1, - 1, -1):        #проходим циклом с наибольшего элемента до наименьшего
                if (self.Arr[i] > other.Arr[i]):        #если i-я цифра первого числа больше i-ой цифры 2-го числа возвращаем 2
                    return 2
                if (other.Arr[i] > self.Arr[i]):        #если i-я цифра вторго числа больше i-ой цифры 1-го числа возвращаем 1
                    return 1
            return 0                                    #если прошли все цифры и не нашлось какой-то большей возвращаем 0


    def NZER_N_B(self):
        #метод проверяет является ли число нулем или нет
        #Возвращает False - если число нуль
        #Возвращает True - если число не равно нулю
        if (self.n == 1 and self.Arr[0] == 0):
            return False

        return True



    def ADD_1N_N(self):
        #метод добавления 1 к числу
        i = 0
        while(self.Arr[i] == 9):            #двигаем с конца числа, пока i-я цифра = 9
            self.Arr[i] = 0                 #все i-е цифры = 9 делаем нулем
            if (i == self.n - 1):           #если дошли до последней цифры
                self.n += 1                 #добавляем размер нашему числу
                self.Arr.append(1)          #ставим 1 на место последней цифры
                return self                 #возвращем число
            i += 1                          #шаг цикла

        self.Arr[i] += 1                    #добавляем 1 к числу не равному 1
        return  self                        #возвращаем число


    def ADD_NN_N(self, other):
        #метод сложения двух чисел
        #алгоритм сложения в столбик

        diff = 0                            #остаток
        tmpObj = Natural("0")               #создаем новый объект класса Natural
        # выбираем максимальную длину числа
        if (self.n > other.n):              #если длина 1-го числа > длины 2-го
            max = self.n
        else:                               #если длина 2-го числа > длины 1-го
            max = other.n
        for i in range(0, max, 1):
            #в созданный новый объект добавляем сумму двух i-ых цифр 1-го и 2-го числа
            tmpObj.set_arr_by_index(i, (self.get_arr_by_index(i) + other.get_arr_by_index(i) + diff) % 10)
            #поиск остатка:
            diff = ( (self.get_arr_by_index(i) + other.get_arr_by_index(i) + diff) // 10)
        if (diff > 0):                      #если цикл закончился а остаток не равен нулю
            tmpObj.set_arr_by_index(i + 1, diff)
        self = tmpObj
        return  self                        #возвращаем число

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
                if a.Arr[i + 1] > 0:  # если следующая цифра первого числа не равна нулю, то просто вычитаем из нее единицу
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
                    if (a.Arr[k] == 0 and k == a.n - 1):  # если k - ый элемент нуль
                        a.Arr.pop(k)  # удаляем его
                        a.n -= 1  # меняем размер на n-1
                mass.append(a.Arr[i] - b.Arr[j] + 10)
            else:  # если цифра первого числа не меньше цифры второго
                mass.append(a.Arr[i] - b.Arr[j])  # добавляем в начало списка разность цифр без заема
            i += 1  # увеличиваем индекс для первого числа
            j += 1  # увеличиваем индекс для второго числа
        while i < a.n:  # если не прошлись по всем разрядам первого числа
            if (a.Arr[i] == 0 and i == a.n - 1):  # если k - ый элемент нуль
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


    def MUL_ND_N(self, num):
        diff = 0
        tmpObj = Natural("0")
        for i in range (0, self.n, 1):
            tmpObj.set_arr_by_index(i, (((self.get_arr_by_index(i) * num) + diff) % 10 ))
            diff = ( ( (self.get_arr_by_index(i) * num) + diff ) // 10)
        if (diff > 0):
            tmpObj.set_arr_by_index(i + 1, diff)
        k = tmpObj.n
        while (tmpObj.get_arr_by_index(k - 1) == 0 and k > 1):
            tmpObj.Arr.pop()
            tmpObj.n -= 1
            k -= 1
        self = tmpObj
        return self


    def MUL_Nk_N(self, k):
        tmpObj = Natural("0")
        if(self.NZER_N_B() == False):
            return self
        for i in range(0, k, 1):
            tmpObj.set_arr_by_index(i , 0)
        for i in range(k, k + self.n, 1):
            tmpObj.set_arr_by_index(i, self.get_arr_by_index(i - k))

        self = tmpObj
        return self


    def MUL_NN_N(self, other):
        if(self.NZER_N_B() == False):
            return self
        if (other.NZER_N_B() == False):
            return other

        tmpObj = Natural("0")
        for i in range(0, other.n, 1):
            tmpObj = tmpObj.ADD_NN_N(self.MUL_ND_N(other.get_arr_by_index(i)).MUL_Nk_N(i))
        self = tmpObj
        return self


    def SUB_NDN_N(self, other, num):
        if (self.COM_NN_D(other) == 1):
            return self
        else:
            tmpObj = Natural("0")
            other = other.MUL_ND_N(num)
            if (self.COM_NN_D(other) == 1):
                return self
            elif (self.COM_NN_D(other) == 0):
                return  tmpObj
            else:
                tmpObj = self
                tmpObj = tmpObj.SUB_NN_N(other)

            self = tmpObj
            return self
    def DIV_NN_Dk(self, other):
        if (self.NZER_N_B() == False or other.NZER_N_B() == False):
            return Natural("0")
        if (self.COM_NN_D(other) == 2):
            larger = self
            smaller = other
        else:
            larger = other
            smaller = self
        k = 1
        while(larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 2 or larger.COM_NN_D(smaller.MUL_Nk_N(k)) == 0):
            k += 1
        k -= 1
        smaller = smaller.MUL_Nk_N(k)
        first_digit = Natural("0")
        while(larger.COM_NN_D(smaller) == 2 or larger.COM_NN_D(smaller) == 0):
            SaveObj = Natural("0")
            larger = larger.SUB_NN_N(smaller)
            first_digit = first_digit.ADD_1N_N()

        return first_digit.MUL_Nk_N(k)


    def DIV_NN_N(self, other):
        # вычисляет частное от деления и возвращает новое число
        quotient = Natural("")  # объект для хранения первой цифры деления с помощью функции DIV_NN_Dk
        result = Natural("0")  # объект для хранения целой части от деления (результат)

        # необходимо, чтобы self было большим
        if self.NZER_N_B() == False:
            return Natural("0")
        if self.COM_NN_D(other) == 1:
            return Natural("0")
        elif self.COM_NN_D(other) == 0:
            return Natural("1")
        else:
            # делим в первый раз и до тех пор, пока не получим младший разряд
            # также необходимо удостовериться, что мы не будем делить ноль на число
            while (quotient.n > 0 or quotient.Arr == []) and self.Arr[self.n - 1] != 0 and (self.COM_NN_D(other) == 2 or self.COM_NN_D(other) == 0):
                quotient = self.DIV_NN_Dk(other)  # вычисляем первую цифру деления
                self = self.SUB_NN_N(other.MUL_NN_N(quotient))
                result = result.ADD_NN_N(quotient)  # добавляем разряд в конечный результат


        return result  # возвращаем результирующее число


    def MOD_NN_N(self, other):
        return  self.SUB_NN_N(self.DIV_NN_N(other).MUL_NN_N(other))


    def GCF_NN_N(self, other):
        while(self.NZER_N_B() == True and other.NZER_N_B() == True):
            if (self.COM_NN_D(other) == 2):
                self = self.MOD_NN_N(other)
            else:
                other = other.MOD_NN_N(self)
        return  self.ADD_NN_N(other)


    def LCM_NN_N(self, other):
        return self.MUL_NN_N(other).DIV_NN_N(self.GCF_NN_N(other))


    def get_arr_by_index(self, index):
        if (index < self.n):
            return self.Arr[index]
        else:
            return 0

    def set_arr_by_index(self, index, value):
        if(index < self.n):
            self.Arr[index] = value
        else:
            for i in range(self.n, index + 1, 1):
                self.Arr.insert(index, 0)
                self.n += 1
            self.Arr[index] = value
        return  self
