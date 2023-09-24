import random

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


def random_number(lower, upper):
    # Function generates a random value between lower and upper limits.
    decimal_number = random.randrange(lower, upper)
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
    binary_value = DecimaltoBinary(value)
    hex_value = Hexify(value)
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
    value, binary_value, hex_value = parse_number(value)
    initial_type = random_data_type('convert')
    result_type = random_data_type('convert')
    while initial_type == result_type:
        result_type = random_data_type('convert')
    if initial_type == 'binary':
        initial_value = DecimaltoBinary(value)
    elif initial_type == 'hexadecimal':
        initial_value = Hexify(value)
    else:
        initial_value = value
    if result_type == 'binary':
        result_value = DecimaltoBinary(value)
    elif result_type == 'hexadecimal':
        result_value = Hexify(value)
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
    data_type = random_data_type('addition')
    number_additives = random.randrange(2, 3)
    value_1 = random_number(minimum_value, maximum_value)
    value_2 = random_number(minimum_value, maximum_value)
    result = value_1 + value_2
    if data_type == 'binary':
        value_1 = DecimaltoBinary(value_1)
        value_2 = DecimaltoBinary(value_2)
    else:
        value_1 = Hexify(value_1)
        value_2 = Hexify(value_2)
    if number_additives > 2:
        value_3 = random_number(minimum_value, maximum_value)
        result = result + value_3
        if data_type == 'binary':
            value_3 = DecimaltoBinary(value_3)
        else:
            value_3 = Hexify(value_3)
        print(f'{value_1} + {value_2} + {value_3} = ({data_type}')
        placeholder = input('Press return to see answer.')
    else:
        print(f'{value_1} + {value_2} = ({data_type})')
        placeholder = input('Press return to see answer.')
    if data_type == 'binary':
        result = DecimaltoBinary(result)
    else:
        result = Hexify(result)
    print(result)
    placeholder = input('Press return to continue.')
    return


def subtraction(minimum_value, maximum_value):
    # Takes input of multiple values for a result.
    data_type = random_data_type('subtraction')
    value_01 = random_number(minimum_value, maximum_value)
    value_02 = random_number(minimum_value, maximum_value)
    value_1 = max(value_01, value_02)
    value_2 = min(value_01, value_02)
    result = value_1 - value_2
    if data_type == 'binary':
        value_1 = DecimaltoBinary(value_1)
        value_2 = DecimaltoBinary(value_2)
    else:
        value_1 = Hexify(value_1)
        value_2 = Hexify(value_2)
    print(f'{value_1} - {value_2} = ({data_type})')
    placeholder = input('Press return to see answer.')
    if data_type == 'binary':
        result = DecimaltoBinary(result)
    else:
        result = Hexify(result)
    print(result)
    placeholder = input('Press return to continue.')
    return


def shift_left(minimum_value, maximum_value):
    # Function to multiply binary numbers by two.
    value = random_number(minimum_value, maximum_value)
    result = value * 2
    value = DecimaltoBinary(value)
    result = DecimaltoBinary(int(result))
    placeholder = input(f'Perform shift-left operations on {value}. Press return to view answer.')
    print(result)
    placeholder = input('')
    return


def shift_right(minimum_value, maximum_value):
    # Function to divide binary numbers by two.
    value = random_number(minimum_value, maximum_value) * 2
    result = value / 2
    value = DecimaltoBinary(value)
    result = DecimaltoBinary(int(result))
    placeholder = input(f'Perform shift-right operations on {value}. Press return to view answer.')
    print(result)
    placeholder = input('')
    return


def perform_random_operation(minimum_value, maximum_value):
    # Function that utilizes numbersystems class to generate random numbers,
    # generate random operation types, and display operations and values.
    operation = random_operation()
    value = random_number(minimum_value, maximum_value)
    number_1, number_1_binary, number_1_hex = parse_number(value)
    if operation != 'shift-right operations' or 'shift-left-operations' or 'convert':
        value = random_number(minimum_value, maximum_value)
        number_2, number_2_binary, number_2_hex = parse_number(value)
    else:
        pass
    if operation == 'convert':
        conversions(value)
    elif operation == 'addition':
        addition(minimum_value, maximum_value)
    elif operation == 'subtraction':
        subtraction(minimum_value, maximum_value)
    elif operation == 'shift-left operations':
        shift_left(minimum_value, maximum_value)
    elif operation == 'shift-right operations':
        shift_right(minimum_value, maximum_value)
    return