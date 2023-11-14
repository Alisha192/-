import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Коллоквиум ДМиТИ")
        self.setFixedSize(QSize(300, 220))
        self.setStyleSheet('background-color: #FDBBE7;')
        self.degree_of_polinom = 0
        self.polinom = Polinom(0)
        self.Menu()

    def Menu(self):
        self.name = QLabel("Калькулятор различных типов данных", self)
        self.name.resize(240, 30)
        self.name.move(40, 10)
        self.font = self.name.font()
        self.font.setBold(True)
        self.name.setFont(self.font)
        self.nat_num_but = QPushButton("Натуральные числа", self)
        self.nat_num_but.resize(240, 30)
        self.nat_num_but.move(30, 50)
        self.nat_num_but.clicked.connect(self.nature_block)
        self.int_num_but = QPushButton("Целые числа", self)
        self.int_num_but.resize(240, 30)
        self.int_num_but.move(30, 90)
        self.int_num_but.clicked.connect(self.integer_block)
        self.rat_num_but = QPushButton("Рациональные числа", self)
        self.rat_num_but.resize(240, 30)
        self.rat_num_but.move(30, 130)
        self.rat_num_but.clicked.connect(self.ration_block)
        self.polinom_but = QPushButton("Многочлены", self)
        self.polinom_but.resize(240, 30)
        self.polinom_but.move(30, 170)
        self.polinom_but.clicked.connect(self.polinom_block)

    def nature_block(self):
        self.natural = Natural_numbers()
        self.natural.show()

    def integer_block(self):
        self.integer = Integer_numbers()
        self.integer.show()

    def ration_block(self):
        self.ration = Ration_numbers()
        self.ration.show()

    def polinom_block(self):
        self.degree_of_polinom, ok = QInputDialog.getText(self, "Ввод многочлена", "Введите степень многочлена")
        if not (self.degree_of_polinom.isdigit()):
            self.degree_of_polinom = 0
        if ok:
            self.degree_of_polinom = int(self.degree_of_polinom)
            self.polinom.change_size(self.degree_of_polinom)
        else:
            return
        self.input_for_polinoms = Input_polinom(self.polinom, self.degree_of_polinom)
        self.input_for_polinoms.show()
        self.input_for_polinoms.exec()
        self.polinom_window = Polinoms(self.polinom)
        self.polinom_window.show()


class Natural_numbers(QWidget):
    def __init__(self):
        super(Natural_numbers, self).__init__()
        self.setWindowTitle("Natural numbers")
        self.setFixedSize(QSize(800, 400))
        self.setStyleSheet('background-color: #B4DAF6;')
        self.labels = ['Сравнение натуральных чисел', 'Проверка на ноль', 'Добавление единицы', 'Сложение двух чисел',
                  'Вычитание двух чисел', 'Умножение на цифру', 'Умножение на 10^k', 'Умножение',
                  'Вычитание с умножением на цифру', 'Вычисление первой цифры', 'Неполное частное',
                  'Остаток от деления', 'НОД', 'НОК']
        self.label = QLabel(self.labels[0])
        self.font = self.label.font()
        self.font.setBold(True)
        self.label.setFont(self.font)
        self.operations_with_natural_num = QListWidget()
        self.operations_with_natural_num.insertItem(0, 'Сравнение натуральных чисел')
        self.operations_with_natural_num.insertItem(1, 'Проверка на ноль')
        self.operations_with_natural_num.insertItem(2, 'Добавление единицы')
        self.operations_with_natural_num.insertItem(3, 'Сложение двух чисел')
        self.operations_with_natural_num.insertItem(4, 'Вычитание двух чисел')
        self.operations_with_natural_num.insertItem(5, 'Умножение на цифру')
        self.operations_with_natural_num.insertItem(6, 'Умножение на 10^k')
        self.operations_with_natural_num.insertItem(7, 'Умножение')
        self.operations_with_natural_num.insertItem(8, 'Вычитание с умножением на цифру')
        self.operations_with_natural_num.insertItem(9, 'Вычисление первой цифры')
        self.operations_with_natural_num.insertItem(10, 'Неполное частное')
        self.operations_with_natural_num.insertItem(11, 'Остаток от деления')
        self.operations_with_natural_num.insertItem(12, 'НОД')
        self.operations_with_natural_num.insertItem(13, 'НОК')

        self.comparing_num = QWidget()
        self.check_zero = QWidget()
        self.add_1 = QWidget()
        self.addition = QWidget()
        self.subtraction = QWidget()
        self.multiplication_by_digit = QWidget()
        self.multiplication_by_ten = QWidget()
        self.multiplication = QWidget()
        self.subtraction_with_multiplication = QWidget()
        self.first_digit = QWidget()
        self.incomplete_quotient = QWidget()
        self.remainder_of_division = QWidget()
        self.NOD = QWidget()
        self.NOK = QWidget()

        self.comparing_num_ui()
        self.check_zero_ui()
        self.add_1_ui()
        self.addition_ui()
        self.subtraction_ui()
        self.multiplication_by_digit_ui()
        self.multiplication_by_ten_ui()
        self.multiplication_ui()
        self.subtraction_with_multiplication_ui()
        self.first_digit_ui()
        self.incomplete_quotient_ui()
        self.remainder_of_division_ui()
        self.NOD_ui()
        self.NOK_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.comparing_num)
        self.Stack.addWidget(self.check_zero)
        self.Stack.addWidget(self.add_1)
        self.Stack.addWidget(self.addition)
        self.Stack.addWidget(self.subtraction)
        self.Stack.addWidget(self.multiplication_by_digit)
        self.Stack.addWidget(self.multiplication_by_ten)
        self.Stack.addWidget(self.multiplication)
        self.Stack.addWidget(self.subtraction_with_multiplication)
        self.Stack.addWidget(self.first_digit)
        self.Stack.addWidget(self.incomplete_quotient)
        self.Stack.addWidget(self.remainder_of_division)
        self.Stack.addWidget(self.NOD)
        self.Stack.addWidget(self.NOK)

        hbox = QGridLayout(self)
        hbox.addWidget(self.label, 0, 0)
        hbox.addWidget(self.operations_with_natural_num, 1, 0)
        hbox.addWidget(self.Stack, 1, 1)

        self.setLayout(hbox)
        self.operations_with_natural_num.currentRowChanged.connect(self.display)
        self.res_0.clicked.connect(self.comparing_num_res)
        self.res_1.clicked.connect(self.check_zero_res)
        self.res_2.clicked.connect(self.add_1_res)
        self.res_3.clicked.connect(self.addition_res)
        self.res_4.clicked.connect(self.subtraction_res)
        self.res_5.clicked.connect(self.multiplication_by_digit_res)
        self.res_6.clicked.connect(self.multiplication_by_ten_res)
        self.res_7.clicked.connect(self.multiplication_res)
        self.res_8.clicked.connect(self.subtraction_with_multiplication_res)
        self.res_9.clicked.connect(self.first_digit_res)
        self.res_10.clicked.connect(self.incomplete_quotient_res)
        self.res_11.clicked.connect(self.remainder_of_division_res)
        self.res_12.clicked.connect(self.NOD_res)
        self.res_13.clicked.connect(self.NOK_res)

    def comparing_num_res(self):
        answer = 'Answer'
        if self.num1_0.text() == '' or self.num2_0.text() == '':
            self.answer_0.setText('Введите все значения')
            return
        if not(self.num1_0.text().isdigit()) or not(self.num2_0.text().isdigit()):
            self.answer_0.setText('Введите корректные значения')
            return
        self.answer_0.setText(answer)

    def check_zero_res(self):
        answer = 'Answer'
        if self.num1_1.text() == '':
            self.answer_1.setText('Введите значение')
            return
        if not(self.num1_1.text().isdigit()):
            self.answer_1.setText('Введите корректное значение')
            return
        self.answer_1.setText(answer)

    def add_1_res(self):
        answer = 'Answer'
        if self.num1_2.text() == '':
            self.answer_2.setText('Введите значение')
            return
        if not(self.num1_2.text().isdigit()):
            self.answer_2.setText('Введите корректное значение')
            return
        self.answer_2.setText(answer)

    def addition_res(self):
        answer = 'Answer'
        if self.num1_3.text() == '' or self.num2_3.text() == '':
            self.answer_3.setText('Введите все значения')
            return
        if not(self.num1_3.text().isdigit()) or not(self.num2_3.text().isdigit()):
            self.answer_3.setText('Введите корректные значения')
            return
        self.answer_3.setText(answer)

    def subtraction_res(self):
        answer = 'Answer'
        if self.num1_4.text() == '' or self.num2_4.text() == '':
            self.answer_4.setText('Введите все значения')
            return
        if not(self.num1_4.text().isdigit()) or not(self.num2_4.text().isdigit()):
            self.answer_4.setText('Введите корректные значения')
            return
        self.answer_4.setText(answer)

    def multiplication_by_digit_res(self):
        answer = 'Answer'
        if self.num1_5.text() == '':
            self.answer_5.setText('Введите значение')
            return
        if not (self.num1_5.text().isdigit()):
            self.answer_5.setText('Введите корректные значения')
            return
        # получить значение spinbox - .value() - int
        self.answer_5.setText(answer)

    def multiplication_by_ten_res(self):
        answer = 'Answer'
        if self.num1_6.text() == '' or self.num2_6.text() == '':
            self.answer_6.setText('Введите все значения')
            return
        if not (self.num1_6.text().isdigit()) or not (self.num2_6.text().isdigit()):
            self.answer_6.setText('Введите корректные значения')
            return
        self.answer_6.setText(answer)

    def multiplication_res(self):
        answer = 'Answer'
        if self.num1_7.text() == '' or self.num2_7.text() == '':
            self.answer_7.setText('Введите все значения')
            return
        if not (self.num1_7.text().isdigit()) or not (self.num2_7.text().isdigit()):
            self.answer_7.setText('Введите корректные значения')
            return
        self.answer_7.setText(answer)

    def subtraction_with_multiplication_res(self):
        answer = 'Answer'
        if self.num1_8.text() == '' or self.num2_8.text() == '':
            self.answer_8.setText('Введите все значения')
            return
        if not (self.num1_8.text().isdigit()) or not (self.num2_8.text().isdigit()):
            self.answer_8.setText('Введите корректные значения')
            return
        self.answer_8.setText(answer)

    def first_digit_res(self):
        answer = 'Answer'
        if self.num1_9.text() == '' or self.num2_9.text() == '':
            self.answer_9.setText('Введите все значения')
            return
        if (not(self.num1_9.text().isdigit()) or not (self.num2_9.text().isdigit())):
            self.answer_9.setText('Введите корректные значения')
            return
        if self.num2_9.text().isdigit() and (int(self.num2_9.text()) < 0 or\
                                             int(self.num2_9.text()) >= len(self.num1_9.text())):
            self.answer_9.setText('Введите корректное значение позиции цифры')
            return
        self.answer_9.setText(answer)

    def incomplete_quotient_res(self):
        answer = 'Answer'
        if self.num1_10.text() == '' or self.num2_10.text() == '':
            self.answer_10.setText('Введите все значения')
            return
        if not (self.num1_10.text().isdigit()) or not (self.num2_10.text().isdigit()):
            self.answer_10.setText('Введите корректные значения')
            return
        self.answer_10.setText(answer)

    def remainder_of_division_res(self):
        answer = 'Answer'
        if self.num1_11.text() == '' or self.num2_11.text() == '':
            self.answer_11.setText('Введите все значения')
            return
        if not (self.num1_11.text().isdigit()) or not (self.num2_11.text().isdigit()):
            self.answer_11.setText('Введите корректные значения')
            return
        self.answer_11.setText(answer)

    def NOD_res(self):
        answer = 'Answer'
        if self.num1_12.text() == '' or self.num2_12.text() == '':
            self.answer_12.setText('Введите все значения')
            return
        if not (self.num1_12.text().isdigit()) or not (self.num2_12.text().isdigit()):
            self.answer_12.setText('Введите корректные значения')
            return
        self.answer_12.setText(answer)

    def NOK_res(self):
        answer = 'Answer'
        if self.num1_13.text() == '' or self.num2_13.text() == '':
            self.answer_13.setText('Введите все значения')
            return
        if not (self.num1_13.text().isdigit()) or not (self.num2_13.text().isdigit()):
            self.answer_13.setText('Введите корректные значения')
            return
        self.answer_13.setText(answer)

    def comparing_num_ui(self):
        layout = QFormLayout()
        self.num1_0 = QLineEdit()
        self.num2_0 = QLineEdit()
        self.res_0 = QPushButton("Получить ответ", self)
        self.answer_0 = QLineEdit()
        self.answer_0.setReadOnly(True)
        layout.addRow("Первое число", self.num1_0)
        layout.addRow("Второе число", self.num2_0)
        layout.addRow(self.res_0)
        layout.addRow("Ответ", self.answer_0)
        self.comparing_num.setLayout(layout)

    def check_zero_ui(self):
        layout = QFormLayout()
        self.num1_1 = QLineEdit()
        self.res_1 = QPushButton("Получить ответ", self)
        self.answer_1 = QLineEdit()
        self.answer_1.setReadOnly(True)
        layout.addRow("Число", self.num1_1)
        layout.addRow(self.res_1)
        layout.addRow("Ответ", self.answer_1)
        self.check_zero.setLayout(layout)

    def add_1_ui(self):
        layout = QFormLayout()
        self.num1_2 = QLineEdit()
        self.res_2 = QPushButton("Получить ответ", self)
        self.answer_2 = QLineEdit()
        self.answer_2.setReadOnly(True)
        layout.addRow("Число", self.num1_2)
        layout.addRow(self.res_2)
        layout.addRow("Ответ", self.answer_2)
        self.add_1.setLayout(layout)

    def addition_ui(self):
        layout = QFormLayout()
        self.num1_3 = QLineEdit()
        self.num2_3 = QLineEdit()
        self.res_3 = QPushButton("Получить ответ", self)
        self.answer_3 = QLineEdit()
        self.answer_3.setReadOnly(True)
        layout.addRow("Первое число", self.num1_3)
        layout.addRow("Второе число", self.num2_3)
        layout.addRow(self.res_3)
        layout.addRow("Ответ", self.answer_3)
        self.addition.setLayout(layout)

    def subtraction_ui(self):
        layout = QFormLayout()
        self.num1_4 = QLineEdit()
        self.num2_4 = QLineEdit()
        self.res_4 = QPushButton("Получить ответ", self)
        self.answer_4 = QLineEdit()
        self.answer_4.setReadOnly(True)
        layout.addRow("Первое число", self.num1_4)
        layout.addRow("Второе число", self.num2_4)
        layout.addRow(self.res_4)
        layout.addRow("Ответ", self.answer_4)
        self.subtraction.setLayout(layout)

    def multiplication_by_digit_ui(self):
        layout = QFormLayout()
        self.num1_5 = QLineEdit()
        self.digit_spinbox_5 = QSpinBox()
        self.digit_spinbox_5.setRange(0, 9)
        self.digit_spinbox_5.setSingleStep(1)
        self.res_5 = QPushButton("Получить ответ", self)
        self.answer_5 = QLineEdit()
        self.answer_5.setReadOnly(True)
        layout.addRow("Число", self.num1_5)
        layout.addRow("Цифра", self.digit_spinbox_5)
        layout.addRow(self.res_5)
        layout.addRow("Ответ", self.answer_5)
        self.multiplication_by_digit.setLayout(layout)

    def multiplication_by_ten_ui(self):
        layout = QFormLayout()
        self.num1_6 = QLineEdit()
        self.num2_6 = QLineEdit()
        self.res_6 = QPushButton("Получить ответ", self)
        self.answer_6 = QLineEdit()
        self.answer_6.setReadOnly(True)
        layout.addRow("Первое число", self.num1_6)
        layout.addRow("Степень 10", self.num2_6)
        layout.addRow(self.res_6)
        layout.addRow("Ответ", self.answer_6)
        self.multiplication_by_ten.setLayout(layout)

    def multiplication_ui(self):
        layout = QFormLayout()
        self.num1_7 = QLineEdit()
        self.num2_7 = QLineEdit()
        self.res_7 = QPushButton("Получить ответ", self)
        self.answer_7 = QLineEdit()
        self.answer_7.setReadOnly(True)
        layout.addRow("Первое число", self.num1_7)
        layout.addRow("Второе число", self.num2_7)
        layout.addRow(self.res_7)
        layout.addRow("Ответ", self.answer_7)
        self.multiplication.setLayout(layout)

    def subtraction_with_multiplication_ui(self):
        layout = QFormLayout()
        self.num1_8 = QLineEdit()
        self.num2_8 = QLineEdit()
        self.digit_spinbox_8 = QSpinBox()
        self.digit_spinbox_8.setRange(0, 9)
        self.digit_spinbox_8.setSingleStep(1)
        self.res_8 = QPushButton("Получить ответ", self)
        self.answer_8 = QLineEdit()
        self.answer_8.setReadOnly(True)
        layout.addRow("Первое число", self.num1_8)
        layout.addRow("Второе число", self.num2_8)
        layout.addRow("Цифра", self.digit_spinbox_8)
        layout.addRow(self.res_8)
        layout.addRow("Ответ", self.answer_8)
        self.subtraction_with_multiplication.setLayout(layout)

    def first_digit_ui(self):
        layout = QFormLayout()
        self.num1_9 = QLineEdit()
        self.num2_9 = QLineEdit()
        self.res_9 = QPushButton("Получить ответ", self)
        self.answer_9 = QLineEdit()
        self.answer_9.setReadOnly(True)
        layout.addRow("Число", self.num1_9)
        layout.addRow("Номер позиции", self.num2_9)
        layout.addRow(self.res_9)
        layout.addRow("Ответ", self.answer_9)
        self.first_digit.setLayout(layout)

    def incomplete_quotient_ui(self):
        layout = QFormLayout()
        self.num1_10 = QLineEdit()
        self.num2_10 = QLineEdit()
        self.res_10 = QPushButton("Получить ответ", self)
        self.answer_10 = QLineEdit()
        self.answer_10.setReadOnly(True)
        layout.addRow("Первое число", self.num1_10)
        layout.addRow("Второе число", self.num2_10)
        layout.addRow(self.res_10)
        layout.addRow("Ответ", self.answer_10)
        self.incomplete_quotient.setLayout(layout)

    def remainder_of_division_ui(self):
        layout = QFormLayout()
        self.num1_11 = QLineEdit()
        self.num2_11 = QLineEdit()
        self.res_11 = QPushButton("Получить ответ", self)
        self.answer_11 = QLineEdit()
        self.answer_11.setReadOnly(True)
        layout.addRow("Первое число", self.num1_11)
        layout.addRow("Второе число", self.num2_11)
        layout.addRow(self.res_11)
        layout.addRow("Ответ", self.answer_11)
        self.remainder_of_division.setLayout(layout)

    def NOD_ui(self):
        layout = QFormLayout()
        self.num1_12 = QLineEdit()
        self.num2_12 = QLineEdit()
        self.res_12 = QPushButton("Получить ответ", self)
        self.answer_12 = QLineEdit()
        self.answer_12.setReadOnly(True)
        layout.addRow("Первое число", self.num1_12)
        layout.addRow("Второе число", self.num2_12)
        layout.addRow(self.res_12)
        layout.addRow("Ответ", self.answer_12)
        self.NOD.setLayout(layout)

    def NOK_ui(self):
        layout = QFormLayout()
        self.num1_13 = QLineEdit()
        self.num2_13 = QLineEdit()
        self.res_13 = QPushButton("Получить ответ", self)
        self.answer_13 = QLineEdit()
        self.answer_13.setReadOnly(True)
        layout.addRow("Первое число", self.num1_13)
        layout.addRow("Второе число", self.num2_13)
        layout.addRow(self.res_13)
        layout.addRow("Ответ", self.answer_13)
        self.NOK.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        self.label.setText(self.labels[self.Stack.currentIndex()])


class Integer_numbers(QWidget):
    def __init__(self):
        super(Integer_numbers, self).__init__()
        self.setWindowTitle("Integer numbers")
        self.setFixedSize(QSize(800, 400))
        self.setStyleSheet('background-color: #FFFF99;')
        self.operations_with_integer_num = QListWidget()
        self.operations_with_integer_num.insertItem(0, 'Абсолютная величина числа')
        self.operations_with_integer_num.insertItem(1, 'Число относительно нуля')
        self.operations_with_integer_num.insertItem(2, 'Умножение на -1')
        self.operations_with_integer_num.insertItem(3, 'Преобразование из натурального в целое')
        self.operations_with_integer_num.insertItem(4, 'Преобразование из целого в натуральное')
        self.operations_with_integer_num.insertItem(5, 'Сложение двух чисел')
        self.operations_with_integer_num.insertItem(6, 'Вычитание двух чисел')
        self.operations_with_integer_num.insertItem(7, 'Умножение')
        self.operations_with_integer_num.insertItem(8, 'Частное от деления')
        self.operations_with_integer_num.insertItem(9, 'Остаток от деления')
        self.labels = ['Абсолютная величина числа', 'Число относительно нуля', 'Умножение на -1',
                       'Преобразование из натурального в целое', 'Преобразование из целого в натуральное',
                       'Сложение двух чисел', 'Вычитание двух чисел','Умножение', 'Частное от деления', 'Остаток от деления']
        self.label = QLabel(self.labels[0])
        self.font = self.label.font()
        self.font.setBold(True)
        self.label.setFont(self.font)

        self.absolute_value = QWidget()
        self.positivity = QWidget()
        self.multiplication_by_m1 = QWidget()
        self.conversion_n_to_z = QWidget()
        self.conversion_z_to_n = QWidget()
        self.addition = QWidget()
        self.subtraction = QWidget()
        self.multiplication = QWidget()
        self.quotient_of_division = QWidget()
        self.remainder_of_division = QWidget()

        self.absolute_value_ui()
        self.positivity_ui()
        self.multiplication_by_m1_ui()
        self.conversion_n_to_z_ui()
        self.conversion_z_to_n_ui()
        self.addition_ui()
        self.subtraction_ui()
        self.multiplication_ui()
        self.quotient_of_division_ui()
        self.remainder_of_division_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.absolute_value)
        self.Stack.addWidget(self.positivity)
        self.Stack.addWidget(self.multiplication_by_m1)
        self.Stack.addWidget(self.conversion_n_to_z)
        self.Stack.addWidget(self.conversion_z_to_n)
        self.Stack.addWidget(self.addition)
        self.Stack.addWidget(self.subtraction)
        self.Stack.addWidget(self.multiplication)
        self.Stack.addWidget(self.quotient_of_division)
        self.Stack.addWidget(self.remainder_of_division)

        hbox = QGridLayout(self)
        hbox.addWidget(self.label, 0, 0)
        hbox.addWidget(self.operations_with_integer_num, 1, 0)
        hbox.addWidget(self.Stack, 1, 1)

        self.setLayout(hbox)
        self.operations_with_integer_num.currentRowChanged.connect(self.display)
        self.res_0.clicked.connect(self.absolute_value_res)
        self.res_1.clicked.connect(self.positivity_res)
        self.res_2.clicked.connect(self.multiplication_by_m1_res)
        self.res_3.clicked.connect(self.conversion_n_to_z_res)
        self.res_4.clicked.connect(self.conversion_z_to_n_res)
        self.res_5.clicked.connect(self.addition_res)
        self.res_6.clicked.connect(self.subtraction_res)
        self.res_7.clicked.connect(self.multiplication_res)
        self.res_8.clicked.connect(self.quotient_of_division_res)
        self.res_9.clicked.connect(self.remainder_of_division_res)
        self.show()

    def absolute_value_res(self):
        answer = 'Answer'
        if self.num1_0.text() == '':
            self.answer_0.setText('Введите значение')
            return
        if not (''.join(self.num1_0.text().split('-')).isdigit()):
            self.answer_0.setText('Введите корректное значение')
            return
        self.answer_0.setText(answer)

    def positivity_res(self):
        answer = ['отрицательное', 'равно нулю', 'положительное']
        res = 1
        if self.num1_1.text() == '':
            self.answer_1.setText('Введите значение')
            return
        if not (''.join(self.num1_1.text().split('-')).isdigit()):
            self.answer_1.setText('Введите корректное значение')
            return
        self.answer_1.setText(answer[res])

    def multiplication_by_m1_res(self):
        answer = 'Answer'
        if self.num1_2.text() == '':
            self.answer_2.setText('Введите значение')
            return
        if not (''.join(self.num1_2.text().split('-')).isdigit()):
            self.answer_2.setText('Введите корректное значение')
            return
        self.answer_2.setText(answer)

    def conversion_n_to_z_res(self):
        answer = 'Answer'
        if self.num1_3.text() == '':
            self.answer_3.setText('Введите значение')
            return
        if not (''.join(self.num1_3.text().split('-')).isdigit()):
            self.answer_3.setText('Введите корректное значение')
            return
        self.answer_3.setText(answer)

    def conversion_z_to_n_res(self):
        answer = 'Answer'
        if self.num1_4.text() == '':
            self.answer_4.setText('Введите значение')
            return
        if not(''.join(self.num1_4.text().split('-')).isdigit()) or\
                (''.join(self.num1_4.text().split('-')).isdigit() and int(self.num1_4.text()) < 0):
            self.answer_4.setText('Введите корректное значение')
            return
        self.answer_4.setText(answer)

    def addition_res(self):
        answer = 'Answer'
        if self.num1_5.text() == '' or self.num2_5.text() == '':
            self.answer_5.setText('Введите все значения')
            return
        if not(''.join(self.num1_5.text().split('-')).isdigit()) or\
                not(''.join(self.num2_5.text().split('-')).isdigit()):
            self.answer_5.setText('Введите корректные значения')
            return
        self.answer_5.setText(answer)

    def subtraction_res(self):
        answer = 'Answer'
        if self.num1_6.text() == '' or self.num2_6.text() == '':
            self.answer_6.setText('Введите все значения')
            return
        if not(''.join(self.num1_6.text().split('-')).isdigit()) or\
                not(''.join(self.num2_6.text().split('-')).isdigit()):
            self.answer_6.setText('Введите корректные значения')
            return
        self.answer_6.setText(answer)

    def multiplication_res(self):
        answer = 'Answer'
        if self.num1_7.text() == '' or self.num2_7.text() == '':
            self.answer_7.setText('Введите все значения')
            return
        if not (''.join(self.num1_7.text().split('-')).isdigit()) or\
                not(''.join(self.num2_7.text().split('-')).isdigit()):
            self.answer_7.setText('Введите корректные значения')
            return
        self.answer_7.setText(answer)

    def quotient_of_division_res(self):
        answer = 'Answer'
        if self.num1_8.text() == '' or self.num2_8.text() == '':
            self.answer_8.setText('Введите все значения')
            return
        if not (''.join(self.num1_8.text().split('-')).isdigit()) or\
                not(''.join(self.num2_8.text().split('-')).isdigit()):
            self.answer_8.setText('Введите корректные значения')
            return
        if ''.join(self.num2_8.text().split('-')).isdigit() and int(self.num2_8.text()) == 0:
            self.answer_8.setText('Введите корректное значение делителя')
            return
        self.answer_8.setText(answer)

    def remainder_of_division_res(self):
        answer = 'Answer'
        if self.num1_9.text() == '' or self.num2_9.text() == '':
            self.answer_9.setText('Введите все значения')
            return
        if not(''.join(self.num1_9.text().split('-')).isdigit()) or\
                not(''.join(self.num2_9.text().split('-')).isdigit()):
            self.answer_9.setText('Введите корректные значения')
            return
        if ''.join(self.num2_9.text().split('-')).isdigit() and int(self.num2_9.text()) == 0:
            self.answer_9.setText('Введите корректное значение делителя')
            return
        self.answer_9.setText(answer)

    def absolute_value_ui(self):
        layout = QFormLayout()
        self.num1_0 = QLineEdit()
        self.res_0 = QPushButton("Получить ответ", self)
        self.answer_0 = QLineEdit()
        self.answer_0.setReadOnly(True)
        layout.addRow("Число", self.num1_0)
        layout.addRow(self.res_0)
        layout.addRow("Ответ", self.answer_0)
        self.absolute_value.setLayout(layout)

    def positivity_ui(self):
        layout = QFormLayout()
        self.num1_1 = QLineEdit()
        self.res_1 = QPushButton("Получить ответ", self)
        self.answer_1 = QLineEdit()
        self.answer_1.setReadOnly(True)
        layout.addRow("Число", self.num1_1)
        layout.addRow(self.res_1)
        layout.addRow("Ответ", self.answer_1)
        self.positivity.setLayout(layout)

    def multiplication_by_m1_ui(self):
        layout = QFormLayout()
        self.num1_2 = QLineEdit()
        self.res_2 = QPushButton("Получить ответ", self)
        self.answer_2 = QLineEdit()
        self.answer_2.setReadOnly(True)
        layout.addRow("Число", self.num1_2)
        layout.addRow(self.res_2)
        layout.addRow("Ответ", self.answer_2)
        self.multiplication_by_m1.setLayout(layout)

    def conversion_n_to_z_ui(self):
        layout = QFormLayout()
        self.num1_3 = QLineEdit()
        self.res_3 = QPushButton("Получить ответ", self)
        self.answer_3 = QLineEdit()
        self.answer_3.setReadOnly(True)
        layout.addRow("Число", self.num1_3)
        layout.addRow(self.res_3)
        layout.addRow("Ответ", self.answer_3)
        self.conversion_n_to_z.setLayout(layout)

    def conversion_z_to_n_ui(self):
        layout = QFormLayout()
        self.num1_4 = QLineEdit()
        self.res_4 = QPushButton("Получить ответ", self)
        self.answer_4 = QLineEdit()
        self.answer_4.setReadOnly(True)
        layout.addRow("Число", self.num1_4)
        layout.addRow(self.res_4)
        layout.addRow("Ответ", self.answer_4)
        self.conversion_z_to_n.setLayout(layout)

    def addition_ui(self):
        layout = QFormLayout()
        self.num1_5 = QLineEdit()
        self.num2_5 = QLineEdit()
        self.res_5 = QPushButton("Получить ответ", self)
        self.answer_5 = QLineEdit()
        self.answer_5.setReadOnly(True)
        layout.addRow("Первое число", self.num1_5)
        layout.addRow("Второе число", self.num2_5)
        layout.addRow(self.res_5)
        layout.addRow("Ответ", self.answer_5)
        self.addition.setLayout(layout)

    def subtraction_ui(self):
        layout = QFormLayout()
        self.num1_6 = QLineEdit()
        self.num2_6 = QLineEdit()
        self.res_6 = QPushButton("Получить ответ", self)
        self.answer_6 = QLineEdit()
        self.answer_6.setReadOnly(True)
        layout.addRow("Первое число", self.num1_6)
        layout.addRow("Второе число", self.num2_6)
        layout.addRow(self.res_6)
        layout.addRow("Ответ", self.answer_6)
        self.subtraction.setLayout(layout)

    def multiplication_ui(self):
        layout = QFormLayout()
        self.num1_7 = QLineEdit()
        self.num2_7 = QLineEdit()
        self.res_7 = QPushButton("Получить ответ", self)
        self.answer_7 = QLineEdit()
        self.answer_7.setReadOnly(True)
        layout.addRow("Первое число", self.num1_7)
        layout.addRow("Второе число", self.num2_7)
        layout.addRow(self.res_7)
        layout.addRow("Ответ", self.answer_7)
        self.multiplication.setLayout(layout)

    def quotient_of_division_ui(self):
        layout = QFormLayout()
        self.num1_8 = QLineEdit()
        self.num2_8 = QLineEdit()
        self.res_8 = QPushButton("Получить ответ", self)
        self.answer_8 = QLineEdit()
        self.answer_8.setReadOnly(True)
        layout.addRow("Первое число", self.num1_8)
        layout.addRow("Второе число", self.num2_8)
        layout.addRow(self.res_8)
        layout.addRow("Ответ", self.answer_8)
        self.quotient_of_division.setLayout(layout)

    def remainder_of_division_ui(self):
        layout = QFormLayout()
        self.num1_9 = QLineEdit()
        self.num2_9 = QLineEdit()
        self.res_9 = QPushButton("Получить ответ", self)
        self.answer_9 = QLineEdit()
        self.answer_9.setReadOnly(True)
        layout.addRow("Первое число", self.num1_9)
        layout.addRow("Второе число", self.num2_9)
        layout.addRow(self.res_9)
        layout.addRow("Ответ", self.answer_9)
        self.remainder_of_division.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        self.label.setText(self.labels[self.Stack.currentIndex()])


class Ration_numbers(QWidget):
    def __init__(self):
        super(Ration_numbers, self).__init__()
        self.setWindowTitle("Ration numbers")
        self.setFixedSize(QSize(800, 400))
        self.setStyleSheet('background-color: #99FF99;')
        self.labels = ['Сокращение дроби', 'Проверка сокращенного на целое', 'Преобразование из целого в дробное',
                       'Преобразование из дробного в целое', 'Сложение двух дробей', 'Вычитание двух дробей',
                       'Умножение дробей ', 'Деление дробей']
        self.label = QLabel(self.labels[0])
        self.font = self.label.font()
        self.font.setBold(True)
        self.label.setFont(self.font)
        self.operations_with_ration_num = QListWidget()
        self.operations_with_ration_num.insertItem(0, 'Сокращение дроби')
        self.operations_with_ration_num.insertItem(1, 'Проверка сокращенного на целое')
        self.operations_with_ration_num.insertItem(2, 'Преобразование из целого в дробное')
        self.operations_with_ration_num.insertItem(3, 'Преобразование из дробного в целое')
        self.operations_with_ration_num.insertItem(4, 'Сложение двух дробей')
        self.operations_with_ration_num.insertItem(5, 'Вычитание двух дробей')
        self.operations_with_ration_num.insertItem(6, 'Умножение дробей ')
        self.operations_with_ration_num.insertItem(7, 'Деление дробей')

        self.reduction = QWidget()
        self.check_abbreviated_num = QWidget()
        self.conversion_z_to_q = QWidget()
        self.conversion_q_to_z = QWidget()
        self.addition = QWidget()
        self.subtraction = QWidget()
        self.multiplication = QWidget()
        self.division = QWidget()

        self.reduction_ui()
        self.check_abbreviated_num_ui()
        self.conversion_z_to_q_ui()
        self.conversion_q_to_z_ui()
        self.addition_ui()
        self.subtraction_ui()
        self.multiplication_ui()
        self.division_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.reduction)
        self.Stack.addWidget(self.check_abbreviated_num)
        self.Stack.addWidget(self.conversion_z_to_q)
        self.Stack.addWidget(self.conversion_q_to_z)
        self.Stack.addWidget(self.addition)
        self.Stack.addWidget(self.subtraction)
        self.Stack.addWidget(self.multiplication)
        self.Stack.addWidget(self.division)

        hbox = QGridLayout(self)
        hbox.addWidget(self.label, 0, 0)
        hbox.addWidget(self.operations_with_ration_num, 1, 0)
        hbox.addWidget(self.Stack, 1, 1)

        self.setLayout(hbox)
        self.operations_with_ration_num.currentRowChanged.connect(self.display)
        self.res_0.clicked.connect(self.reduction_res)
        self.res_1.clicked.connect(self.check_abbreviated_num_res)
        self.res_2.clicked.connect(self.conversion_z_to_q_res)
        self.res_3.clicked.connect(self.conversion_q_to_z_res)
        self.res_4.clicked.connect(self.addition_res)
        self.res_5.clicked.connect(self.subtraction_res)
        self.res_6.clicked.connect(self.multiplication_res)
        self.res_7.clicked.connect(self.division_res)
        self.show()

    def reduction_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.numerator_0.text() == '':
            self.answer_n_0.setText('Введите числитель')
            return
        if self.denominator_0.text() == '':
            self.answer_d_0.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator_0.text().split('-')).isdigit()):
            self.answer_n_0.setText('Введите корректное значение числителя')
            return
        if not (''.join(self.denominator_0.text().split('-')).isdigit()) or\
                (''.join(self.denominator_0.text().split('-')).isdigit() and int(self.denominator_0.text()) == 0):
            self.answer_d_0.setText('Введите корректное значение знаменателя')
            return
        self.answer_n_0.setText(ans_n)
        self.answer_d_0.setText(ans_d)

    def check_abbreviated_num_res(self):
        answer = 'Answer'
        if self.numerator_1.text() == '' or self.denominator_1.text() == '':
            self.answer_1.setText('Введите значения')
            return
        if not(''.join(self.numerator_0.text().split('-')).isdigit()):
            self.answer_1.setText('Введите корректное значение числителя')
            return
        if not (self.denominator_1.text().isdigit()) or (
                self.denominator_1.text().isdigit() and int(self.denominator_1.text()) == 0):
            self.answer_1.setText('Введите корректное значение знаменателя')
            return
        self.answer_1.setText(answer)

    def conversion_z_to_q_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.num_2.text() == '':
            self.answer_n_2.setText('Введите значение')
            return
        if not(''.join(self.num_2.text().split('-')).isdigit()):
            self.answer_n_2.setText('Введите корректное значение')
            return
        self.answer_n_2.setText(ans_n)
        self.answer_d_2.setText(ans_d)

    def conversion_q_to_z_res(self):
        answer = 'Answer'
        if self.numerator_3.text() == '' or self.denominator_3.text() == '':
            self.answer_3.setText('Введите значения')
            return
        if not(''.join(self.numerator_3.text().split('-')).isdigit()):
            self.answer_3.setText('Введите корректное значение числителя')
            return
        if not (self.denominator_3.text().isdigit()) or (
                self.denominator_3.text().isdigit() and int(self.denominator_3.text()) == 0):
            self.answer_3.setText('Введите корректное значение знаменателя')
            return
        self.answer_3.setText(answer)

    def addition_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.numerator1_4.text() == '' or self.numerator2_4.text() == '':
            self.answer_n_4.setText('Введите числитель')
            return
        if self.denominator1_4.text() == '' or self.denominator2_4.text() == '':
            self.answer_d_4.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator1_4.text().split('-')).isdigit()) or\
                not(''.join(self.numerator2_4.text().split('-')).isdigit()):
            self.answer_n_4.setText('Введите корректное значение числителя')
            return
        if not (self.denominator1_4.text().isdigit()) or (
                self.denominator1_4.text().isdigit() and int(self.denominator1_4.text()) == 0):
            self.answer_d_4.setText('Введите корректное значение знаменателя')
            return
        if not (self.denominator2_4.text().isdigit()) or (
                self.denominator2_4.text().isdigit() and int(self.denominator2_4.text()) == 0):
            self.answer_d_4.setText('Введите корректное значение знаменателя')
            return
        self.answer_n_4.setText(ans_n)
        self.answer_d_4.setText(ans_d)

    def subtraction_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.numerator1_5.text() == '' or self.numerator2_5.text() == '':
            self.answer_n_5.setText('Введите числитель')
            return
        if self.denominator1_5.text() == '' or self.denominator2_5.text() == '':
            self.answer_d_5.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator1_5.text().split('-')).isdigit()) or\
                not(''.join(self.numerator2_5.text().split('-')).isdigit()) :
            self.answer_n_5.setText('Введите корректное значение числителя')
            return
        if not (self.denominator1_5.text().isdigit()) or (
                self.denominator1_5.text().isdigit() and int(self.denominator1_5.text()) == 0):
            self.answer_d_5.setText('Введите корректное значение знаменателя')
            return
        if not (self.denominator2_5.text().isdigit()) or (
                self.denominator2_5.text().isdigit() and int(self.denominator2_5.text()) == 0):
            self.answer_d_5.setText('Введите корректное значение знаменателя')
            return
        self.answer_n_5.setText(ans_n)
        self.answer_d_5.setText(ans_d)

    def multiplication_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.numerator1_6.text() == '' or self.numerator2_6.text() == '':
            self.answer_n_6.setText('Введите числитель')
            return
        if self.denominator1_6.text() == '' or self.denominator2_6.text() == '':
            self.answer_d_6.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator1_6.text().split('-')).isdigit()) or\
                not(''.join(self.numerator2_6.text().split('-')).isdigit()) :
            self.answer_n_6.setText('Введите корректное значение числителя')
            return
        if not (self.denominator1_6.text().isdigit()) or (
                self.denominator1_6.text().isdigit() and int(self.denominator1_6.text()) == 0):
            self.answer_d_6.setText('Введите корректное значение знаменателя')
            return
        if not (self.denominator2_6.text().isdigit()) or (
                self.denominator2_6.text().isdigit() and int(self.denominator2_6.text()) == 0):
            self.answer_d_6.setText('Введите корректное значение знаменателя')
            return
        self.answer_n_6.setText(ans_n)
        self.answer_d_6.setText(ans_d)

    def division_res(self):
        ans_n, ans_d = 'числитель', 'знаменатель'
        if self.numerator1_7.text() == '' or self.numerator2_7.text() == '':
            self.answer_n_7.setText('Введите числитель')
            return
        if self.denominator1_7.text() == '' or self.denominator2_7.text() == '':
            self.answer_d_7.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator1_7.text().split('-')).isdigit()) or\
                not(''.join(self.numerator2_7.text().split('-')).isdigit()) :
            self.answer_n_7.setText('Введите корректное значение числителя')
            return
        if not (self.numerator2_7.text().isdigit()) or (
                self.numerator2_7.text().isdigit() and int(self.numerator2_7.text()) == 0):
            self.answer_n_7.setText('Делитель не должен быть равен нулю')
            return
        if not (self.denominator1_7.text().isdigit()) or (
                self.denominator1_7.text().isdigit() and int(self.denominator1_7.text()) == 0):
            self.answer_d_7.setText('Введите корректное значение знаменателя')
            return
        if not (self.denominator2_7.text().isdigit()) or (
                self.denominator2_7.text().isdigit() and int(self.denominator2_7.text()) == 0):
            self.answer_d_7.setText('Введите корректное значение знаменателя')
            return
        self.answer_n_7.setText(ans_n)
        self.answer_d_7.setText(ans_d)

    def reduction_ui(self):
        layout = QFormLayout()
        self.numerator_0 = QLineEdit()
        self.denominator_0 = QLineEdit()
        self.res_0 = QPushButton("Получить ответ", self)
        self.answer_0 = QLabel("Ответ")
        self.answer_n_0 = QLineEdit()
        self.answer_n_0.setReadOnly(True)
        self.answer_d_0 = QLineEdit()
        self.answer_d_0.setReadOnly(True)
        layout.addRow("Числитель", self.numerator_0)
        layout.addRow("Знаменатель", self.denominator_0)
        layout.addRow(self.res_0)
        layout.addRow(self.answer_0)
        layout.addRow("Числитель", self.answer_n_0)
        layout.addRow("Знаменатель", self.answer_d_0)
        self.reduction.setLayout(layout)

    def check_abbreviated_num_ui(self):
        layout = QFormLayout()
        self.numerator_1 = QLineEdit()
        self.denominator_1 = QLineEdit()
        self.res_1 = QPushButton("Получить ответ", self)
        self.answer_1 = QLineEdit()
        self.answer_1.setReadOnly(True)
        layout.addRow("Числитель", self.numerator_1)
        layout.addRow("Знаменатель", self.denominator_1)
        layout.addRow(self.res_1)
        layout.addRow("Ответ", self.answer_1)
        self.check_abbreviated_num.setLayout(layout)

    def conversion_z_to_q_ui(self):
        layout = QFormLayout()
        self.num_2 = QLineEdit()
        self.res_2 = QPushButton("Получить ответ", self)
        self.answer_2 = QLabel("Ответ")
        self.answer_n_2 = QLineEdit()
        self.answer_n_2.setReadOnly(True)
        self.answer_d_2 = QLineEdit()
        self.answer_d_2.setReadOnly(True)
        layout.addRow("Число", self.num_2)
        layout.addRow(self.res_2)
        layout.addRow(self.answer_2)
        layout.addRow("Числитель", self.answer_n_2)
        layout.addRow("Знаменатель", self.answer_d_2)
        self.conversion_z_to_q.setLayout(layout)

    def conversion_q_to_z_ui(self):
        layout = QFormLayout()
        self.numerator_3 = QLineEdit()
        self.denominator_3 = QLineEdit()
        self.res_3 = QPushButton("Получить ответ", self)
        self.answer_3 = QLineEdit()
        self.answer_3.setReadOnly(True)
        layout.addRow("Числитель", self.numerator_3)
        layout.addRow("Знаменатель", self.denominator_3)
        layout.addRow(self.res_3)
        layout.addRow("Ответ", self.answer_3)
        self.conversion_q_to_z.setLayout(layout)

    def addition_ui(self):
        layout = QFormLayout()
        self.rat1_4 = QLabel("Первая дробь")
        self.numerator1_4 = QLineEdit()
        self.denominator1_4 = QLineEdit()
        self.rat2_4 = QLabel("Вторая дробь")
        self.numerator2_4 = QLineEdit()
        self.denominator2_4 = QLineEdit()
        self.res_4 = QPushButton("Получить ответ", self)
        self.answer_4 = QLabel("Ответ")
        self.answer_n_4 = QLineEdit()
        self.answer_n_4.setReadOnly(True)
        self.answer_d_4 = QLineEdit()
        self.answer_d_4.setReadOnly(True)
        layout.addRow(self.rat1_4)
        layout.addRow("Числитель", self.numerator1_4)
        layout.addRow("Знаменатель", self.denominator1_4)
        layout.addRow(self.rat2_4)
        layout.addRow("Числитель", self.numerator2_4)
        layout.addRow("Знаменатель", self.denominator2_4)
        layout.addRow(self.res_4)
        layout.addRow(self.answer_4)
        layout.addRow("Числитель", self.answer_n_4)
        layout.addRow("Знаменатель", self.answer_d_4)
        self.addition.setLayout(layout)

    def subtraction_ui(self):
        layout = QFormLayout()
        self.rat1_5 = QLabel("Первая дробь")
        self.numerator1_5 = QLineEdit()
        self.denominator1_5 = QLineEdit()
        self.rat2_5 = QLabel("Вторая дробь")
        self.numerator2_5 = QLineEdit()
        self.denominator2_5 = QLineEdit()
        self.res_5 = QPushButton("Получить ответ", self)
        self.answer_5 = QLabel("Ответ")
        self.answer_n_5 = QLineEdit()
        self.answer_n_5.setReadOnly(True)
        self.answer_d_5 = QLineEdit()
        self.answer_d_5.setReadOnly(True)
        layout.addRow(self.rat1_5)
        layout.addRow("Числитель", self.numerator1_5)
        layout.addRow("Знаменатель", self.denominator1_5)
        layout.addRow(self.rat2_5)
        layout.addRow("Числитель", self.numerator2_5)
        layout.addRow("Знаменатель", self.denominator2_5)
        layout.addRow(self.res_5)
        layout.addRow(self.answer_5)
        layout.addRow("Числитель", self.answer_n_5)
        layout.addRow("Знаменатель", self.answer_d_5)
        self.subtraction.setLayout(layout)

    def multiplication_ui(self):
        layout = QFormLayout()
        self.rat1_6 = QLabel("Первая дробь")
        self.numerator1_6 = QLineEdit()
        self.denominator1_6 = QLineEdit()
        self.rat2_6 = QLabel("Вторая дробь")
        self.numerator2_6 = QLineEdit()
        self.denominator2_6 = QLineEdit()
        self.res_6 = QPushButton("Получить ответ", self)
        self.answer_6 = QLabel("Ответ")
        self.answer_n_6 = QLineEdit()
        self.answer_n_6.setReadOnly(True)
        self.answer_d_6 = QLineEdit()
        self.answer_d_6.setReadOnly(True)
        layout.addRow(self.rat1_6)
        layout.addRow("Числитель", self.numerator1_6)
        layout.addRow("Знаменатель", self.denominator1_6)
        layout.addRow(self.rat2_6)
        layout.addRow("Числитель", self.numerator2_6)
        layout.addRow("Знаменатель", self.denominator2_6)
        layout.addRow(self.res_6)
        layout.addRow(self.answer_6)
        layout.addRow("Числитель", self.answer_n_6)
        layout.addRow("Знаменатель", self.answer_d_6)
        self.multiplication.setLayout(layout)

    def division_ui(self):
        layout = QFormLayout()
        self.rat1_7 = QLabel("Первая дробь")
        self.numerator1_7 = QLineEdit()
        self.denominator1_7 = QLineEdit()
        self.rat2_7 = QLabel("Вторая дробь")
        self.numerator2_7 = QLineEdit()
        self.denominator2_7 = QLineEdit()
        self.res_7 = QPushButton("Получить ответ", self)
        self.answer_7 = QLabel("Ответ")
        self.answer_n_7 = QLineEdit()
        self.answer_n_7.setReadOnly(True)
        self.answer_d_7 = QLineEdit()
        self.answer_d_7.setReadOnly(True)
        layout.addRow(self.rat1_7)
        layout.addRow("Числитель", self.numerator1_7)
        layout.addRow("Знаменатель", self.denominator1_7)
        layout.addRow(self.rat2_7)
        layout.addRow("Числитель", self.numerator2_7)
        layout.addRow("Знаменатель", self.denominator2_7)
        layout.addRow(self.res_7)
        layout.addRow(self.answer_7)
        layout.addRow("Числитель", self.answer_n_7)
        layout.addRow("Знаменатель", self.answer_d_7)
        self.division.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        self.label.setText(self.labels[self.Stack.currentIndex()])


class Polinoms(QWidget):

    def __init__(self, polinom):
        super(Polinoms, self).__init__()
        self.setWindowTitle("Polinoms")
        self.setFixedSize(QSize(800, 400))
        self.setStyleSheet('background-color: #CC99FF;')
        self.polinom = polinom
        self.polinom2 = Polinom()
        self.degree_of_polinom = self.polinom.get_degree()
        self.degree_of_polinom2 = self.polinom2.get_degree()
        self.labels = ['Сложение многочленов', 'Вычитание многочленов', 'Умножение на рациональное число',
                       'Умножение на x^k', 'Старший коэффициент многочлена', 'Степень многочлена',
                       'НОК знаменателей и НОД числителей', 'Умножение многочленов',
                       'Частное от деления многочлена на многочлен', 'Остаток от деления многочлена на многочлен',
                       'НОД многочленов', 'Производная многочлена', 'Преобразование многочлена']
        self.label = QLabel(self.labels[0])
        self.font = self.label.font()
        self.font.setBold(True)
        self.label.setFont(self.font)
        self.operations_with_polinom = QListWidget()
        self.operations_with_polinom.insertItem(0, 'Сложение многочленов')
        self.operations_with_polinom.insertItem(1, 'Вычитание многочленов')
        self.operations_with_polinom.insertItem(2, 'Умножение на рациональное число')
        self.operations_with_polinom.insertItem(3, 'Умножение на x^k')
        self.operations_with_polinom.insertItem(4, 'Старший коэффициент многочлена')
        self.operations_with_polinom.insertItem(5, 'Степень многочлена')
        self.operations_with_polinom.insertItem(6, 'НОК знаменателей и НОД числителей')
        self.operations_with_polinom.insertItem(7, 'Умножение многочленов')
        self.operations_with_polinom.insertItem(8, 'Частное от деления многочлена на многочлен')
        self.operations_with_polinom.insertItem(9, 'Остаток от деления многочлена на многочлен')
        self.operations_with_polinom.insertItem(10, 'НОД многочленов')
        self.operations_with_polinom.insertItem(11, 'Производная многочлена')
        self.operations_with_polinom.insertItem(12, 'Преобразование многочлена')

        self.input_polinom = QPushButton("Ввести или изменить многочлен", self)
        self.input_polinom.resize(200, 40)
        self.input_polinom.clicked.connect(self.input_pol)

        self.save_polinom = QPushButton("Выполнить действия с ответом", self)
        self.save_polinom.resize(200, 40)
        self.save_polinom.clicked.connect(self.save_pol)

        self.addition = QWidget()
        self.subtraction = QWidget()
        self.multiplication_by_ration_number = QWidget()
        self.multiplication_by_x = QWidget()
        self.leading_coefficient = QWidget()
        self.degree = QWidget()
        self.NOK_NOD = QWidget()
        self.multiplication = QWidget()
        self.quotient_of_division = QWidget()
        self.remainder_of_division = QWidget()
        self.NOD = QWidget()
        self.derivative = QWidget()
        self.conversion = QWidget()

        self.addition_ui()
        self.subtraction_ui()
        self.multiplication_by_ration_number_ui()
        self.multiplication_by_x_ui()
        self.leading_coefficient_ui()
        self.degree_ui()
        self.NOK_NOD_ui()
        self.multiplication_ui()
        self.quotient_of_division_ui()
        self.remainder_of_division_ui()
        self.NOD_ui()
        self.derivative_ui()
        self.conversion_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.addition)
        self.Stack.addWidget(self.subtraction)
        self.Stack.addWidget(self.multiplication_by_ration_number)
        self.Stack.addWidget(self.multiplication_by_x)
        self.Stack.addWidget(self.leading_coefficient)
        self.Stack.addWidget(self.degree)
        self.Stack.addWidget(self.NOK_NOD)
        self.Stack.addWidget(self.multiplication)
        self.Stack.addWidget(self.quotient_of_division)
        self.Stack.addWidget(self.remainder_of_division)
        self.Stack.addWidget(self.NOD)
        self.Stack.addWidget(self.derivative)
        self.Stack.addWidget(self.conversion)

        hbox = QGridLayout(self)
        hbox.addWidget(self.label, 0, 0)
        hbox.addWidget(self.operations_with_polinom, 1, 0)
        hbox.addWidget(self.Stack, 1, 1)
        hbox.addWidget(self.input_polinom, 2, 0)
        hbox.addWidget(self.save_polinom, 2, 1)

        self.setLayout(hbox)
        self.operations_with_polinom.currentRowChanged.connect(self.display)
        self.show()

    def input_pol(self):
        self.degree_of_polinom, ok = QInputDialog.getText(self, "Ввод многочлена", "Введите степень многочлена")
        if not (self.degree_of_polinom.isdigit()):
            self.degree_of_polinom = 0
        if ok:
            self.degree_of_polinom = int(self.degree_of_polinom)
            if self.degree_of_polinom != self.polinom.get_degree():
                self.polinom.change_size(self.degree_of_polinom)
        else:
            return
        self.input_for_polinoms = Input_polinom(self.polinom, self.degree_of_polinom)
        self.input_for_polinoms.show()
        self.input_for_polinoms.exec()

    def input_pol2(self):
        self.degree_of_polinom2, ok = QInputDialog.getText(self, "Ввод многочлена", "Введите степень многочлена")
        if not (self.degree_of_polinom2.isdigit()):
            self.degree_of_polinom2 = 0
        if ok:
            self.degree_of_polinom2 = int(self.degree_of_polinom2)
            if self.degree_of_polinom2 != self.polinom2.get_degree():
                self.polinom2.change_size(self.degree_of_polinom2)
        else:
            return
        self.input_for_polinoms = Input_polinom(self.polinom2, self.degree_of_polinom2)
        self.input_for_polinoms.show()
        self.input_for_polinoms.exec()
        self.pol2_0.setText(str(self.polinom2))

    def save_pol(self):
        text = 'Answer'
        if self.Stack.currentWidget() == self.addition:
            text = self.answer_0.text()
        elif self.Stack.currentWidget() == self.subtraction:
            text = self.answer_1.text()
        elif self.Stack.currentWidget() == self.multiplication_by_ration_number:
            text = self.answer_2.text()
        elif self.Stack.currentWidget() == self.multiplication_by_x:
            text = self.answer_3.text()
        elif self.Stack.currentWidget() == self.leading_coefficient:
            text = self.answer_4.text()
        elif self.Stack.currentWidget() == self.degree:
            text = self.answer_5.text()
        elif self.Stack.currentWidget() == self.NOK_NOD:
            text = self.answer_6.text()
        elif self.Stack.currentWidget() == self.multiplication:
            text = self.answer_7.text()
        elif self.Stack.currentWidget() == self.quotient_of_division:
            text = self.answer_8.text()
        elif self.Stack.currentWidget() == self.remainder_of_division:
            text = self.answer_9.text()
        elif self.Stack.currentWidget() == self.NOD:
            text = self.answer_10.text()
        elif self.Stack.currentWidget() == self.derivative:
            text = self.answer_11.text()
        elif self.Stack.currentWidget() == self.conversion:
            text = self.answer_12.text()
        if text != 'Answer' and text != 'Введите числитель' and text != 'Введите знаменатель' and text != '' and\
            text != 'Введите корректное значение числителя' and text != 'Введите корректное значение знаменателя':
            self.move_polinom(text)

    def move_polinom(self, polinom):
        self.pol1_0.setText(polinom)
        self.pol1_1.setText(polinom)
        self.pol1_2.setText(polinom)
        self.pol1_3.setText(polinom)
        self.pol1_4.setText(polinom)
        self.pol1_5.setText(polinom)
        self.pol1_6.setText(polinom)
        self.pol1_7.setText(polinom)
        self.pol1_8.setText(polinom)
        self.pol1_9.setText(polinom)
        self.pol1_10.setText(polinom)
        self.pol1_11.setText(polinom)
        self.pol1_12.setText(polinom)
        self.polinom.str_to_polinom(polinom)

    def addition_res(self):
        answer = 'Answer'
        self.answer_0.setText(answer)

    def subtraction_res(self):
        answer = 'Answer'
        self.answer_1.setText(answer)

    def multiplication_by_ration_number_res(self):
        answer = 'Answer'
        if self.numerator_2.text() == '':
            self.answer_2.setText('Введите числитель')
            return
        if self.denominator_2.text() == '':
            self.answer_2.setText('Введите знаменатель')
            return
        if not(''.join(self.numerator_2.text().split('-')).isdigit()):
            self.answer_2.setText('Введите корректное значение числителя')
            return
        if not (''.join(self.denominator_2.text().split('-')).isdigit()) or\
                (''.join(self.denominator_2.text().split('-')).isdigit() and int(self.denominator_2.text()) == 0):
            self.answer_2.setText('Введите корректное значение знаменателя')
            return
        self.answer_2.setText(answer)

    def multiplication_by_x_res(self):
        answer = 'Answer'
        self.answer_3.setText(answer)

    def leading_coefficient_res(self):
        answer = 'Answer'
        self.answer_4.setText(answer)

    def degree_res(self):
        answer = 'Answer'
        self.answer_5.setText(answer)

    def NOK_NOD_res(self):
        answer = 'Answer'
        self.answer_6.setText(answer)

    def multiplication_res(self):
        answer = 'Answer'
        self.answer_7.setText(answer)

    def quotient_of_division_res(self):
        answer = 'Answer'
        if self.pol2_8.text() == '0' or self.pol2_8.text() == '':
            self.answer_8.setText('Знаменатеьль не может быть нулём')
            return
        self.answer_8.setText(answer)

    def remainder_of_division_res(self):
        answer = 'Answer'
        if self.pol2_9.text() == '0' or self.pol2_9.text() == '':
            self.answer_9.setText('Знаменатеьль не может быть нулём')
            return
        self.answer_9.setText(answer)

    def NOD_res(self):
        answer = 'Answer'
        self.answer_10.setText(answer)

    def derivative_res(self):
        answer = 'Answer'
        self.answer_11.setText(answer)

    def conversion_res(self):
        answer = 'Answer'
        self.answer_12.setText(answer)

    def addition_ui(self):
        layout = QFormLayout()
        self.pol1_0 = QLineEdit()
        self.pol1_0.setText(str(self.polinom))
        self.pol1_0.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_0 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_0.clicked.connect(self.input_pol2)
        self.pol2_0 = QLineEdit()
        self.pol2_0.setText(str(self.polinom2))
        self.pol2_0.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_0 = QPushButton("Получить ответ")
        self.res_0.clicked.connect(self.addition_res)
        self.answer_0 = QLineEdit()
        self.answer_0.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_0)
        layout.addRow(self.input_second_polinom_0)
        layout.addRow("Второй многочлен", self.pol2_0)
        layout.addRow(self.res_0)
        layout.addRow("Ответ", self.answer_0)
        self.addition.setLayout(layout)

    def subtraction_ui(self):
        layout = QFormLayout()
        self.pol1_1 = QLineEdit()
        self.pol1_1.setText(str(self.polinom))
        self.pol1_1.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_1 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_1.clicked.connect(self.input_pol2)
        self.pol2_1 = QLineEdit()
        self.pol2_1.setText(str(self.polinom2))
        self.pol2_1.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_1 = QPushButton("Получить ответ")
        self.res_1.clicked.connect(self.subtraction_res)
        self.answer_1 = QLineEdit()
        self.answer_1.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_1)
        layout.addRow(self.input_second_polinom_1)
        layout.addRow("Второй многочлен", self.pol2_1)
        layout.addRow(self.res_1)
        layout.addRow("Ответ", self.answer_1)
        self.subtraction.setLayout(layout)

    def multiplication_by_ration_number_ui(self):
        layout = QFormLayout()
        self.pol1_2 = QLineEdit()
        self.pol1_2.setText(str(self.polinom))
        self.pol1_2.textEdited.connect(self.polinom.str_to_polinom)
        self.numerator_2 = QLineEdit()
        self.denominator_2 = QLineEdit()
        self.res_2 = QPushButton("Получить ответ", self)
        self.res_2.clicked.connect(self.multiplication_by_ration_number_res)
        self.answer_2 = QLineEdit()
        self.answer_2.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_2)
        layout.addRow("Числитель", self.numerator_2)
        layout.addRow("Знаменатель", self.denominator_2)
        layout.addRow(self.res_2)
        layout.addRow("Ответ", self.answer_2)
        self.multiplication_by_ration_number.setLayout(layout)

    def multiplication_by_x_ui(self):
        layout = QFormLayout()
        self.pol1_3 = QLineEdit()
        self.pol1_3.setText(str(self.polinom))
        self.pol1_3.textEdited.connect(self.polinom.str_to_polinom)
        self.num_3 = QLineEdit()
        self.res_3 = QPushButton("Получить ответ", self)
        self.res_3.clicked.connect(self.multiplication_by_x_res)
        self.answer_3 = QLineEdit()
        self.answer_3.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_3)
        layout.addRow("Введите степень для x", self.num_3)
        layout.addRow(self.res_3)
        layout.addRow("Ответ", self.answer_3)
        self.multiplication_by_x.setLayout(layout)

    def leading_coefficient_ui(self):
        layout = QFormLayout()
        self.pol1_4 = QLineEdit()
        self.pol1_4.setText(str(self.polinom))
        self.pol1_4.textEdited.connect(self.polinom.str_to_polinom)
        self.res_4 = QPushButton("Получить ответ", self)
        self.res_4.clicked.connect(self.leading_coefficient_res)
        self.answer_4 = QLineEdit()
        self.answer_4.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_4)
        layout.addRow(self.res_4)
        layout.addRow("Ответ", self.answer_4)
        self.leading_coefficient.setLayout(layout)

    def degree_ui(self):
        layout = QFormLayout()
        self.pol1_5 = QLineEdit()
        self.pol1_5.setText(str(self.polinom))
        self.pol1_5.textEdited.connect(self.polinom.str_to_polinom)
        self.res_5 = QPushButton("Получить ответ", self)
        self.res_5.clicked.connect(self.degree_res)
        self.answer_5 = QLineEdit()
        self.answer_5.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_5)
        layout.addRow(self.res_5)
        layout.addRow("Ответ", self.answer_5)
        self.degree.setLayout(layout)

    def NOK_NOD_ui(self):
        layout = QFormLayout()
        self.pol1_6 = QLineEdit()
        self.pol1_6.setText(str(self.polinom))
        self.pol1_6.textEdited.connect(self.polinom.str_to_polinom)
        self.res_6 = QPushButton("Получить ответ", self)
        self.res_6.clicked.connect(self.NOK_NOD_res)
        self.answer_6 = QLineEdit()
        self.answer_6.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_6)
        layout.addRow(self.res_6)
        layout.addRow("Ответ", self.answer_6)
        self.NOK_NOD.setLayout(layout)

    def multiplication_ui(self):
        layout = QFormLayout()
        self.pol1_7 = QLineEdit()
        self.pol1_7.setText(str(self.polinom))
        self.pol1_7.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_7 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_7.clicked.connect(self.input_pol2)
        self.pol2_7 = QLineEdit()
        self.pol2_7.setText(str(self.polinom2))
        self.pol2_7.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_7 = QPushButton("Получить ответ")
        self.res_7.clicked.connect(self.multiplication_res)
        self.answer_7 = QLineEdit()
        self.answer_7.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_7)
        layout.addRow(self.input_second_polinom_7)
        layout.addRow("Второй многочлен", self.pol2_7)
        layout.addRow(self.res_7)
        layout.addRow("Ответ", self.answer_7)
        self.multiplication.setLayout(layout)

    def quotient_of_division_ui(self):
        layout = QFormLayout()
        self.pol1_8 = QLineEdit()
        self.pol1_8.setText(str(self.polinom))
        self.pol1_8.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_8 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_8.clicked.connect(self.input_pol2)
        self.pol2_8 = QLineEdit()
        self.pol2_8.setText(str(self.polinom2))
        self.pol2_8.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_8 = QPushButton("Получить ответ")
        self.res_8.clicked.connect(self.quotient_of_division_res)
        self.answer_8 = QLineEdit()
        self.answer_8.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_8)
        layout.addRow(self.input_second_polinom_8)
        layout.addRow("Второй многочлен", self.pol2_8)
        layout.addRow(self.res_8)
        layout.addRow("Ответ", self.answer_8)
        self.quotient_of_division.setLayout(layout)

    def remainder_of_division_ui(self):
        layout = QFormLayout()
        self.pol1_9 = QLineEdit()
        self.pol1_9.setText(str(self.polinom))
        self.pol1_9.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_9 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_9.clicked.connect(self.input_pol2)
        self.pol2_9 = QLineEdit()
        self.pol2_9.setText(str(self.polinom2))
        self.pol2_9.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_9 = QPushButton("Получить ответ")
        self.res_9.clicked.connect(self.remainder_of_division_res)
        self.answer_9 = QLineEdit()
        self.answer_9.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_9)
        layout.addRow(self.input_second_polinom_9)
        layout.addRow("Второй многочлен", self.pol2_9)
        layout.addRow(self.res_9)
        layout.addRow("Ответ", self.answer_9)
        self.remainder_of_division.setLayout(layout)

    def NOD_ui(self):
        layout = QFormLayout()
        self.pol1_10 = QLineEdit()
        self.pol1_10.setText(str(self.polinom))
        self.pol1_10.textEdited.connect(self.polinom.str_to_polinom)
        self.input_second_polinom_10 = QPushButton("Ввести второй многочлен")
        self.input_second_polinom_10.clicked.connect(self.input_pol2)
        self.pol2_10 = QLineEdit()
        self.pol2_10.setText(str(self.polinom2))
        self.pol2_10.textEdited.connect(self.polinom2.str_to_polinom)
        self.res_10 = QPushButton("Получить ответ")
        self.res_10.clicked.connect(self.NOD_res)
        self.answer_10 = QLineEdit()
        self.answer_10.setReadOnly(True)
        layout.addRow("Первый многочлен", self.pol1_10)
        layout.addRow(self.input_second_polinom_10)
        layout.addRow("Второй многочлен", self.pol2_10)
        layout.addRow(self.res_10)
        layout.addRow("Ответ", self.answer_10)
        self.NOD.setLayout(layout)

    def derivative_ui(self):
        layout = QFormLayout()
        self.pol1_11 = QLineEdit()
        self.pol1_11.setText(str(self.polinom))
        self.pol1_11.textEdited.connect(self.polinom.str_to_polinom)
        self.res_11 = QPushButton("Получить ответ", self)
        self.res_11.clicked.connect(self.derivative_res)
        self.answer_11 = QLineEdit()
        self.answer_11.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_11)
        layout.addRow(self.res_11)
        layout.addRow("Ответ", self.answer_11)
        self.derivative.setLayout(layout)

    def conversion_ui(self):
        layout = QFormLayout()
        self.pol1_12 = QLineEdit()
        self.pol1_12.setText(str(self.polinom))
        self.pol1_12.textEdited.connect(self.polinom.str_to_polinom)
        self.res_12 = QPushButton("Получить ответ", self)
        self.res_12.clicked.connect(self.conversion_res)
        self.answer_12 = QLineEdit()
        self.answer_12.setReadOnly(True)
        layout.addRow("Многочлен", self.pol1_12)
        layout.addRow(self.res_12)
        layout.addRow("Ответ", self.answer_12)
        self.conversion.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)
        self.label.setText(self.labels[self.Stack.currentIndex()])


class Polinom():
    def __init__(self, m=0):
        if m < 0:
            m = 0
        self.polinom = [0] * (m + 1)
        self.degree = m

    def __str__(self):
        line = []
        for i in range(self.degree, 0, -1):
            if self.polinom[i] == 1:
                if i != 1:
                    line.append(f"x^{i}")
                else:
                    line.append(f"x")
            elif self.polinom[i] != 0:
                if i != 1:
                    line.append(f"{self.polinom[i]}x^{i}")
                else:
                    line.append(f"{self.polinom[i]}x")
        if self.polinom[0] != 0:
            line.append(str(self.polinom[0]))
        line = ' + '.join(line)
        if line == '':
            line = '0'
        return line

    def str_to_polinom(self, line):
        st = ''.join(line.split())
        sign = ['^', 'x', '-', '+']
        for el in sign:
            st = ''.join(st.split(el))
        if line == '' or not(st.isdigit()):
            line = '0'
        line = line.split('+')
        line = [el.split('x^') for el in line]
        for i in range(self.degree + 1):
            self.polinom[i] = 0
        for el in line:
            if len(el) > 1 and len(el[1]) > 0:
                if el[0] == '':
                    el[0] = '0'
                elif el[0] == '-':
                    el[0] = '-1'
                if int(el[1]) > self.degree:
                    self.change_size(int(el[1]))
                if '.' in el[0]:
                    self.change(int(el[1]), float(el[0]))
                else:
                    self.change(int(el[1]), int(el[0]))
            else:
                if len(el[0]) > 0:
                    el[0] = ''.join(el[0].split())
                    if el[0] == '':
                        el[0] = '0'
                    elif el[0] == '-':
                        el[0] = '-1'
                    if 'x' not in el[0]:
                        if '.' in el[0]:
                            self.change(0, float(el[0]))
                        else:
                            self.change(0, int(el[0]))
                    else:
                        if self.degree < 1:
                            self.change_size(1)
                        m = el[0][:el[0].index('x')]
                        if m == '':
                            m = '1'
                        elif m == '-':
                            m = '-1'
                        if '.' in m:
                            self.change(1, float(m))
                        else:
                            self.change(1, int(m))

    def get_polinom(self):
        return self.polinom

    def get_degree(self):
        return self.degree

    def change(self, m, k):
        self.polinom[m] = k

    def change_size(self, n):
        if n < 0:
            return
        self.degree = n
        if (len(self.polinom) - 1) == n:
            return
        if (len(self.polinom) - 1) < n:
            while (len(self.polinom) - 1) < n:
                self.polinom.append(0)
        else:
            while (len(self.polinom) - 1) > n:
                del self.polinom[-1]


class Input_polinom(QDialog):
    def __init__(self, polinom, m):
        super(Input_polinom, self).__init__()
        self.setWindowTitle("Ввод многочлена")
        self.setFixedSize(QSize(300, 200))
        self.setStyleSheet('background-color: #FAA4A4;')
        self.polinom = polinom
        self.degree_of_polinom = m
        self.flag = False
        self.degree_label = QLabel("Степень", self)
        self.degree_label.move(10, 5)
        self.coef_label = QLabel("Коэффициент при x^k", self)
        self.coef_label.move(80, 5)
        self.polinom_label = QLabel(" " * 300, self)
        self.polinom_label.move(5, 100)
        self.degree = QSpinBox(self)
        self.degree.setRange(0, m)
        self.degree.setSingleStep(1)
        self.degree.move(17, 25)
        self.coef = QLineEdit(self)
        self.coef.move(80, 25)
        self.ok = QPushButton("Сохранить", self)
        self.next = QPushButton("Далее", self)
        self.next.move(100, 175)
        self.ok.move(200, 175)
        self.coef.textEdited.connect(self.change_label_coef)
        self.degree.valueChanged.connect(self.change_label_deg)
        self.next.clicked.connect(self.next_input)
        self.ok.clicked.connect(self.end)

    def change_label_coef(self, text):
        m = self.degree.value()
        self.change_label(text, m)

    def change_label_deg(self, m):
        text = self.coef.text()
        self.change_label(text, m)

    def change_label(self, text, m):
        pol = [el for el in self.polinom.get_polinom()]
        if text != '':
            if text.isdigit() or (text[0] == '-' and text[1:].isdigit()):
                pol[m] = int(text)
            elif ''.join(text.split('.')).isdigit() or (text[0] and ''.join(text.split('.'))[1:].isdigit()):
                pol[m] = float(text)
            elif text == '-':
                pol[m] = -1
        else:
            if self.polinom.get_polinom()[m] == 0:
                pol[m] = 0
        line = []
        for i in range(self.degree_of_polinom, 0, -1):
            if pol[i] == 1:
                if i != 1:
                    line.append(f"x^{i}")
                else:
                    line.append(f"x")
            elif pol[i] != 0:
                if i != 1:
                    line.append(f"{pol[i]}x^{i}")
                else:
                    line.append(f"{pol[i]}x")
        if pol[0] != 0:
            line.append(str(pol[0]))
        line = ' + '.join(line)
        self.polinom_label.setText(line)

    def get_polinom(self):
        return self.polinom

    def next_input(self):
        self.save_polinom()
        self.coef.setText('')
        self.degree.setValue(0)

    def save_polinom(self):
        m = self.degree.value()
        if self.coef.text() == '':
            return
        if self.coef.text().isdigit() or (self.coef.text()[0] == '-' and self.coef.text()[1:].isdigit()):
            self.polinom.change(m, int(self.coef.text()))
        elif ''.join(self.coef.text().split('.')).isdigit() or\
                (self.coef.text()[0] == '-' and ''.join(self.coef.text().split('.'))[1:].isdigit()):
            self.polinom.change(m, float(self.coef.text()))

    def end(self):
        self.save_polinom()
        self.close()


def main():
    app = QApplication(sys.argv)
    style = QStyleFactory.create('Fusion')
    app.setStyle(style)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
