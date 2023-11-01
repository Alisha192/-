//
// Created by gidra on 01.11.23.
//

#ifndef UNTITLED15_NATURALNUMBERSWITHNULL_H
#define UNTITLED15_NATURALNUMBERSWITHNULL_H
#include "vector"
#include "string"
#include "cstdint"
using digit = uint8_t;
class NaturalNumbersWithNull {
    std::vector<digit> digits_; // цифры идут в обратном порядке 123 = [3 2 1]
    std::size_t n_; // номер старшей позиции
public:
    explicit NaturalNumbersWithNull(std::size_t number);
    static digit COM_NN_D(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    bool NZER_N_B() const;
    static NaturalNumbersWithNull ADD_1N_N();
    static NaturalNumbersWithNull ADD_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull SUB_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull MUL_ND_D(const NaturalNumbersWithNull& a, const digit& number);
    static NaturalNumbersWithNull MUL_NK_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& k);
    static NaturalNumbersWithNull MUL_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull SUB_NDN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b, digit& number );
    static digit DIV_NN_Dk(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b, digit number);
    static NaturalNumbersWithNull DIV_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull MOD_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull GCF_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
    static NaturalNumbersWithNull LCM_NN_N(const NaturalNumbersWithNull& a, const NaturalNumbersWithNull& b);
};




#endif //UNTITLED15_NATURALNUMBERSWITHNULL_H

