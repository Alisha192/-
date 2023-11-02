//
// Created by gidra on 02.11.23.
//

#include "Integer.h"
Integer::Integer(const int *arr, const int n, const int s)
{
    //Поэлементно копируем параметры функции в члены класса
    this->sign = s;
    this->n = n;
    this->Arr = (int *)malloc(sizeof(int)*n);
    for(int i = 0;i<this->n;i++)
        this->Arr[i] = arr[i];
}
Integer::Integer()
{
    Integer("+0");
}

Integer::Integer(std::string number)
{
    //Гарантия корректности строки на вызывающей стороне
    this->sign = (number[0]=='+')?1:0;//Пулачаем знак из первого символа
    this->n = number.size()-1;//Вычисляем номер старшего разряда из длины строки
    this->Arr = (int*)malloc(sizeof(int)*n);
    //Записываем массив от младшего разряда к старшему для удобства
    for(int i = 0;i<this->n;i++)
        this->Arr[i] = number[(this->n)-i]-'0';
}

/*****************Конструктор копирования****************/
Integer::Integer(const Integer &other)
{
    //Почленно копируем элементы передаваемого объекта в наш
    if(this!=&other){
        this->sign = other.get_sign();
        this->n = other.get_n();
        this->Arr = (int*)malloc(sizeof(int)*this->n);
        const int *arr = other.get_Arr();
        for(int i = 0;i<n;i++)
            this->Arr[i] = arr[i];
    }
}


/*****Конструктор приведения натурального к целому*******/
Integer::Integer(const Natural &other)
{
    //Устанавливаем знак в состояние false, массив разрядов и номер старшего разряда просто копируем
    this->sign = 0;
    this->n = other.get_n();
    this->Arr = (int*)malloc(sizeof(int)*this->n);
    const int *arr = other.get_Arr();
    for(int i = 0;i<n;i++)
        this->Arr[i] = arr[i];

}


/************Перегрузка оператора присваивания***********/
Integer &Integer::operator=(const Integer &other)
{
    //Почленное копирование элементов правого числа в левое
    if(this!=&other){
        if(this->Arr!=nullptr){
            free(this->Arr);
            this->Arr = nullptr;
        }

        this->sign = other.get_sign();
        this->n = other.get_n();
        this->Arr = (int*)malloc(sizeof(int)*this->n);
        const int *arr = other.get_Arr();
        for(int i = 0;i<n;i++)
            this->Arr[i] = arr[i];
    }
    return *this;
}

Natural &Integer::ABS_Z_Z() const {
    //return <#initializer#>;
}

int Integer::POZ_Z_D() {
    return 0;
}

Integer &Integer::MUL_ZM_Z() const {
    //return <#initializer#>;
}

Natural &Integer::TRANS_Z_N() const {
    //return <#initializer#>;
}

Integer &Integer::ADD_ZZ_Z(const Integer &) const {
    //return <#initializer#>;
}

Integer &Integer::SUB_ZZ_Z(const Integer &) const {
    //return <#initializer#>;
}

Integer &Integer::MUL_ZZ_Z(const Integer &) const {
    //return <#initializer#>;
}

Integer &Integer::DIV_ZZ_Z(const Natural &) const {
    //return <#initializer#>;
}

Integer &Integer::MOD_ZZ_Z(const Natural &) const {
    //return <#initializer#>;
}
Integer::~Integer()
{
    if(this->Arr!=nullptr)
        free(this->Arr);

    this->Arr = nullptr;
}
