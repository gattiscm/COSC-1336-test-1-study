import logical_operations
import number_systems

###############################################################################
# Program: COSC-1336 Test I Study Program                                     #
# Author: C. Gattis                                                           #
# Release: 1.1.1                                                                #
# Date: 25 September 2023                                                     #
###############################################################################

def numbersystems_menu(number_of_operations):
    # Menu for number systems operations. For information on functions from here,
    # see number_systems.py
    number_1, number_1_binary, number_1_hex, number_2, number_2_binary, \
        number_2_hex, minimum_value, maximum_value = number_systems.initialize_values()
    loop = 'yes'
    while loop == 'yes':
        print('''Number systems submenu.
    What type of number system operation would you like to practice?
    1. Conversions
    2. Addition
    3. Subtraction
    4. Shift-Left Operations
    5. Shift-Right Operations
    6. Random Operations.
    99. Main Menu.''')
        desired_operation = input()
        if int(desired_operation) < 7:
            number_of_operations = input('How many operations would you like to practice?\nOr press return for a default of five.')
        if number_of_operations == '':
            number_of_operations = 5
        else:
            number_of_operations = int(number_of_operations)
        if desired_operation == '1':
            while number_of_operations > 0:
                value = number_systems.random_number(64, 65535)
                number_systems.conversions(value)
                number_of_operations -= 1
        elif desired_operation == '2':
            while number_of_operations > 0:
                number_systems.addition(minimum_value, maximum_value)
                number_of_operations -= 1
        elif desired_operation == '3':
            while number_of_operations > 0:
                number_systems.subtraction(minimum_value, maximum_value)
                number_of_operations -= 1
        elif desired_operation == '4':
            while number_of_operations > 0:
                number_systems.shift_left(minimum_value, maximum_value)
                number_of_operations -= 1
        elif desired_operation == '5':
            while number_of_operations > 0:
                number_systems.shift_right(minimum_value, maximum_value)
                number_of_operations -= 1
        elif desired_operation == '6':
            while number_of_operations > 0:
                number_systems.perform_random_operation(minimum_value, maximum_value)
                number_of_operations -= 1
        elif desired_operation == '99':
            loop = 'no'
            break
        else:
            print('Invalid Entry.')
    return

def logic_menu():
    # Menu for logic operations. For information on functions from here,
    # see logic_operations.py
    loop = 'yes'
    while loop == 'yes':
        print('''Number systems submenu.
What type of number system operation would you like to practice?
1. Individual Logic Question and Answer
2. Logic Tables
99. Main Menu''')
        selection = input('Please enter a selection.\n')
        if selection == '1':
            number_of_operations = int(input('How many questions would you like?\n'))
            while number_of_operations > 0:
                logical_operations.single_operation()
                number_of_operations -= 1
        elif selection == '2':
            logical_operations.filled_table_generation()
        elif selection == '99':
            loop = 'no'
            break
        else:
            print('Invalid entry.')
            continue
    return

def main():
    # Main function loop, acts as a menu.
    loop = 'yes'
    number_of_operations = 5
    while loop == 'yes':
        print('COSC-1336-73246 Test I Study script.\nMain Menu.\n1.Number Systems\n2. Logic Operations\n3. Exit')
        value = input('Please enter a selection.\n')
        if value == '1':
            numbersystems_menu(number_of_operations)
        elif value == '2':
            logic_menu()
        elif value == '3' or '99':
            exit()
        else:
            print('Invalid Entry')
            continue
    return

while __name__ == '__main__':
    main()