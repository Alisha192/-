//
// Created by gidra on 02.11.23.
//

#ifndef UNTITLED16_INTEGER_H
#define UNTITLED16_INTEGER_H


#include <string>
#include "Natural.h"

class Integer
{
private:
    int* Arr;//Массив разрядов числа
    int n;//Номер старшего разряда
    int sign;//Знак числа

public:
    Integer();

    Integer(std::string);//Конструктор принимающий строку
    Integer(const int*, int, int);//Конструктор принимающий массив разрядов, номер старшего разряд и знак

    Integer(const Integer&);//Конструктор копирования

    explicit Integer(const Natural&);//Конструктор преобразования натурального в целое

    Integer & operator=(const Integer&);//Перегрузка оператора присваивания

    Natural & ABS_Z_Z() const;//Модуль целого числа

    static int POZ_Z_D() ;//Возвращение знака числа 2 - положительное, 0 - ноль, 1 - отрицательное

    Integer & MUL_ZM_Z() const;//Умножение целого числа на (-1)

    Natural & TRANS_Z_N() const;//Привод неотрицательного целого к натуральному

    Integer & ADD_ZZ_Z(const Integer &) const;//Сложение целых чисел

    Integer & SUB_ZZ_Z(const Integer &) const;//Вычитание целых чисел

    Integer & MUL_ZZ_Z(const Integer &) const;//Умножение целых чисел

    Integer & DIV_ZZ_Z(const Natural &) const;//Частное от деления с остатком целого на натуральное отличное от нуля

    Integer & MOD_ZZ_Z(const Natural &) const;//Остаток от деления с остатком целого на натуральное отличное от нуля

    [[nodiscard]] int* get_Arr() const {return this->Arr;}
    [[nodiscard]] int get_n() const {return this->n;}
    [[nodiscard]] int get_sign() const {return this->sign;}

    ~Integer();//Деструктор
};



#endif //UNTITLED16_INTEGER_H
