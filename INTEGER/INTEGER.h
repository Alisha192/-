//
// Created by gidra on 01.11.23.
//

#ifndef UNTITLED15_INTEGER_H
#define UNTITLED15_INTEGER_H
#include "vector"
#include "cstdint"
#include "string"
#include "NaturalNumbersWithNull.h"
using digit = uint8_t;
class INTEGER {
    digit sign;
    std::vector<digit> digits_; // цифры идут в обратном порядке 123 = [3 2 1]
    std::size_t n_; // номер старшей позиции
public:
    explicit INTEGER(std::size_t number, digit sign);    // ДОПИСАТЬ КОНСТРУКТОР КАК ВАМ УДОБНО!!!!!
    static NaturalNumbersWithNull ABS_Z_Z(const INTEGER& a);
    static digit POZ_Z_D(const INTEGER& a);
    static NaturalNumbersWithNull MUL_ZM_Z(const INTEGER& a);
    static INTEGER TRANS_N_Z(const NaturalNumbersWithNull& a);
    static NaturalNumbersWithNull TRANS_Z_N(const INTEGER& a);
    static INTEGER ADD_Z_Z(const INTEGER& a, const INTEGER& b);
    static INTEGER SUB_Z_Z(const INTEGER& a, const INTEGER& b);
    static INTEGER MUL_ZZ_Z(const INTEGER& a, const INTEGER& b);
    static INTEGER DIV_ZZ_Z(const INTEGER& a, const INTEGER& b);
    static INTEGER MOD_ZZ_Z(const INTEGER& a, const INTEGER& b);
};


#endif //UNTITLED15_INTEGER_H
