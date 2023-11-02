//
// Created by gidra on 02.11.23.
//

#include "Rational.h"
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
    //return <#initializer#>;
}

bool Rational::INT_Q_B() {
    return false;
}

Integer &Rational::TRANS_Q_Z() const {
    //return <#initializer#>;
}

Rational &Rational::ADD_QQ_Q(const Rational &) const {
    //return <#initializer#>;
}

Rational &Rational::SUB_QQ_Q(const Rational &) const {
    //return <#initializer#>;
}

Rational &Rational::MUL_QQ_Q(const Rational &) const {
    //return <#initializer#>;
}

Rational &Rational::DIV_QQ_Q(const Rational &) const {
    //
}
