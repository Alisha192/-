//
// Created by gidra on 02.11.23.
//

#ifndef UNTITLED16_NATURAL_H
#define UNTITLED16_NATURAL_H
#include <string>

class Natural
{
private:
    int n;//Номер старшего разряда
    int* Arr;//Указатель на массив разрядов числа
public:
    Natural();
    Natural(std::string);//Конструктор принимающий строку
    Natural(const int*,int);//Конструктор принимающий массив разрядов и номер старшего разряда

    Natural(const Natural &);//Конструктор копирования

    Natural & operator=(const Natural&);//Перегрузка оператора присваивания

    int COM_NN_D(const Natural &) ;//Сравнение двух натуральных 2 - если первое больше второго, 0, если равны, 1 иначе

    bool NZER_N_B() ;//Проверка числа на 0

    Natural & ADD_1N_N();//Добавление единицы к натуральному числу

    Natural & ADD_NN_N(const Natural &);//Сложение натуральных чисел

    Natural & SUB_NDN_N(const Natural&,int) const;//Вычитание из натурального другого натурального, умноженного на цифру

    Natural & SUB_NN_N(const Natural &);//Вычитание из первого большего второго меньшего

    Natural & MUL_ND_N(int);//Умножение натурального на цифру

    Natural & MUL_Nk_N(int);//Умножение натуралного на 10^k

    Natural & MUL_NN_N(const Natural &) const;//Умножение натуральных чисел

    static int DIV_NN_Dk(const Natural&, int) ;//Вычисление первой цифры от деления большего на меньшее с остатком

    Natural & DIV_NN_N(const Natural &) const;//Частное от деления большего натурального числа на меньшее или равное натуральное с остаткомB

    Natural & MOD_NN_N(const Natural &) const;//Остаток от деления большего натурального числа на меньшее или равное

    Natural & GCF_NN_N(const Natural &) const;//НОД двух натурльных чисел

    Natural & LCM_NN_N(const Natural &) const;//НОК двух натуральных чисел

    [[nodiscard]] int get_n() const{return this->n;};//Получить номер старшего разряда
    [[nodiscard]] int* get_Arr() const {return this->Arr;};//Получить указатель на первый элемент массива разрядов
    int get_Arr_by_index(int index) const ;
    void set_Arr_by_index(int index, int value);

    ~Natural();//Деструктор
};

#endif //UNTITLED16_NATURAL_H
