//
// Created by gidra on 02.11.23.
//

#include <iostream>
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

//Created by Ismailov_Maksim
//06.11.2023

int Natural::COM_NN_D(const Natural & other) {
    int num_1_len = this->n; //Берем номер старшего разряда 1-го числа
    int num_2_len = other.get_n(); //Берем номер старшего разряда 2-го числа
    if (num_1_len > num_2_len){ 
        return 2; //Если номер старшего разряда 1-го числа > номера старшего разряда 2-го числа
    } else if ( num_1_len < num_2_len) {
        return 1; //Если номер старшего разряда 1-го числа < номера старшего разряда 2-го числа
    } else { //Если номера старших разрядов одинаковые:
        int* num_1 = this->get_Arr();  //Берем массив циифр 1-го числа
        int* num_2 = other.get_Arr(); //Берем массив цифр 2-го числа
        for(int i = num_1_len - 1; i >= 0; i--){  //Двигаемся со старшего разряда до конца числа
            if(num_1[i]>num_2[i]){ 
                return 2; 
            }
            else if(num_1[i]<num_2[i]){
                return 1;
            }
        }
        return 0;
    }
    
}

//Created by Ismailov_Maksim
//06.11.2023

bool Natural::NZER_N_B() { //Проверяем если число нуль:
    if (this->n == 1 && this->Arr[0] == 0){ 
        return false;
    }
    return true;
}

//Created by Ismailov_Maksim
//06.11.2023

Natural &Natural::ADD_1N_N() { //Добавляем 1 к числу:
    int i = 0;
    while (this->Arr[i] == 9) //Двигаемся с начала массива до последнего разряда: 
    {                         //Если i-я цифра числа = 9 то заходим в цикл: 
        this->Arr[i] = 0;   //i-ый элемент массива становится нулем.
        if (i == this->n - 1){ //если дошли до старшего разряда и он равен 9
            this->n += 1;      //добавляем еще 1 разряд, а предыдущий становится нулем.
            this->Arr = (int*)realloc(this->Arr, sizeof(int)*(this->n));
            this->Arr[this->n-1] = 1;
            return *this;
        }
        i++; //шаг итератора
    }
    this->Arr[i]++; //добавляем 1 к следующему элементу
    return *this;
}

//Created by Ismailov_Maksim
//06.11.2023

Natural& Natural::ADD_NN_N(const Natural& other) {
    int n, i;
    int diff = 0;
    Natural tmpObj("0"); //Создаем пустой объект Natural
    int max = 0; //Переменная max, которая в следующих двух строчках, получается свое значение.
    if (this->get_n() > other.get_n()) max = this->get_n(); 
    else max = other.get_n();
    for (i = 0; i < max; i++) { //Двигаемся до старшего разряда с шагом 1
        tmpObj.set_Arr_by_index(i, (this->get_Arr_by_index(i) + other.get_Arr_by_index(i) + diff) % 10);
        diff = (this->get_Arr_by_index(i) + other.get_Arr_by_index(i) + diff) / 10;
    }
    if (diff > 0) tmpObj.set_Arr_by_index(i + 1, diff);
    *this = tmpObj;
    return *this;
}

//Created by Berezin_Dmitry
//06.11.2023

Natural& Natural::SUB_NDN_N(const Natural& other, int digit) {
    // Создадим копию второго числа
    Natural product(other);

    // Умножим копию второго числа на данную цифру
    product.MUL_ND_N(digit);

    // Выполним вычитание из первого числа умноженного второго числа
    SUB_NN_N(product);

    return *this;
}

//Created by Berezin_Dmitry
//13.11.2023

Natural &Natural::SUB_NN_N(const Natural &other) {
    int comparison = COM_NN_D(other);
    int n = this->get_n();
    int m = other.get_n();
    if (comparison == 2){
      // Создадим временный объект, который будет хранить результат
      Natural result(*this);

      int borrow = 0;

      // Убедимся, что this имеет достаточное количество разрядов для хранения разности
      if (n < m) {
          n = m;
          result.Arr = (int*)realloc(result.Arr, sizeof(int) * n);
      }

      for (int i = 0; i < n; i++) {
          int diff = result.get_Arr_by_index(i) - borrow;

          if (i < m) {
              diff -= other.get_Arr_by_index(i);
          }

          if (diff < 0) {
              diff += 10;  // В случае отрицательного результата, добавляем 10
              borrow = 1;
          } else {
              borrow = 0; // В противном случае заем равен 0
          }

          result.set_Arr_by_index(i, diff);
      }

      // Удаляем ведущие нули из результата
      while (n > 1 && result.get_Arr_by_index(n - 1) == 0) {
          n--;
      }

      result.n = n;
      result.Arr = (int*)realloc(result.Arr, sizeof(int) * n);

      // Копируем результат в текущий объект
      *this = result;
    }

    else if(comparison == 0){
      this->n = 1;
      this->Arr[0] = 0;
    }

    return *this;
}

//Created by Ismailov_Maksim
//06.11.2023

Natural &Natural::MUL_ND_N(const int num) { //БЫЛИ ОШИБКИ В РАЗНЫХ КОМПИЛЯТОРАХ РАЗНЫЕ ОТВЕТЫ
    int diff = 0; 
    int i, n;
    n = this->n;
    Natural tmpObj ("0");
    for(i = 0; i < n; i++){
        tmpObj.set_Arr_by_index(i + 1, ( ( (this->get_Arr_by_index(i) * num  ) + diff ) % 10));
        diff = ( (this->get_Arr_by_index(i) * num )+ diff) / 10;
    }
    if (diff > 0) { tmpObj.set_Arr_by_index(i, diff); }
    *this = tmpObj;
    return *this;
}

//Created by Ismailov_Maksim
//06.11.2023

Natural &Natural::MUL_Nk_N(const int k){ //НЕ ТЕСТИЛ ВРОДЕ ВЕРНО
    int n = this->get_n();
    int i;
    Natural tmpObj("0");

    if (!this->NZER_N_B()){
        *this = tmpObj;
        return *this;
    }

    for (int i = 0; i < k; i++){
        tmpObj.set_Arr_by_index(i + 1, 0);
    }
    for (int i = k; i < n + k; i++){
        tmpObj.set_Arr_by_index(i + 1, this->get_Arr_by_index(i - k));
    }

    *this = tmpObj;
    return *this;

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

//Created by Grebennikov_Dmitry
//06.11.2023

Natural& Natural::MOD_NN_N(const Natural& natural) const {
    // Проверка делителя на равенство 0
    if (natural.NZER_N_B()) {
        // Можно выбрать другую стратегию обработки ошибок в зависимости от требований
        // В данном случае возвращаем исходный объект без изменений
        return *this;
    }

    // Вычисляем частное от деления
    Natural quotient = this->DIV_NN_N(natural);

    // Вычитаем из исходного числа произведение делителя на частное
    Natural product = natural;
    product.MUL_NN_N(quotient);
    
    // Остаток от деления
    this->SUB_NDN_N(product, 0);

    return *this;
}

Natural &Natural::GCF_NN_N(const Natural &) const {
    //return <#initializer#>;
}

Natural &Natural::LCM_NN_N(const Natural &) const {
    //return <#initializer#>;
}

//Created by Ismailov_Maksim
//06.11.2023

int Natural::get_Arr_by_index(int index) const {
    if (index < this->n) return this->Arr[index];
    else return 0;
}

//Created by Ismailov_Maksim
//06.11.2023

void Natural::set_Arr_by_index(int index, int value) {
    if (index < this->n) this->Arr[index] = value;
    else {
        int n = this->n;
        this->n = index;
        this->Arr = (int*)realloc(this->Arr, sizeof(int)*this->n);
        for (int i = n; i < this->n; i++){
            this->Arr[i] = 0;
        }
        this->Arr[index - 1] = value;
    }
}


Natural::~Natural()
{
    if(this->Arr!=nullptr)
        free(this->Arr);

    this->Arr = nullptr;
}
