from Natural import Natural
from Integer import Integer


class Rational:
    def __init__(self, num, denum):
        self.numerator = Integer(num)
        self.denumerator = Natural(denum)

    def __eq__(self, other):
        if self.numerator.number.NZER_N_B() == False and other.numerator.number.NZER_N_B() == False:
            return True
        n1 = self.RED_Q_Q()
        n2 = other.RED_Q_Q()
        return n1.numerator == n2.numerator and n1.denumerator == n2.denumerator

    def __lt__(self, other):
        n1 = self.RED_Q_Q()
        n2 = other.RED_Q_Q()
        t1 = n1.numerator.MUL_ZZ_Z(Integer(str(n2.denumerator)))
        t2 = n2.numerator.MUL_ZZ_Z(Integer(str(n1.denumerator)))
        if t1 < t2:
            return True
        else:
            return False

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        n1 = self.RED_Q_Q()
        n2 = other.RED_Q_Q()
        t1 = n1.numerator.MUL_ZZ_Z(Integer(str(n2.denumerator)))
        t2 = n2.numerator.MUL_ZZ_Z(Integer(str(n1.denumerator)))
        if t1 > t2:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'{self.numerator}/{self.denumerator}'

    def RED_Q_Q(self):
        GCF = self.denumerator.GCF_NN_N(self.numerator.ABS_Z_N())
        gcf_result = Integer(str(GCF))
        RED = Rational(str(self.numerator.DIV_ZZ_Z(gcf_result)), str(self.denumerator.DIV_NN_N(GCF)))
        return RED

    def INT_Q_B(self):
        return self.RED_Q_Q().denumerator.COM_NN_D(Natural("1")) == 0

    @staticmethod
    def TRANS_Z_Q(num_z):
        numerator = Integer.copy(num_z)
        denumerator = Natural('1')
        denum = denumerator.MUL_NN_N(Natural(''.join(str(num_z).split('-'))))
        num = numerator.MUL_ZZ_Z(Integer(str(num_z.ABS_Z_N())))
        result = Rational(str(num), str(denum))
        return result

    @staticmethod
    def copy(x):
        # принимает на вход объект класса Polynom x
        # возвращает новый объект класса Polynom, равный x
        res = Rational('', '')  # создаем пустой объект
        res.numerator = x.numerator  # копируем степень
        res.denumerator = x.denumerator
        return res  # возвращаем копию

    def TRANS_Q_Z(self):
        return Integer(str(self.RED_Q_Q().numerator))

    def ADD_QQ_Q(self, other):
        if self.numerator.number.NZER_N_B() == False:
            return other
        elif other.numerator.number.NZER_N_B() == False:
            return self
        Denum = self.denumerator.LCM_NN_N(other.denumerator)
        Num = self.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(self.denumerator))))
        Num = Num.ADD_ZZ_Z(other.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(other.denumerator)))))
        res = Rational(str(Num), str(Denum)).RED_Q_Q()
        return res

    def SUB_QQ_Q(self, other):
        if self.numerator.number.NZER_N_B() == False:
            return Rational(str(other.numerator.MUL_ZM_Z()), str(other.denumerator))
        Opposite = Rational(str(other.numerator.MUL_ZM_Z()), str(other.denumerator))
        SUB = self.ADD_QQ_Q(Opposite)
        return SUB

    def MUL_QQ_Q(self, other):
        if self.numerator.number.NZER_N_B() == False or other.numerator.number.NZER_N_B() == False:
            return Rational('0', '1')
        NUM = self.numerator.MUL_ZZ_Z(other.numerator)
        DENUM = self.denumerator.MUL_NN_N(other.denumerator)
        MUL = Rational(str(NUM), str(DENUM)).RED_Q_Q()
        return MUL

    def DIV_QQ_Q(self, other):
        NUM = Integer(str(other.denumerator))
        DENUM = other.numerator.ABS_Z_N()
        # print(NUM)
        # print(DENUM)
        if other.numerator.POZ_Z_D() == 1:
            NUM = NUM.MUL_ZM_Z()
        DIV = self.MUL_QQ_Q(Rational(str(NUM), str(DENUM)))
        return DIV
