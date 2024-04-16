import os
import sys
from string import *

operator = ['^', '*', '/', '+', '-']


def solve(equation):
    """Receives the final list and solves the arithmetic problem"""
    alphabet = list(ascii_lowercase)
    alpha_error = False

    # This loop detects any Alphabet in the equation and returns an Error Message to the User
    for equ in equation:
        if equ in alphabet:
            alpha_error = True

    if alpha_error:
        return print("\nThe Equation contains a letter. \nRewrite your Equation.")
    else:
        spaces(equation)

        full_stop(equation)

        raised_to_pow(equation)

        division(equation)

        multiplication(equation)

        subtraction(equation)

        addition(equation)

        calculator = 0
        for equ in equation:
            if equ in operator:
                solve(equation)
        for equ in equation:
            calculator += float(equ)
        return calculator


def spaces(values):
    """This function detects any unused spaces in the values and deletes it"""
    for equ in values:
        if equ == " ":
            space_pos = values.index(" ")
            del values[space_pos]


def full_stop(values):
    """This function detects any decimal point in the values and merges the values beside it to form a decimal
    number"""
    for equ in values:
        if equ == ".":
            decimal_position = values.index(".")
            value_merge = [values[decimal_position - 1], values[decimal_position],
                           values[decimal_position + 1]]
            decimal_val = "".join(value_merge)
            del values[decimal_position - 1:decimal_position + 2]
            values.insert(decimal_position - 1, decimal_val)


def raised_to_pow(values):
    """This function solves the exponential problems in the values"""
    for equ in values:
        if equ == "^":
            exponential_position = values.index("^")
            exponential_solved = float(values[exponential_position - 1]) ** float(
                values[exponential_position + 1])
            del values[exponential_position - 1:exponential_position + 2]
            values.insert(exponential_position - 1, str(exponential_solved))


def division(values):
    """This functions solves the division problems in the values"""
    for equ in values:
        if equ == "/":
            division_position = values.index("/")
            try:
                division_solved = float(values[division_position - 1]) / float(values[division_position + 1])
            except ZeroDivisionError:
                print("\nA Number can't be Divisible by Zero!\n")
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                del values[division_position - 1:division_position + 2]
                values.insert(division_position - 1, str(division_solved))


def multiplication(values):
    """This function solves the multiplication problems in the values"""
    for equ in values:
        if equ == "*":
            multi_position = values.index("*")
            multi_solved = float(values[multi_position - 1]) * float(values[multi_position + 1])
            del values[multi_position - 1:multi_position + 2]
            values.insert(multi_position - 1, str(multi_solved))


def subtraction(values):
    """This function merges the subtraction problems to the values"""
    for equ in values:
        if equ == "-":
            subtract_position = values.index("-")
            subtract_merge = [values[subtract_position], values[subtract_position + 1]]
            del values[subtract_position:subtract_position + 2]
            values.insert(subtract_position, "".join(subtract_merge))
            del subtract_merge[:]


def addition(values):
    """This function merges the addition problems to the values"""
    for equ in values:
        if equ == "+":
            add_position = values.index("+")
            add_merge = [values[add_position], values[add_position + 1]]
            del values[add_position:add_position + 2]
            values.insert(add_position, "".join(add_merge))
            del add_merge[:]

