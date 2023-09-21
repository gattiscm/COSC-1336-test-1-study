import random

###############################################################################
# Program: COSC-1336 Test I Study Program                                     #
# Author: C. Gattis                                                           #
# Release: 1.0                                                                #
# Date: 20 September 2023                                                     #
###############################################################################

class numbersystems:
    # Class to accumulate functions associated with section one, number systems.
    def __init__(self, value):
        self.value = value

    def initialize_values():
        number_1 = 0
        number_1_binary = 0
        number_1_hex = 0
        number_2 = 0
        number_2_binary = 0
        number_2_hex = 0
        minimum_value = 16
        maximum_value = 255
        return number_1, number_1_binary, number_1_hex, number_2, number_2_binary, \
            number_2_hex, minimum_value, maximum_value

    def DecimaltoBinary(n):
        # Function to convert a decimal to binary and strip the leading digraph.
        return bin(n).replace("0b", "")

    def Hexify(n):
        # Function to convert a decimal to hexadecimal and strip the leading digraph.
        return str.upper(hex(n).replace('0x', ''))

    def random_number(lower,upper):
        # Function generates a random value between lower and upper limits.
        decimal_number = random.randrange(lower,upper)
        return decimal_number

    def random_operation():
        # Function generates a random value between zero and one. Depending on
        # the result, one of four operations will be returned.
        random_value = random.random()
        if random_value < 0.35:
            operation = 'addition'
        elif random_value < 0.7:
            operation = 'subtraction'
        elif random_value < 0.75:
            operation = 'shift-left operations'
        elif random_value < 0.8:
            operation = 'shift-right operations'
        else:
            operation = 'convert'
        return operation

    def parse_number(value):
        # Function that utilizes two functions to convert number bases.
        binary_value = numbersystems.DecimaltoBinary(value)
        hex_value = numbersystems.Hexify(value)
        return value, binary_value, hex_value

    def random_data_type(in_type):
        # Generates a random value and returns a data type based on result.
        random_number = random.random()
        if in_type == 'convert':
            if random_number < (1 / 3):
                type = 'decimal'
            elif random_number < (2 / 3):
                type = 'binary'
            else:
                type = 'hexadecimal'
        else:
            if random_number < 0.5:
                type = 'binary'
            else:
                type = 'hexadecimal'
        return type

    def conversions(value):
        # Function which accumulates other functions into a number conversion tester.
        value, binary_value, hex_value = numbersystems.parse_number(value)
        initial_type = numbersystems.random_data_type('convert')
        result_type = numbersystems.random_data_type('convert')
        while initial_type == result_type:
            result_type = numbersystems.random_data_type('convert')
        if initial_type == 'binary':
            initial_value = numbersystems.DecimaltoBinary(value)
        elif initial_type == 'hexadecimal':
            initial_value = numbersystems.Hexify(value)
        else:
            initial_value = value
        if result_type == 'binary':
            result_value = numbersystems.DecimaltoBinary(value)
        elif result_type == 'hexadecimal':
            result_value = numbersystems.Hexify(value)
        else:
            result_value = value
        line = f'Please convert {initial_value} from {initial_type} to {result_type}.\nPress return when done for the answer.'
        print(line)
        placeholder = input()
        print(result_value)
        placeholder = input('Press return to continue.')
        return

    def addition(minimum_value, maximum_value):
        # Takes input of multiple values for a result.
        data_type = numbersystems.random_data_type('addition')
        number_additives = random.randrange(2,3)
        value_1 = numbersystems.random_number(minimum_value, maximum_value)
        value_2 = numbersystems.random_number(minimum_value, maximum_value)
        result = value_1 + value_2
        if data_type == 'binary':
            value_1 = numbersystems.DecimaltoBinary(value_1)
            value_2 = numbersystems.DecimaltoBinary(value_2)
        else:
            value_1 = numbersystems.Hexify(value_1)
            value_2 = numbersystems.Hexify(value_2)
        if number_additives > 2:
            value_3 = numbersystems.random_number(minimum_value, maximum_value)
            result = result + value_3
            if data_type == 'binary':
                value_3 = numbersystems.DecimaltoBinary(value_3)
            else:
                value_3 = numbersystems.Hexify(value_3)
            print(f'{value_1} + {value_2} + {value_3} = ({data_type}')
            placeholder = input('Press return to see answer.')
        else:
            print(f'{value_1} + {value_2} = ({data_type})')
            placeholder = input('Press return to see answer.')
        if data_type == 'binary':
            result = numbersystems.DecimaltoBinary(result)
        else:
            result = numbersystems.Hexify(result)
        print(result)
        placeholder = input('Press return to continue.')
        return

    def subtraction(minimum_value, maximum_value):
        # Takes input of multiple values for a result.
        data_type = numbersystems.random_data_type('subtraction')
        value_01 = numbersystems.random_number(minimum_value, maximum_value)
        value_02 = numbersystems.random_number(minimum_value, maximum_value)
        value_1 = max(value_01, value_02)
        value_2 = min(value_01, value_02)
        result = value_1 - value_2
        if data_type == 'binary':
            value_1 = numbersystems.DecimaltoBinary(value_1)
            value_2 = numbersystems.DecimaltoBinary(value_2)
        else:
            value_1 = numbersystems.Hexify(value_1)
            value_2 = numbersystems.Hexify(value_2)
        print(f'{value_1} - {value_2} = ({data_type})')
        placeholder = input('Press return to see answer.')
        if data_type == 'binary':
            result = numbersystems.DecimaltoBinary(result)
        else:
            result = numbersystems.Hexify(result)
        print(result)
        placeholder = input('Press return to continue.')
        return

    def shift_left(minimum_value, maximum_value):
        # Function to multiply binary numbers by two.
        value = numbersystems.random_number(minimum_value, maximum_value)
        result = value * 2
        value = numbersystems.DecimaltoBinary(value)
        result = numbersystems.DecimaltoBinary(int(result))
        placeholder = input(f'Perform shift-left operations on {value}. Press return to view answer.')
        print(result)
        placeholder = input('')
        return

    def shift_right(minimum_value, maximum_value):
        # Function to divide binary numbers by two.
        value = numbersystems.random_number(minimum_value, maximum_value) * 2
        result = value / 2
        value = numbersystems.DecimaltoBinary(value)
        result = numbersystems.DecimaltoBinary(int(result))
        placeholder = input(f'Perform shift-right operations on {value}. Press return to view answer.')
        print(result)
        placeholder = input('')
        return

    def perform_random_operation(minimum_value, maximum_value):
        # Function that utilizes numbersystems class to generate random numbers,
        # generate random operation types, and display operations and values.
        operation = numbersystems.random_operation()
        value = numbersystems.random_number(minimum_value, maximum_value)
        number_1, number_1_binary, number_1_hex = numbersystems.parse_number(value)
        if operation != 'shift-right operations' or 'shift-left-operations' or 'convert':
            value = numbersystems.random_number(minimum_value, maximum_value)
            number_2, number_2_binary, number_2_hex = numbersystems.parse_number(value)
        else:
            pass
        if operation == 'convert':
            numbersystems.conversions(value)
        elif operation == 'addition':
            numbersystems.addition(minimum_value, maximum_value)
        elif operation == 'subtraction':
            numbersystems.subtraction(minimum_value, maximum_value)
        elif operation == 'shift-left operations':
            numbersystems.shift_left(minimum_value, maximum_value)
        elif operation == 'shift-right operations':
            numbersystems.shift_right(minimum_value, maximum_value)
        return

def main():
    # Main function loop.
    number_of_operations = 5
    number_1, number_1_binary, number_1_hex, number_2, number_2_binary, \
        number_2_hex, minimum_value, maximum_value = numbersystems.initialize_values()
    print('''Main menu.
What type of number system operation would you like to practice?
1. Conversions
2. Addition
3. Subtraction
4. Shift-Left Operations
5. Shift-Right Operations
6. Random operations.
Any other number to exit.''')
    desired_operation = input()
    if int(desired_operation) < 7:
        number_of_operations = input('How many operations would you like to practice?\nOr press return for a default of five.')
    if number_of_operations == '':
        number_of_operations = 5
    else:
        number_of_operations = int(number_of_operations)
    if desired_operation == '1':
        while number_of_operations > 0:
            value = numbersystems.random_number(64, 65535)
            numbersystems.conversions(value)
            number_of_operations -= 1
    elif desired_operation == '2':
        while number_of_operations > 0:
            numbersystems.addition(minimum_value, maximum_value)
            number_of_operations -= 1
    elif desired_operation == '3':
        while number_of_operations > 0:
            numbersystems.subtraction(minimum_value, maximum_value)
            number_of_operations -= 1
    elif desired_operation == '4':
        while number_of_operations > 0:
            numbersystems.shift_left(minimum_value, maximum_value)
            number_of_operations -= 1
    elif desired_operation == '5':
        while number_of_operations > 0:
            numbersystems.shift_right(minimum_value, maximum_value)
            number_of_operations -= 1
    elif desired_operation == '6':
        while number_of_operations > 0:
            numbersystems.perform_random_operation(minimum_value, maximum_value)
            number_of_operations -= 1
    else:
        exit()

while __name__ == '__main__':
    main()