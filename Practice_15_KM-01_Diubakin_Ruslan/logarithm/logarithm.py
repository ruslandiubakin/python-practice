import math


def input_a_b():
    is_not_valid = True
    while is_not_valid:
        try:
            value_a = int(input('Enter the value of the base of the logarithm: '))
            if value_a <= 0 or value_a == 1:
                print('You have entered an invalid logarithm base value!')
                continue
            value_b = float(input('Enter the number for the logarithm: '))
            if value_b < 0:
                print('You have entered a negative value!')
                continue
            return value_a, value_b
        except:
            print('You did not enter a numeric value!')
            continue


def input_b():
    is_not_valid = True
    while is_not_valid:
        try:
            value_b = float(input('Enter the number for the logarithm: '))
            if value_b < 0:
                print('You have entered a negative value!')
                continue
            return value_b
        except:
            print('You did not enter a numeric value!')
            continue


def log(a, b):
    return math.log(b, a)


def ln(b):
    return math.log(b)


def lg(b):
    return math.log(b, 10)