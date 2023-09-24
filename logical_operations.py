import random

def AND(a, b):
    if a and b == 1:
        output = 1
    else:
        output = 0
    return  output

def OR(a, b):
    if a and b != 1:
        output = 1
    else:
        output = 0
    return output

def NAND(a, b):
    if a and b == 0:
        output = 1
    else:
        output = 0
    return output

def NOR(a, b):
    if a and b == 1:
        output = 1
    else:
        output = 0
    return output

def XOR(a, b):
    if a != b:
        output = 1
    else:
        output = 0
    return output

def COIN(a, b):
    if a == b:
        output = 1
    else:
        output = 0
    return output

def NOT(value):
    if value == 0:
        output = 1
    else:
        output = 0
    return output

def rand_bit():
    random_bit = int(round(random.random(),0))
    return  random_bit

def rand_not(identifier):
    random_bit = int(round(random.random(), 0))
    if random_bit == 1:
        if identifier == 'A':
            identifier = '(A)'
        elif identifier == 'B':
            identifier = '(B)'
        elif identifier == 'C':
            identifier = '(C)'
        elif identifier == 'D':
            identifier = '(D)'
    else:
        identifier = identifier
    return identifier

def table_value_generation():
    value_1 = int(round(random.random(), 0))
    value_2 = int(round(random.random(), 0))
    value_3 = int(round(random.random(), 0))
    value_4 = int(round(random.random(), 0))
    return value_1, value_2, value_3, value_4

def random_logic_operation():
    random_value = random.randrange(1,6)
    if random_value == 1:
        operation = '.'
    elif random_value == 2:
        operation = '+'
    elif random_value == 3:
        operation = '↑'
    elif random_value == 4:
        operation = '↓'
    elif random_value == 5:
        operation = 'Ꚛ'
    else:
        operation = 'Ꙩ'
    return operation

def id_not(label, value):
    num = label.count('(')
    if num != 0:
        value = NOT(value)
    return value

def execute_operation(operator, value_1, value_2):
    if operator == '.':
        output = AND(value_1, value_2)
    elif operator == '+':
        output = OR(value_1, value_2)
    elif operator == '↑':
        output = NAND(value_1, value_2)
    elif operator == '↓':
        output = NOR(value_1, value_2)
    elif operator == 'Ꚛ':
        output = XOR(value_1, value_2)
    else:
        output = COIN(value_1, value_2)
    return output

def len_pad(value_1, value_2, operator,length=9):
    line = value_1 + operator + value_2
    len_in = len(line)
    len_diff = length - len_in
    pad = int(len_diff / 2)
    output = (pad * ' ') + line + (pad * ' ')
    return output

def table_populate():
    a1, a2, a3, a4 = table_value_generation()
    b1, b2, b3, b4 = table_value_generation()
    c1, c2, c3, c4 = table_value_generation()
    d1, d2, d3, d4 = table_value_generation()
    return a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4

def table_operators_generation():
    symbol_1 = random_logic_operation()
    symbol_2 = random_logic_operation()
    symbol_3 = random_logic_operation()
    symbol_4 = random_logic_operation()
    symbol_5 = random_logic_operation()
    return symbol_1, symbol_2, symbol_3, symbol_4, symbol_5

def letter_assign(input):
    repeat = 'yes'
    while repeat == 'yes':
        if input == 1:
            data = random.randrange(2,5)
        elif input == 1:
            data = random.randrange(1,4)
        else:
            data = random.randrange(1, 5)
        if data != input:
            repeat = 'no'
    if data == 1:
        output = 'A'
    elif data == 2:
        output = 'B'
    elif data == 3:
        output = 'C'
    else:
        output = 'D'
    return output

def table_headings(symbol_1, symbol_2, symbol_3, symbol_4, symbol_5):
    v1_1 = rand_not('A')
    v1_2 = rand_not(letter_assign(1))
    v2_1 = rand_not('B')
    v2_2 = rand_not(letter_assign(2))
    v3_1 = rand_not('C')
    v3_2 = rand_not(letter_assign(3))
    v4_1 = rand_not('D')
    v4_2 = rand_not(letter_assign(4))
    v5_1 = random.randrange(1, 5)
    v5_2 = random.randrange(1, 5)
    while v5_1 == v5_2:
        v5_2 = random.randrange(1, 5)
    v5_1 = rand_not(letter_assign(v5_1))
    v5_2 = rand_not(letter_assign(v5_2))
    op1 = len_pad(v1_1 , v1_2,symbol_1)
    op2 = len_pad(v2_1 , v2_2,symbol_2)
    op3 = len_pad(v3_1 , v3_2,symbol_3)
    op4 = len_pad(v4_1 , v4_2,symbol_4)
    op5 = len_pad(v5_1 , v5_2,symbol_5)
    return v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5

def cell_execute(header_1, value_1, header_2, value_2, symbol):
    value_1 = id_not(header_1, value_1)
    value_2 = id_not(header_2, value_2)
    output = execute_operation(symbol, value_1, value_2)
    return output

def get_values(a, b, c, d, header_1, header_2):
    if header_1.count('A') == 1:
        output_1 = a
    elif header_1.count('B') == 1:
        output_1 = b
    elif header_1.count('B') == 1:
        output_1 = c
    else:
        output_1 = d
    if header_2.count('A') == 1:
        output_2 = a
    elif header_2.count('B') == 1:
        output_2 = b
    elif header_2.count('B') == 1:
        output_2 = c
    else:
        output_2 = d
    return output_1, output_2

def row_filler(a, b, c, d, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5):
    v1_1_1, v1_2_1 = get_values(a, b, c, d, v1_1, v1_2)
    v2_1_1, v2_2_1 = get_values(a, b, c, d, v2_1, v2_2)
    v3_1_1, v3_2_1 = get_values(a, b, c, d, v3_1, v3_2)
    v4_1_1, v4_2_1 = get_values(a, b, c, d, v4_1, v4_2)
    v5_1_1, v5_2_1 = get_values(a, b, c, d, v5_1, v5_2)
    o1 = cell_execute(v1_1, v1_1_1, v1_2, v1_2_1, op1)
    o2 = cell_execute(v2_1, v2_1_1, v2_2, v2_2_1, op2)
    o3 = cell_execute(v3_1, v3_1_1, v3_2, v3_2_1, op3)
    o4 = cell_execute(v4_1, v4_1_1, v4_2, v4_2_1, op4)
    o5 = cell_execute(v5_1, v5_1_1, v5_2, v5_2_1, op5)
    return o1, o2, o3, o4, o5

def fill_rows(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5):
    r1a, r1b, r1c, r1d, r1e = row_filler(a1, b1, c1, d1, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5)
    r2a, r2b, r2c, r2d, r2e = row_filler(a2, b2, c2, d2, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5)
    r3a, r3b, r3c, r3d, r3e = row_filler(a3, b3, c3, d3, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5)
    r4a, r4b, r4c, r4d, r4e = row_filler(a4, b4, c4, d4, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5)
    return r1a, r1b, r1c, r1d, r1e, r2a, r2b, r2c, r2d, r2e, r3a, r3b, r3c, r3d, r3e, r4a, r4b, r4c, r4d, r4e

def table_display(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, op1, op2, op3, op4, op5, r1a, r1b, r1c, r1d, r1e, r2a, r2b, r2c, r2d, r2e, r3a, r3b, r3c, r3d, r3e, r4a, r4b, r4c, r4d, r4e):
    blank_spacing = '         '
    blank_row = f'{blank_spacing}║{blank_spacing}║{blank_spacing}║{blank_spacing}║{blank_spacing}'
    top_row = '**Note: Not values are in parenthesis ().**\n╔═══╦═══╦═══╦═══╦═════════╦═════════╦═════════╦═════════╦═════════╗\n'
    top_valued_row = f'║ A ║ B ║ C ║ D ║{op1}║{op2}║{op3}║{op4}║{op5}║\n'
    inter_row = '╠═══╬═══╬═══╬═══╬═════════╬═════════╬═════════╬═════════╬═════════╣\n'
    bottom_row = '╚═══╩═══╩═══╩═══╩═════════╩═════════╩═════════╩═════════╩═════════╝'
    row_1 = f'║ {a1} ║ {b1} ║ {c1} ║ {d1} ║{blank_row}║\n'
    row_2 = f'║ {a2} ║ {b2} ║ {c2} ║ {d2} ║{blank_row}║\n'
    row_3 = f'║ {a3} ║ {b3} ║ {c3} ║ {d3} ║{blank_row}║\n'
    row_4 = f'║ {a4} ║ {b4} ║ {c4} ║ {d4} ║{blank_row}║\n'
    blank_table = f'{top_row}{top_valued_row}{inter_row}{row_1}{inter_row}{row_2}{inter_row}{row_3}{inter_row}{row_4}{bottom_row}'
    filled_row_1 = f'    {r1a}    ║    {r1b}    ║    {r1c}    ║    {r1d}    ║    {r1e}    '
    filled_row_2 = f'    {r2a}    ║    {r2b}    ║    {r2c}    ║    {r2d}    ║    {r2e}    '
    filled_row_3 = f'    {r3a}    ║    {r3b}    ║    {r3c}    ║    {r3d}    ║    {r3e}    '
    filled_row_4 = f'    {r4a}    ║    {r4b}    ║    {r4c}    ║    {r4d}    ║    {r4e}    '
    row_1 = f'║ {a1} ║ {b1} ║ {c1} ║ {d1} ║{filled_row_1}║\n'
    row_2 = f'║ {a2} ║ {b2} ║ {c2} ║ {d2} ║{filled_row_2}║\n'
    row_3 = f'║ {a3} ║ {b3} ║ {c3} ║ {d3} ║{filled_row_3}║\n'
    row_4 = f'║ {a4} ║ {b4} ║ {c4} ║ {d4} ║{filled_row_4}║\n'
    filled_table = f'{top_row}{top_valued_row}{inter_row}{row_1}{inter_row}{row_2}{inter_row}{row_3}{inter_row}{row_4}{bottom_row}'
    return blank_table, filled_table

def blank_table_generation():
    symbol_1, symbol_2, symbol_3, symbol_4, symbol_5 = table_operators_generation()
    a1, a2, a3, a4 = table_value_generation()
    b1, b2, b3, b4 = table_value_generation()
    c1, c2, c3, c4 = table_value_generation()
    d1, d2, d3, d4 = table_value_generation()
    v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5 = table_headings(symbol_1, symbol_2, symbol_3, symbol_4, symbol_5)
    blank_table, filled_table = table_display(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, op1, op2, op3, op4, op5, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    print(blank_table)
    placeholder = input('Press return to continue.')
    return

def filled_table_generation():
    symbol_1, symbol_2, symbol_3, symbol_4, symbol_5 = table_operators_generation()
    a1, a2, a3, a4 = table_value_generation()
    b1, b2, b3, b4 = table_value_generation()
    c1, c2, c3, c4 = table_value_generation()
    d1, d2, d3, d4 = table_value_generation()
    v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, op1, op2, op3, op4, op5 = table_headings(symbol_1, symbol_2, symbol_3, symbol_4, symbol_5)
    r1a, r1b, r1c, r1d, r1e, r2a, r2b, r2c, r2d, r2e, r3a, r3b, r3c, r3d, r3e, r4a, r4b, r4c, r4d, r4e = fill_rows(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3, a4, b4, c4, d4, v1_1, v1_2, v2_1, v2_2, v3_1, v3_2, v4_1, v4_2, v5_1, v5_2, symbol_1, symbol_2, symbol_3, symbol_4, symbol_5)
    blank_table, filled_table = table_display(a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4, op1, op2, op3, op4, op5, r1a, r1b, r1c, r1d, r1e, r2a, r2b, r2c, r2d, r2e, r3a, r3b, r3c, r3d, r3e, r4a, r4b, r4c, r4d, r4e)
    print(blank_table)
    placeholder = input('Press return when you are ready to check your answers.\n')
    print(filled_table)
    placeholder = input('Press return when you are continue.\n')
    return

def single_operation():
    value_1 = int(round(random.random(), 0))
    value_2 = int(round(random.random(), 0))
    label_1 = rand_not('A')
    label_2 = rand_not('B')
    symbol = random_logic_operation()
    value_1a = id_not(label_1, value_1)
    value_2a = id_not(label_2, value_2)
    result = execute_operation(symbol, value_1a, value_2a)
    print('** Note: Labels in parenthesis are NOT. **')
    print(f'''Please solve where:
    A = {value_1}
    B = {value_2}
    {label_1} {symbol} {label_2}''')
    answer = input('Please enter your answer: ')
    if str(answer) == str(result):
        print('Correct.')
    else:
        print(f'The correct answer was: {result}.')
    return