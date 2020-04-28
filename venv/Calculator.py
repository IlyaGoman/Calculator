from pythonds.basic.stack import Stack
from string import ascii_letters, digits

def infixToPostfix(infixexpr):
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        check_var = check_variable(token)
        if check_var == 'variable':
            postfixList.append(token)
        elif  token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in possible_operation:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
        else:
            print(check_var)
            return ''


    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postFixCalculate(expression):
    stack = Stack()
    for operand in expression.split():
        if operand in ascii_letters:
            stack.push(int(user_dict[operand]))
        elif operand.isdigit():
            stack.push(int(operand))
        else:
            stack.push(calculate(stack.pop(), stack.pop(), operand))
    return stack.items


def calculate(x, y, operation):
    operation = type_operation(operation)
    dict_calc = {'+': lambda x, y: x + y, \
                 '-': lambda x, y: x - y, \
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    return dict_calc[operation](x, y)


def type_operation(operation):
    if '+' in operation or len(operation) % 2 == 0:
        return '+'
    else:
        return '-'


def check_operation(operand):
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


def check_variable(variable, isprint=False):
    if variable.isalpha():
        if variable in user_dict and isprint:
            return user_dict[variable]
        elif variable in user_dict:
            return  'variable'
        else:
            return 'Unknown variable'
    else:
        return 'Invalid identifier'


def exec_command(command):
    if user_in == '/help':
        print('The program calculates the expression')
    elif user_in.startswith('/'):
        print('Unknown command')


def expressionDefine(expression):
    lst, last_operation, result = [], '', 'not answer'

    postfix_expression = infixToPostfix(expression)
    # print(postfix_expression)
    if postfix_expression != '':
        result = postFixCalculate(postfix_expression)

    if result != 'not answer':
        print(result[0])
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
        expressionDefine(string)
    elif string.strip() != '':
        print(check_variable(string, isprint=True))


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
