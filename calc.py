#to be tested

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid operator'
        
def test_add():
    assert calculator(1, 2, '+') == 3

def test_sub():
    assert calculator(2, 1, '-') == 1

def test_mult():
    assert calculator(2, 2, '*') == 4

def test_div():
    assert calculator(2, 1, '/') == 2

def test_fail():
    assert calculator(1, 2, 3) == 'Invalid operator'
