def input_value():
    is_not_valid = True
    while is_not_valid:
        try:
            value = float(input('Enter number: '))
            return value
        except:
            print('You did not enter a numeric value!')
            continue


def exp2(value):
    return value ** 2


def exp3(value):
    return value ** 3
