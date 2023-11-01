//
// Created by gidra on 01.11.23.
//

#ifndef UNTITLED15_RATIO_H
#define UNTITLED15_RATIO_H
#include "INTEGER.h"
#include "NaturalNumbersWithNull.h"

class Ratio {
    NaturalNumbersWithNull& numerator;
    INTEGER& denominator;
public:
    explicit Ratio(NaturalNumbersWithNull& num, INTEGER& den); // ДОПИСАТЬ КОНСТРУКТОР КАК ВАМ УДОБНО!!!!!
    static Ratio RED_Q_Q(NaturalNumbersWithNull& num, INTEGER& den);
    static bool INT_Q_B(Ratio& a);
    Ratio TRANZ_Z_Q(INTEGER& a);
    static INTEGER TRANZ_Q_Z(Ratio& a);
    static Ratio ADD_QQ_Q(Ratio& a, Ratio& b);
    static Ratio SUB_QQ_Q(Ratio& a, Ratio& b);
    static Ratio MUL_QQ_Q(Ratio& a, Ratio& b);
    static Ratio DIV_QQ_Q(Ratio& a, Ratio& b);
};



#endif //UNTITLED15_RATIO_H
