from Ratio import Rational, Natural, Integer

# определяем класс Polynom для работы с многочленами
class Polynom:

    # конструктор класса Polynom
    def __init__(self, parts: list):
        # принимает на вход строку s, представляющую многочлен
        # если строка пустая или содержит недопустимые символы, то создает пустой объект
        # иначе создает объект с атрибутами degree и coefficients, где degree - степень многочлена, coefficients - список коэффициентов
        self.degree = 0 # по умолчанию степень равна нулю
        self.coefficients = [] # по умолчанию список коэффициентов пуст
        # if parts == []: # если строка пустая
        #     return # возвращаем пустой объект
        try:
            # tmp = parts[:]
            # # print(tmp)
            # for i in range(len(tmp)):
            #     if tmp[i].numerator.number.NZER_N_B() == False:
            #         # print(i)
            #         parts.pop(i)
            #     else:
            #         break
            self.degree = len(parts)-1 # преобразуем первую часть в целое число и присваиваем ее атрибуту degree
            if self.degree < 0: # если степень меньше нуля
                raise ValueError # возбуждаем исключение
            self.coefficients = [el for el in parts]
            for i in range(len(self.coefficients)):
                if type(self.coefficients[i]) == Integer:
                    self.coefficients[i] = Rational(str(self.coefficients[i]), '1')
        except: # если возникла ошибка
            self.degree = 0 # обнуляем степень
            self.coefficients = [] # обнуляем список коэффициентов
        print(self.coefficients)
            
        

    # переопределяем вывод
    def __str__(self):
        # проходимся по массиву в обратном порядке и объединяем его в строчку
        s = []
        for i in range(self.degree+1):
            s.append(str(self.coefficients[i])+'x^' + str(i))
        return ' + '.join(s[::-1])

    def get_coef(self):
        return self.coefficients

    # метод для копирования объекта класса Polynom
    @staticmethod
    def copy(x):
        # принимает на вход объект класса Polynom x
        # возвращает новый объект класса Polynom, равный x
        res = Polynom([]) # создаем пустой объект
        res.degree = x.degree # копируем степень
        for i in range(len(x.coefficients)): # для каждого коэффициента
            res.coefficients.append(x.coefficients[i]) # копируем рациональное число и добавляем его в список коэффициентов
        return res # возвращаем копию

    # метод для сложения двух многочленов
    def ADD_PP_P(self, other):
        # принимает на вход объект класса Polynom other
        # возвращает объект класса Polynom, равный сумме данного и other
        res = Polynom([]) # создаем пустой объект
        if self.degree > other.degree: # если степень первого многочлена больше степени второго
            res.degree = self.degree # устанавливаем степень результата равной степени первого многочлена
            for i in range(other.degree + 1): # для каждого коэффициента второго многочлена
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i])) # складываем соответствующие коэффициенты обоих многочленов и добавляем их в список коэффициентов результата
            for i in range(other.degree + 1, self.degree + 1): # для оставшихся коэффициентов первого многочлена
                res.coefficients.append(Rational.copy(self.coefficients[i])) # копируем их и добавляем в список коэффициентов результата
        elif self.degree < other.degree: # если степень второго многочлена больше степени первого
            res.degree = other.degree # устанавливаем степень результата равной степени второго многочлена
            for i in range(self.degree + 1): # для каждого коэффициента первого многочлена
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i])) # складываем соответствующие коэффициенты обоих многочленов и добавляем их в список коэффициентов результата
            for i in range(self.degree + 1, other.degree + 1): # для оставшихся коэффициентов второго многочлена
                res.coefficients.append(Rational.copy(other.coefficients[i])) # копируем их и добавляем в список коэффициентов результата
        else: # если степени многочленов равны
            # print('tut')
            res.degree = self.degree # устанавливаем степень результата равной степени одного из них
            for i in range(self.degree + 1): # для каждого коэффициента
                res.coefficients.append(self.coefficients[i].ADD_QQ_Q(other.coefficients[i])) # складываем соответствующие коэффициенты обоих многочленов и добавляем их в список коэффициентов результата
            while res.degree > 0 and res.coefficients[res.degree].INT_Q_B() and res.coefficients[res.degree].numerator.number.n == 1 and res.coefficients[res.degree].numerator.number.Arr[0] == 0: # пока степень результата больше нуля и старший коэффициент равен нулю
                res.degree -= 1 # уменьшаем степень результата на единицу
                res.coefficients.pop() # удаляем старший коэффициент из списка
        return res # возвращаем результат

    # метод для вычитания одного многочлена из другого

    def SUB_PP_P(self, other):
        # print(self)
        
        tmp = other.coefficients[:]
        res = Polynom(tmp)
        # print(res)
        for i in range(len(other.coefficients)):
            res.coefficients[i] = Rational(str(res.coefficients[i].numerator.MUL_ZM_Z()), str(res.coefficients[i].denumerator))
        # print(res)
        return self.ADD_PP_P(res)

    # метод для умножения многочлена на рациональное число
    def MUL_PQ_P(self, other):
        # принимает на вход объект класса Rational other
        # возвращает объект класса Polynom, равный произведению данного многочлена на other
        res = Polynom([])  # создаем пустой объект
        res.degree = self.degree  # устанавливаем степень результата равной степени данного многочлена
        for i in range(self.degree + 1):  # для каждого коэффициента данного многочлена
            res.coefficients.append(self.coefficients[i].MUL_QQ_Q(other))  # умножаем его на other и добавляем в список коэффициентов результата
        return res  # возвращаем результат

    # метод для умножения многочлена на x^k
    def MUL_Pxk_P(self, k):
        # принимает на вход натуральное число k
        
        # возвращает объект класса Polynom, равный произведению данного многочлена на x^k
        res = Polynom([])  # создаем пустой объект
        res.degree = self.degree + k  # устанавливаем степень результата равной сумме степени данного многочлена и k
        for i in range(k):  # для первых k коэффициентов
            res.coefficients.append(Rational("0", '1'))  # добавляем нули в список коэффициентов результата
        for i in range(self.degree + 1):  # для оставшихся коэффициентов
            res.coefficients.append(Rational.copy(self.coefficients[i]))  # копируем коэффициенты данного многочлена и добавляем в список коэффициентов результата
        return res  # возвращаем результат

    # метод для старшего коэффициента многочлена
    def LED_P_Q(self):
        # возвращает рациональное число, равное старшему коэффициенту данного многочлена
        return Rational.copy(self.coefficients[self.degree])  # копируем старший коэффициент и возвращаем его

    # метод для высшей степени многочлена
    def DEG_P_N(self):
        # возвращает натуральное число, равное степени данного многочлена
        return Natural(str(self.degree))  # преобразуем степень в строку и создаем из нее натуральное число
    
    # Вынесение НОК числителей и НОД знаменателей
    def FAC_P_Q(self):
        coef = self.coefficients[:]
        nums = [i.numerator.number for i in coef]
        dens = [i.denumerator for i in coef]
        tmp_num = nums[0]
        for i in range(1, len(nums)):
            tmp_num = tmp_num.LCM_NN_N(nums[i])
        tmp_den = dens[0]
        for i in range(1, len(dens)):
            tmp_den = tmp_den.GCF_NN_N(dens[i])
        return Rational(str(tmp_num), str(tmp_den))

    # Умножение полиномов
    def MUL_PP_P(self, other):
        
        result = Polynom([])
        result.degree = self.degree + other.degree
        for i in range(result.degree+1):
            result.coefficients.append(Rational('0', '1'))
        # print(result)
        for k in range(result.degree+1):
            for i in range(k+1):
                j = k - i
                if (j <= other.degree) and (i <= self.degree):
                    tmp = self.coefficients[i].MUL_QQ_Q(other.coefficients[j])
                    # print(tmp)
                    # print(result.coefficients[k])
                    result.coefficients[k] = result.coefficients[k].ADD_QQ_Q(tmp)
        return result

    # Частное от деления полинома на полином при делении с остатком
    def DIV_PP_P(self, other):
        n = self.degree
        m = other.degree
        self_copy = Polynom(self.coefficients)
        if self.degree < other.degree:
            return 0
        result = Polynom([Rational('0', '1') for _ in range(n - m + 1)])
        for i in range(n, m - 1, -1):
            result.coefficients[i - m] = self_copy.coefficients[i].DIV_QQ_Q(other.coefficients[m])
            for j in range(m, -1 , -1):
                self_copy.coefficients[i - m + j] = self_copy.coefficients[i - m + j].SUB_QQ_Q(other.coefficients[j].MUL_QQ_Q(result.coefficients[i-m]))
        return result
        

    # Остаток от деления полинома на полином при делении с остатком
    def MOD_PP_P(self, other):
        if self.degree < other.degree:
            return self
        # print(f'A: {self} \nB: {other}')
        coef = self.coefficients[:]
        result = Polynom(coef)
        # tmp = self.DIV_PP_P(other)
        # print(result)
        # print(other)
        # print(tmp)
        # tmp2 = other.MUL_PP_P(tmp)
        # print(tmp2)
        # tmp3 = result.SUB_PP_P(tmp2)

        # return tmp3.DIV_PP_P(Polynom([tmp3.coefficients[-1]]))
        # print('mod: ', result.SUB_PP_P(other.MUL_PP_P(self.DIV_PP_P(other))))
        return result.SUB_PP_P(other.MUL_PP_P(self.DIV_PP_P(other)))
    
    # НОД полиномов
    def GCF_PP_P(self, other):
        def zip_longest_custom(*iterables, fillvalue=Rational('0', '1')):
            # Находим максимальную длину среди всех итерируемых объектов
            max_length = max(len(iterable) for iterable in iterables)
            # Итерируемся по индексам от 0 до максимальной длины
            for i in range(max_length):
                yield tuple(iterable[i] if i < len(iterable) else fillvalue for iterable in iterables)

        def compare_polynomials(poly1, poly2):
            if len(poly1) > len(poly2):
                return 1
            if len(poly1) < len(poly2):
                return -1
            for elem1, elem2 in list(zip_longest_custom(poly1, poly2)):
                if elem1 > elem2:
                    return 1
                elif elem1 == elem2:
                    continue
                else:
                    return -1
            return 0 
                  
        p1 = Polynom(self.coefficients)
        p2 = Polynom(other.coefficients)
        # print(p1)
        # print(p2)
        while compare_polynomials(p1.coefficients, [Rational('0', '1')]) and compare_polynomials(p2.coefficients, [Rational('0', '1')]):
            if p1.degree == p2.degree and compare_polynomials(p1.coefficients, p2.coefficients) == -1:
                # print('tut')
                for i in range(p1.degree+1):
                    p1.coefficients[i] = p1.coefficients[i].MUL_QQ_Q(p2.coefficients[-1])
            # for i in range(len(p2.coefficients)):
            #         # print(p2.coefficients[i])
            #         p2.coefficients[i] = p2.coefficients[i].DIV_QQ_Q(p2.coefficients[-1])
            # print(p1)
            # print(p2)
            # print('')
            if compare_polynomials(p1.coefficients, p2.coefficients) == 1:
                p1, p2 = p2, p1.MOD_PP_P(p2)
                # print(p1)
                # print(p2)
                # print('')
            elif compare_polynomials(p1.coefficients, p2.coefficients) == 1:
                return p1
                return 'error'
        for i in range(len(p1.coefficients)):
            p1.coefficients[i] = p1.coefficients[i].DIV_QQ_Q(p1.coefficients[-1])
        return p1

    # Производная полинома
    def DER_P_P(self):
        # Инициализируем результат пустым списком
        result = []
        # Перебираем все коэффициенты полинома, начиная со второго
        for i in range(1, len(self.coefficients)):
            # Умножаем коэффициент на i
            c = self.coefficients[i].MUL_QQ_Q(Rational(str(i), '1'))
            # Добавляем коэффициент в результат
            result.append(c)
        # Создаем полином из результата
        result = Polynom(result)
        # Возвращаем результат
        return result

    # Преобразование полинома — кратные корни в простые
    def NMR_P_P(self):
        # Находим НОД полинома и его производной
        g = self.GCF_PP_P(self.DER_P_P())
        # Делим полином на НОД
        result = self.DIV_PP_P(g)
        # Возвращаем результат
        # return g
        return result
