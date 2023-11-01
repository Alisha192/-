//
// Created by gidra on 01.11.23.
//

#include "NaturalNumbersWithNull.h"

NaturalNumbersWithNull::NaturalNumbersWithNull(std::size_t number) {

}

digit NaturalNumbersWithNull::COM_NN_D(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return 0;
}

bool NaturalNumbersWithNull::NZER_N_B() const {
    return true;
}

NaturalNumbersWithNull NaturalNumbersWithNull::ADD_1N_N() {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::ADD_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::MUL_ND_D(const NaturalNumbersWithNull &a, const digit &number) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::SUB_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::MUL_NK_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &k) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::MUL_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::SUB_NDN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b, digit& number) {
    return NaturalNumbersWithNull(0);
}

digit NaturalNumbersWithNull::DIV_NN_Dk(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b, digit number) {
    return 0;
}

NaturalNumbersWithNull NaturalNumbersWithNull::DIV_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::MOD_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::GCF_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}

NaturalNumbersWithNull NaturalNumbersWithNull::LCM_NN_N(const NaturalNumbersWithNull &a, const NaturalNumbersWithNull &b) {
    return NaturalNumbersWithNull(0);
}






