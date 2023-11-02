//
// Created by gidra on 02.11.23.
//

#ifndef UNTITLED16_RATIONAL_H
#define UNTITLED16_RATIONAL_H


#include "Natural.h"
#include "Integer.h"

class Rational
{

private:
    Integer* numerator;//Числитель - целое число
    Natural* denumerator;//Знаменатель - натуральное число

public:
    Rational();
    Rational(Integer&,Natural&);//Конструктор, принимающий целую и натуральную составляющие
    Rational(const Rational&);//Конеструктор копировани
    explicit Rational(const Integer&);//Перевод из целого в вещественное
    Rational& operator=(const Rational&);//Перегрузка оператора присваивания

    Rational& RED_Q_Q() const;//Сокращение дроби

    static bool INT_Q_B() ;//Проверка является ли вещественное целым

    Integer& TRANS_Q_Z() const;//Приведение к целому, требует перед этим проверки

    Rational& ADD_QQ_Q(const Rational&) const;//Cумма рациональных чисел

    Rational& SUB_QQ_Q(const Rational&) const;//Разность рациональных чисел

    Rational& MUL_QQ_Q(const Rational&) const;//Произведение рациональных чисел

    Rational& DIV_QQ_Q(const Rational&) const;//Деление рациональных чисел, требуется проверка на 0

    [[nodiscard]] Integer* get_NUM() const{return this->numerator;}//Получение указателя на числитель

    [[nodiscard]] Natural* get_DENUM() const{return this->denumerator;}//Получение указателя на знаменатель

    ~Rational();//Деструктор
};


#endif //UNTITLED16_RATIONAL_H
