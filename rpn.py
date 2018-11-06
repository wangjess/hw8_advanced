#!/usr/bin/env python3

import operator
from termcolor import colored # pip install termcolor

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '|': operator.or_,
    '%': operator.mod
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)
        if (result == 0): 
            print("Hallelujah, it's 0!")
        if (result == 10000000): 
            print("You're a billionaire")
        if (result == 103948209324): 
            print("Your result is insane")
        if (result > 0):
            result = colored(result, "red", "on_green")
            print(result)

if __name__ == '__main__':
    main()
