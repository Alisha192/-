//
// Created by gidra on 01.11.23.
//

#include "INTEGER.h"

NaturalNumbersWithNull INTEGER::ABS_Z_Z(const INTEGER &a) {
    return NaturalNumbersWithNull(0);
}

digit INTEGER::POZ_Z_D(const INTEGER &a) {
    return 0;
}

NaturalNumbersWithNull INTEGER::MUL_ZM_Z(const INTEGER &a) {
    return NaturalNumbersWithNull(0);
}



NaturalNumbersWithNull INTEGER::TRANS_Z_N(const INTEGER &a) {
    return NaturalNumbersWithNull(0);
}



INTEGER::INTEGER(std::size_t number, digit sign) {

}

INTEGER INTEGER::TRANS_N_Z(const NaturalNumbersWithNull &a) {
    return INTEGER(0, 0);
}

INTEGER INTEGER::ADD_Z_Z(const INTEGER &a, const INTEGER &b) {
    return INTEGER(0, 0);
}

INTEGER INTEGER::SUB_Z_Z(const INTEGER &a, const INTEGER &b) {
    return INTEGER(0, 0);
}

INTEGER INTEGER::MUL_ZZ_Z(const INTEGER &a, const INTEGER &b) {
    return INTEGER(0, 0);
}

INTEGER INTEGER::DIV_ZZ_Z(const INTEGER &a, const INTEGER &b) {
    return INTEGER(0, 0);
}

INTEGER INTEGER::MOD_ZZ_Z(const INTEGER &a, const INTEGER &b) {
    return INTEGER(0, 0);
}

