//
// Created by gidra on 02.11.23.
//

#include "Rational.h"
#include "Natural.h"
#include "Integer.h"
Rational::Rational(Integer &num, Natural &denum)
{
    this->numerator = new Integer(num);
    this->denumerator = new Natural(denum);
}
Rational::Rational()
{
    this->numerator = new Integer("+0");
    this->denumerator  = new Natural("1");
}

/******************Конуструктор копирования***************/
Rational::Rational(const Rational &other)
{
    if(this!=&other){
        this->numerator = new Integer(*other.get_NUM());
        this->denumerator = new Natural(*other.get_DENUM());

    }
}


/*****Конструктор приведения целого к рациональному******/
Rational::Rational(const Integer &other)
{
    //Задаем знаменатель равным 1
    this->numerator = new Integer(other);
    int arr[1] = {1};
    this->denumerator = new Natural(arr, 0);
}


/************Перегрузка оператора присваивания***********/
Rational &Rational::operator=(const Rational &other)
{
    if(this!=&other){
        this->numerator = new Integer(*other.get_NUM());
        this->denumerator = new Natural(*other.get_DENUM());
    }

    return *this;
}

Rational::~Rational()
{
    delete numerator;
    delete denumerator;
}

Rational &Rational::RED_Q_Q() const {
    Natural GCF = this->denumerator->GCF_NN_N(this->numerator->ABS_Z_Z());

    Rational* RED = new Rational(this->numerator->DIV_ZZ_Z(GCF),this->denumerator->DIV_NN_N(GCF));
    return *RED;
}

bool Rational::INT_Q_B() const {
    if(this->RED_Q_Q().denumerator->COM_NN_D(Natural("1"))==0)
        return true;
    else
        return false;
}


Integer &Rational::TRANS_Q_Z() const {
    Integer* TRANS = new Integer(*(this->RED_Q_Q().numerator));
    return *TRANS;
}

Rational &Rational::ADD_QQ_Q(const Rational &other) const {
    Natural Denum = this->denumerator->LCM_NN_N(*(other.get_DENUM()));

    //Числитель высчитаем как сумму числителя первого умноженного на дополнительный множитель
    //и втогоро числителя на дополнительный множитель
    Integer Num = this->numerator->MUL_ZZ_Z(Integer(Denum.DIV_NN_N(*(this->denumerator))));
    Num = Num.ADD_ZZ_Z(other.get_NUM()->MUL_ZZ_Z(Integer(Denum.DIV_NN_N(*(other.get_DENUM())))));

    //Сократим результат
    Rational *SUM = new Rational(Rational(Num,Denum).RED_Q_Q());

    return *SUM;
}

Rational &Rational::SUB_QQ_Q(const Rational &other) const {
    Rational Opposite = Rational(other.get_NUM()->MUL_ZM_Z(),*(other.get_DENUM()));
    Rational* SUB = new Rational(this->ADD_QQ_Q(Opposite));

    return *SUB;
}

Rational &Rational::MUL_QQ_Q(const Rational &other) const {
    Integer NUM = this->numerator->MUL_ZZ_Z(*(other.get_NUM()));

    Natural DENUM = this->denumerator->MUL_NN_N(*(other.get_DENUM()));

    //Сокращаем результат
    Rational* MUL = new Rational(Rational(NUM,DENUM).RED_Q_Q());

    return *MUL;
}

Rational &Rational::DIV_QQ_Q(const Rational &other) const {
    Integer NUM = Integer(*other.get_DENUM());
    Natural DENUM = other.get_NUM()->TRANS_Z_N();

    if(other.get_NUM()->POZ_Z_D()==1)
        NUM = NUM.MUL_ZM_Z();


    Rational* DIV = new Rational(this->MUL_QQ_Q(Rational(NUM,DENUM)));

    return *DIV;
}
