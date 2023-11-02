//
// Created by gidra on 02.11.23.
//

#include "Polinom.h"
Polinom::Polinom(std::map<Natural,Rational,Comparator> &C_other)
{
    //Проходимся по коэффициентам и записываем все ненулевые коэффициенты
    for(auto it = C_other.begin();it!=C_other.end();it++)
        if(it->second.get_NUM()->POZ_Z_D()!=0)
            this->C[it->first] = it->second;

    //Если мы не записали в итоге ни одного коэффициента
    //то запишем туда 0
    if(this->C.empty())
        this->C[Natural("0")] = Rational();

    this->hDegree = new Natural((this->C.begin())->first);

}


/*****************Конструктор копирования**************************/
Polinom::Polinom(const Polinom &other)
{
    if(this!=&other){
        //Очищаем коэффициенты
        this->C.clear();
        std::map<Natural,Rational,Comparator> temp = other.get_C();
        //Записываем все ненулевые коэффициенты
        for(auto it = temp.begin();it!=temp.end();it++)
            if(it->second.get_NUM()->POZ_Z_D()!=0)
                this->C[it->first] = it->second;

        //Если ничего не записали - запишем 0
        if(this->C.empty())
            this->C[Natural("0")] = Rational();

        this->hDegree = new Natural((this->C.begin())->first);
    }
}


/*************Перегрузка оператора присваивани***************************/
Polinom &Polinom::operator =(const Polinom &other)
{
    //Аналогично конструктору копирования
    if(this!=&other){
        this->C.clear();
        std::map<Natural,Rational,Comparator> temp = other.get_C();
        for(auto it = temp.begin();it!=temp.end();it++)
            if(it->second.get_NUM()->POZ_Z_D()!=0)
                this->C[it->first] = it->second;

        if(this->C.empty())
            this->C[Natural("0")] = Rational();

        this->hDegree = new Natural((this->C.begin())->first);


    }

    return *this;
}


Polinom::~Polinom()
{
    delete hDegree;
}

Polinom &Polinom::ADD_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::SUB_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::MUL_PQ_P(const Rational &) const {
    //return <#initializer#>;
}

Polinom &Polinom::MUL_Pxk_P(const Natural &) const {
    //return <#initializer#>;
}

Rational &Polinom::LED_P_Q() const {
    //return <#initializer#>;
}

Natural &Polinom::DEG_P_N() const {
    //return <#initializer#>;
}

Rational &Polinom::FAC_P_Q() const {
    //return <#initializer#>;
}

Polinom &Polinom::MUL_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::DIV_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::MOD_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::GCF_PP_P(const Polinom &) const {
    //return <#initializer#>;
}

Polinom &Polinom::DER_P_P() const {
    //return <#initializer#>;
}

Polinom &Polinom::NMR_P_P() const {
    //return <#initializer#>;
}
