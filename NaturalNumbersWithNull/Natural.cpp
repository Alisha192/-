//
// Created by gidra on 02.11.23.
//

#include "Natural.h"
Natural::Natural()
{
    Natural("0");
}

/*********************************************************/
/************Конструктор, принимающий строку**************/
Natural::Natural(std::string number)
{
    //Считается, что строка подана уже пройдя валидацию и в ней нет всякого рода "мусора"
    this->n = number.size();
    this->Arr = (int*)malloc(sizeof(int)*n);

    //Для удобства будем хранить разряды в обратном порядке
    for(int i = 0;i<this->n;i++)
        this->Arr[i] = number[(this->n-1)-i]-'0';

}
Natural::Natural(const int *arr,const int n)
{

    //Присваиваем старшему разряду число n, переданное в функцию
    this->n = n;
    this->Arr = (int *)malloc(sizeof(int)*n);

    //Поэлементно записываем в массив числа элементы массива, переданного в функцию
    for(int i = 0;i<this->n;i++)
        this->Arr[i] = arr[i];
}


Natural::Natural(const Natural & other)
{
    //Копирует переданное натуральное число в новое
    if(this!=&other){
        this->n = other.get_n();
        this->Arr = (int*)malloc(sizeof(int)*this->n);
        const int *arr = other.get_Arr();
        for(int i = 0;i<n;i++)
            this->Arr[i] = arr[i];
    }

}


Natural& Natural::operator=(const Natural & other)
{
    //Копирует переданное натуральное число в текущее
    if(this!=&other){
        if(this->Arr!=nullptr){
            free(this->Arr);
            this->Arr = nullptr;
        }

        this->n = other.get_n();
        this->Arr = (int*)malloc(sizeof(int)*this->n);
        const int *arr = other.get_Arr();
        for(int i = 0;i<n;i++)
            this->Arr[i] = arr[i];
    }
    return *this;
}

int Natural::COM_NN_D(const Natural &) {
    return 0;
}

bool Natural::NZER_N_B() {
    return false;
}

Natural &Natural::ADD_1N_N() {
    //return <#initializer#>;
}

Natural &Natural::ADD_NN_N(const Natural &) const {
    //return <#initializer#>;
}

Natural &Natural::SUB_NDN_N(const Natural &, int) const {
    //return <#initializer#>;
}

Natural &Natural::SUB_NN_N(const Natural &) const {

    }

Natural &Natural::MUL_ND_N(const int) const {
    //return <#initializer#>;
}

Natural &Natural::MUL_Nk_N(const int) const {
    //return <#initializer#>;
}

Natural &Natural::MUL_NN_N(const Natural &) const {
    //return <#initializer#>;
}

int Natural::DIV_NN_Dk(const Natural &, int) {
    return 0;
}

//Created by Grebennikov_Dmitry
//06.11.2023
 
Natural& Natural::DIV_NN_N(const Natural& natural) const {
    // Проверка делителя на равенство 0
    if (natural.NZER_N_B()) {
        // В данном случае возвращаем исходный объект без изменений
        return *this;
    }
 
    Natural quotient;  // Неполное частное
    Natural remainder = *this;  // Остаток
 
    while (COM_NN_D(remainder) != 1) {
        // Вычисляем первую цифру от деления (DIV_NN_Dk возвращает пару: частное и остаток)
        int firstDigit = DIV_NN_Dk(remainder, natural.get_Arr_by_index(natural.get_n() - 1));
 
        // Добавляем цифру к неполному частному
        quotient.ADD_NN_N(Natural(&firstDigit, 1));
 
        // Вычитаем из остатка умноженное на цифру делителя
        remainder.SUB_NDN_N(natural, firstDigit);
    }
 
    // quotient содержит неполное частное
    // remainder содержит остаток
 
    return quotient;
}

Natural &Natural::MOD_NN_N(const Natural &) const {
    //return <#initializer#>;
}

Natural &Natural::GCF_NN_N(const Natural &) const {
    //return <#initializer#>;
}

Natural &Natural::LCM_NN_N(const Natural &) const {
    //return <#initializer#>;
}

Natural::~Natural()
{
    if(this->Arr!=nullptr)
        free(this->Arr);

    this->Arr = nullptr;
}
