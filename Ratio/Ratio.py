from Natural import Natural
from Integer import Integer



class Rational:
    def __init__(self, num, denum):
        self.numerator = Integer(num)
        self.denumerator = Natural(denum)
    
    
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denumerator == other.denumerator
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return f'{self.numerator} {self.denumerator}'
    
    def __repr__(self):
        return self.__str__()
    
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

    
    def TRANS_Q_Z(self):
        return Integer(str(self.RED_Q_Q().numerator))
    
    def ADD_QQ_Q(self, other):
        Denum = self.denumerator.LCM_NN_N(other.denumerator)
        Num = self.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(self.denumerator))))
        Num = Num.ADD_ZZ_Z(other.numerator.MUL_ZZ_Z(Integer(str(Denum.DIV_NN_N(other.denumerator)))))
        SUM = Rational(str(Num), str(Denum)).RED_Q_Q()
        return SUM
    
    def SUB_QQ_Q(self, other):
        Opposite = Rational(str(other.numerator.MUL_ZM_Z()), str(other.denumerator))
        SUB = self.ADD_QQ_Q(Opposite)
        return SUB
    
    def MUL_QQ_Q(self, other):
        NUM = self.numerator.MUL_ZZ_Z(other.numerator)
        DENUM = self.denumerator.MUL_NN_N(other.denumerator)
        MUL = Rational(str(NUM), str(DENUM)).RED_Q_Q()
        return MUL
    
    def DIV_QQ_Q(self, other):
        NUM = Integer(str(other.denumerator))
        DENUM = other.numerator.TRANS_Z_N()
        if other.numerator.POZ_Z_D() == 1:
            NUM = NUM.MUL_ZM_Z()
        DIV = self.MUL_QQ_Q(Rational(str(NUM), str(DENUM)))
        return DIV