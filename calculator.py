'''This module equals calculator program'''

from string import ascii_letters

def infix_to_postfix(infixexpr):
    '''
    Convert infix expression in postfix notation
    :param infixexpr:
    :return:
    '''
    op_stack = []
    postfix_list = []
    token_list = infixexpr.split()

    for token in token_list:
        check_var = check_variable(token)
        if check_var == 'variable':
            postfix_list.append(token)
        elif  token.isdigit():
            postfix_list.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        elif token in possible_operation:
            while len(op_stack) > 0 and (prec[op_stack[-1]] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.append(token)
        else:
            print(check_var)
            return ''


    while len(op_stack) > 0:
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def postfix_calculate(expression):
    '''
    Calculate expression in postfix notation
    :param expression:
    :return:
    '''
    stack = []
    for operand in expression.split():
        if operand in ascii_letters:
            stack.append(int(user_dict[operand]))
        elif operand.isdigit():
            stack.append(int(operand))
        else:
            stack.append(calculate(stack.pop(), stack.pop(), operand))
        # print(stack.items)
    return stack


def calculate(x, y, operation):
    '''
    Calculate basic operation allow in program
    :param x:
    :param y:
    :param operation:
    :return:
    '''
    dict_calc = {'+': lambda x, y: x + y, \
                 '-': lambda x, y: y - x, \
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: y / x}
    return dict_calc[operation](x, y)


def define_variables(variables):
    operands = variables.replace(' ', '').split('=')
    if len(operands) == 2:
        if operands[0].isalpha():
            if operands[1].isdigit(): # define variable and assigment numbers
                user_dict[operands[0]] = operands[1]
            elif operands[1].isalpha() and operands[1] in user_dict:
                user_dict[operands[0]] = user_dict[operands[1]]
            elif operands[1].isalpha() and operands[1] not in user_dict: # unknown variable
                print('Unknown variable')
            else:
                print('Invalid assignment')
        else:
            print('Invalid identifier')
    else:
        print('Invalid assignment')


def check_variable(variable, isprint=False):
    if variable.isalpha():
        if variable in user_dict and isprint:
            return user_dict[variable]
        elif variable in user_dict:
            return  'variable'
        else:
            return 'Unknown variable'
    elif isprint and (variable.isdigit() or variable[1:].isdigit()):
        return variable
    else:
        return 'Invalid identifier'


def exec_command(command):
    if command == '/help':
        print('The program calculates the expression')
    elif command.startswith('/'):
        print('Unknown command')


def expression_define(expression):
    postfix_expression = infix_to_postfix(expression)
    if postfix_expression != '':
        result = postfix_calculate(postfix_expression)
    if result != 'not answer':
        print(int(result[0]))

def choice_action(string):
    if '=' in string:
        define_variables(string)
    elif string.startswith('/'):
        exec_command(string)
    elif '+' in string or '-' in string[1:] or '/' in string or '*' in string:
        expression = parse_expression(string)
        if check_invalid_expression(expression):
            expression_define(expression)
    elif string.strip() != '':
        print(check_variable(string, isprint=True))


def parse_expression(expression):
    # expression = expression.replace(' ', '')
    dict_replace = {'---': '-', \
                    '--': '+', \
                    '+++': '+'}
    for key, value in dict_replace.items():
        expression = expression.replace(key, value)
    if ' ' not in expression:
        return ' '.join(expression)
    return expression.replace('(', '( ').replace(')', ' )')

def check_invalid_expression(expression):
    if expression.count('(') != expression.count(')') or \
        expression.count('**') > 0 or expression.count('//') > 0:
        print('Invalid expression')
        return False
    return True


# Initialisation program variables
user_dict = {}
user_in = input()
possible_operation = ['+', '-', '*', '/']
prec = {'^': 4,
        '*': 3, '/': 3,
        '+': 2, '-': 2,
        '(': 1}


while user_in != '/exit':
    choice_action(user_in)

    user_in = input()

print('Bye!')
