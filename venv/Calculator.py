def type_operation(operation):
    if '+' in operation or len(operation) % 2 == 0:
        return '+'
    else:
        return '-'


def check_input(operand):
    if set(operand) == set('-'): return '-'
    if set(operand) == set('+'): return '+'
    if operand.isdigit() or operand[1:].isdigit(): return 'digits'
    return 'Invalid expression'


def define_variables(variables):
    operands = variables.replace(' ', '').split('=')
    if len(operands) == 2:

        #Invalid identifier
        for i in operands:
            if i.isalpha():
                print('Invalid identifier')

        if variables.count('=') > 1:
            print('Invalid assignment')
    else:
        print('Invalid assignment')


def exec_command(command):
    if user_in == '/help':
        print('The program calculates the sum of numbers')
    elif user_in.startswith('/'):
        print('Unknown command')


def calculate(expression):
    lst, last_operation, result = [], '', 0
    if user_in != '':
        lst = user_in.split()
        for i in range(len(lst)):
            check = check_input(lst[i])
            if check == 'digits':
                if i == 0:
                    result = int(lst[i])
                elif last_operation == '+':
                    result += int(lst[i])
                elif last_operation == '-':
                    result -= int(lst[i])
                else:
                    check = 'Invalid expression'
                    print(check)
                    break
            elif check in possible_operation:
                last_operation = type_operation(lst[i])
            else:
                print(check)
                break

        if check != 'Invalid expression':
            print(result)


def choice_action(string):
    if '=' in string:
        define_variables(string)
    elif '/' in string:
        exec_command(string)
    elif '+' in string or '-' in string:
        calculate(string)
    else:
        pass  # check variable exists and print value


user_dict = {}
user_in = input()
possible_operation = ['+', '-']

while user_in != '':
    choice_action(user_in)

    user_in = input()

print('Bye!')
