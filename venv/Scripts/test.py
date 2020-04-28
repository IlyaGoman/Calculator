from pythonds.basic.stack import Stack
from string import ascii_letters, digits

# a b c * +
def calc_postFix(expression):
    stack = Stack()
    for operand in expression.split():
        if operand in ascii_letters or operand in digits:
            stack.push(int(operand))
        else:
            stack.push(calc(stack.pop(), stack.pop(), operand))
    print(stack.items)


def calc(x, y, operation):
    dict_calc = {'+': lambda x, y: x + y, \
                 '-': lambda x, y: x - y, \
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    return dict_calc[operation](x, y)


exp = '12 2 3 + *'
calc_postFix(exp)