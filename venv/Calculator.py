from pythonds.basic.stack import Stack
from string import ascii_letters, digits

def infixToPostfix(infixexpr):
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.replace('(', '( ').replace(')', ' )').split()

    for token in tokenList:
        if token in ascii_letters or token in digits:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def type_operation(operation):
    if '+' in operation or len(operation) % 2 == 0:
        return '+'
    else:
        return '-'


def check_input(operand):
    if set(operand) == set('-'): return '-'
    if set(operand) == set('+'): return '+'
    if operand.isdigit() or operand[1:].isdigit(): return 'digits'
    if operand.isalpha():
        if operand in user_dict:
            return 'variable'
        else:
            return 'Unknown variable'

    return 'Invalid expression'


def define_variables(variables):
    operands = variables.replace(' ', '').split('=')
    if len(operands) == 2:
        if operands[0].isalpha():
            if operands[1].isdigit(): # define variable and assigment numbers
                user_dict[operands[0]] = operands[1]
            elif operands[1].isalpha() and operands[1] in user_dict: # define variable and assigment variable
                user_dict[operands[0]] = user_dict[operands[1]]
            elif operands[1].isalpha() and operands[1] not in user_dict: # unknown variable
                print('Unknown variable')
            else:
                print('Invalid assignment')
        else:
            print('Invalid identifier')
    else:
        print('Invalid assignment')


def check_variable(variable):
    if variable.isalpha():
        if variable in user_dict:
            print(user_dict[variable])
        else:
            print('Unknown variable')
    else:
        print('Invalid identifier')


def exec_command(command):
    if user_in == '/help':
        print('The program calculates the expression')
    elif user_in.startswith('/'):
        print('Unknown command')


def calculate(expression):
    lst, last_operation, result = [], '', 0

    postfix_expression = infixToPostfix(expression)
    print(postfix_expression)
    '''
    lst = expression.split()    
    for idx, item in enumerate(lst):
        check = check_input(item)
        if check == 'digits':
            if idx == 0:
                result = int(item)
            elif last_operation == '+':
                result += int(item)
            elif last_operation == '-':
                result -= int(item)
            else:
                check = 'Invalid expression'
                print(check)
                break
        elif check == 'variable':
            if idx == 0:
                result = int(user_dict[item])
            elif last_operation == '+':
                result += int(user_dict[item])
            elif last_operation == '-':
                result -= int(user_dict[item])
            else:
                check = 'Invalid expression'
                print(check)
                break

        elif check in possible_operation:
            last_operation = type_operation(item)
        else:
            print(check)
            break

    if check != 'Invalid expression':
        print(result)
    '''


def choice_action(string):
    if '=' in string:
        define_variables(string)
    elif '/' in string:
        exec_command(string)
    elif '+' in string or '-' in string:
        calculate(string)
    elif string.strip() != '':
        check_variable(string)


def prec_define():
    global prec
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

# Initialisation program variables
user_dict = {}
user_in = input()
possible_operation = ['+', '-', '*', '/']
prec = {}
prec_define()


while user_in != '/exit':
    choice_action(user_in)
    user_in = input()

print('Bye!')
