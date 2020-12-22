import factorial.factorial
import exp_root.exponentiation
import exp_root.root
import logarithm.logarithm


def main():

    repeat = True

    while repeat:
        print(50 * '.')
        print('MENU')
        print(50 * '.')
        print(50 * '.')
        print('Select a function from the list: ')
        print(50 * '.')
        print('''1. fact()
2. exp2()
3. exp3()
4. root2()
5. root3()
6. log()
7. ln()
8. lg()''')

        while True:
            try:
                choice = int(input('Enter the function number from the list: '))
                if choice not in range(1, 9):
                    print('Such a function is not in the list!')
                    continue
                break
            except:
                print('Enter the function number as a number!')
                continue

        if choice == 1:
            value = factorial.factorial.input_value()
            print(factorial.factorial.fact(value))
        elif choice == 2:
            value = exp_root.exponentiation.input_value()
            print(exp_root.exponentiation.exp2(value))
        elif choice == 3:
            value = exp_root.exponentiation.input_value()
            print(exp_root.exponentiation.exp3(value))
        elif choice == 4:
            value = exp_root.root.input_value()
            print(exp_root.root.root2(value))
        elif choice == 5:
            value = exp_root.root.input_value()
            print(exp_root.root.root3(value))
        elif choice == 6:
            value_a, value_b = logarithm.logarithm.input_a_b()
            print(logarithm.logarithm.log(value_a, value_b))
        elif choice == 7:
            value_b = logarithm.logarithm.input_b()
            print(logarithm.logarithm.ln(value_b))
        elif choice == 8:
            value_b = logarithm.logarithm.input_b()
            print(logarithm.logarithm.lg(value_b))

        question_repeat = input('Repeat the program? If yes - enter "Y", if not - press ENTER: ').lower()
        if question_repeat == 'y':
            continue
        else:
            break

if __name__ == "__main__":
    main()
