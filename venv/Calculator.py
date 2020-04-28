from string import ascii_letters, digits

def infixToPostfix(infixexpr):
    opStack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        check_var = checkVariable(token)
        if check_var == 'variable':
            postfixList.append(token)
        elif  token.isdigit():
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        elif token in possible_operation:
            while len(opStack) > 0 and \
               (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)
        else:
            print(check_var)
            return ''


    while len(opStack) > 0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def postFixCalculate(expression):
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
    dict_calc = {'+': lambda x, y: x + y, \
                 '-': lambda x, y: y - x, \
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: y / x}
    return dict_calc[operation](x, y)


# def type_operation(operation):
#     if '+' in operation or len(operation) % 2 == 0:
#         return '+'
#     else:
#         return '-'


# def check_operation(operand):
#     if set(operand) == set('-'): return '-'
#     if set(operand) == set('+'): return '+'
#     if operand.isdigit() or operand[1:].isdigit(): return 'digits'
#     if operand.isalpha():
#         if operand in user_dict:
#             return 'variable'
#         else:
#             return 'Unknown variable'
#
#     return 'Invalid expression'


def defineVariables(variables):
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


def checkVariable(variable, isprint=False):
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


def execCommand(command):
    if user_in == '/help':
        print('The program calculates the expression')
    elif user_in.startswith('/'):
        print('Unknown command')


def expressionDefine(expression):
    postfix_expression = infixToPostfix(expression)
    if postfix_expression != '':
        result = postFixCalculate(postfix_expression)
    if result != 'not answer':
        print(int(result[0]))
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


def choiceAction(string):
    if '=' in string:
        defineVariables(string)
    elif string.startswith('/'):
        execCommand(string)
    elif '+' in string or '-' in string[1:] or '/' in string or '*' in string:
        expression = parseExpression(string)
        if checkInvalidExpression(expression):
            expressionDefine(expression)
    elif string.strip() != '':
        print(checkVariable(string, isprint=True))


def parseExpression(expression):
    # expression = expression.replace(' ', '')
    dict_replace = {'---': '-', \
                    '--': '+', \
                    '+++': '+'}
    for key, value in dict_replace.items():
        expression = expression.replace(key, value)
    # return ' '.join([i for i in expression])
    return expression.replace('(', '( ').replace(')', ' )')

def checkInvalidExpression(expression):
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
        '*': 3,'/': 3,
        '+': 2, '-': 2,
        '(': 1}


while user_in != '/exit':
    choiceAction(user_in)

    user_in = input()

print('Bye!')
