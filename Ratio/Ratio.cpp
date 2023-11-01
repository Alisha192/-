//
// Created by gidra on 01.11.23.
//

#include "Ratio.h"



Ratio::Ratio(NaturalNumbersWithNull &num, INTEGER &den): numerator(num), denominator(den) {

}

bool Ratio::INT_Q_B(Ratio &a) {
    return false;
}

Ratio Ratio::RED_Q_Q(NaturalNumbersWithNull &num, INTEGER &den) {
}

Ratio Ratio::TRANZ_Z_Q(INTEGER &a) {
}

INTEGER Ratio::TRANZ_Q_Z(Ratio &a) {
    return INTEGER(0, 0);
}

Ratio Ratio::ADD_QQ_Q(Ratio &a, Ratio &b) {
}

Ratio Ratio::SUB_QQ_Q(Ratio &a, Ratio &b) {
}

Ratio Ratio::MUL_QQ_Q(Ratio &a, Ratio &b) {
}

Ratio Ratio::DIV_QQ_Q(Ratio &a, Ratio &b) {
}


