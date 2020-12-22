def input_value():
    is_not_valid = True
    while is_not_valid:
        try:
            value = float(input('Enter number: '))
            if value < 0:
                print('You have entered a negative value!')
                continue
            return value
        except:
            print('You did not enter a numeric value!')
            continue


def root2(value):
    return value ** 0.5


def root3(value):
    return value ** (1 / 3)