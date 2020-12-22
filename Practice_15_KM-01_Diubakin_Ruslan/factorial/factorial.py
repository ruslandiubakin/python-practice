def input_value():
    is_not_valid = True
    while is_not_valid:
        try:
            value = int(input('Enter a natural number: '))
            if value <= 0:
                print('You did not enter a natural number. Enter a number greater than zero!')
                continue
            return value
        except:
            print('You did not enter a numeric value!')
            continue


def fact(value):
    if value == 0:
        return 1
    else:
        return(value * fact(value - 1))