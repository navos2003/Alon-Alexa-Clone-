import re

def to_expression(string):
    if 'plus' in string:
        string = string.replace('plus', '+')
    if 'minus' in string:
        string = string.replace('minus', '+')
    if 'times' in string:
        string = string.replace('times', '*')
    if re.match(r'(divide|divide by)', string):
        string = re.sub(r'(divide|divide by)', '/', string)
    if 'squared' in string:
        string = string.replace('squared', '**2')
    if 'cubed' in string:
        string = string.replace('squared', '**3')
    if 'to the power of' in string:
        string = string.replace('to the power of', '**')
    return string

def calculate(exp):
    try:
        print(f'\n{to_expression(exp)} = {eval(to_expression(exp))}')
    except:
        print('\nCannot calculate this expression')

def text_to_speech(exp):
    try:
        return f'\nThe answer is {eval(to_expression(exp))}.'
    except:
        return '\nI cannot calculate this expression.'
