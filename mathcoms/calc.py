#!/usr/bin/env python3
from decimal import Decimal, getcontext

## Importing decimal exceptions, so the user can know what goes wrong in ##
## the evaluation of their expression. ##
from decimal import \
     DecimalException, \
     Clamped, \
     InvalidOperation, \
     DivisionByZero, \
     Inexact, \
     Rounded, \
     Subnormal, \
     Overflow, \
     Underflow, \
     ConversionSyntax

from coreutils import setvar
import math
getcontext().prec = 10

def calc(*args):
    exceptionOccured = False
    expression = []
    operatorList = ['+','-','*','/','//','%','**','sqrt','rt']
    for item in args:
        try:
            expression.append(Decimal(item))
        except Exception:
            if item not in operatorList and item.replace('@', '') not in setvar.variables:
                print('Argument {} is not a number'.format(item))
                return
            else:
                pass
        if item[0] == '@':
            realVarName = item.replace('@', '')
            try:
                expression.append(Decimal(setvar.variables[realVarName]))
            except Exception:
                print('Argument {} is not a number'.format(setvar.variables[realVarName]))
                return
        elif item in operatorList:
            expression.append(str(item))
    while len(expression) != 1:
        for item in expression:
            exceptionOccured = False
            try:
                operatorIndex = expression.index(item)
                if item == 'sqrt' or item == 'rt':
                    if item == 'sqrt':
                        radical = expression[operatorIndex + 1]
                        val = Decimal(math.sqrt(float(radical)))
                        expression.insert(expression.index(radical) + 1, val)
                        expression.remove(radical)
                        expression.remove(item)
                    elif item == 'rt':
                        radical = expression[operatorIndex + 1]
                        radicand = expression[operatorIndex - 1]
                        val = Decimal(radical ** Decimal(1/radicand))
                        expression.insert(expression.index(radical) + 1, val)
                        expression.remove(radical)
                        expression.remove(radicand)
                        expression.remove(item)
                elif item == '**':
                    base = expression[operatorIndex - 1]
                    exponent = expression[operatorIndex + 1]
                    val = Decimal(base ** exponent)
                    expression.insert(expression.index(exponent) + 1, val)
                    expression.remove(base)
                    expression.remove(exponent)
                    expression.remove(item)
                elif item == '*':
                    factor1 = expression[operatorIndex - 1]
                    factor2 = expression[operatorIndex + 1]
                    val = Decimal(factor1 * factor2)
                    expression.insert(expression.index(factor2) + 1, val)
                    expression.remove(factor1)
                    expression.remove(factor2)
                    expression.remove(item)
                elif item == '/' or item == '//' or item == '%':
                    if item == '/':
                        dividend = expression[operatorIndex - 1]
                        divisor = expression[operatorIndex + 1]
                        val = Decimal(dividend / divisor)
                        expression.insert(expression.index(divisor) + 1, val)
                        expression.remove(dividend)
                        expression.remove(divisor)
                        expression.remove(item)
                    elif item == '//':
                        dividend = expression[operatorIndex - 1]
                        divisor = expression[operatorIndex + 1]
                        val = Decimal(dividend // divisor)
                        expression.insert(expression.index(divisor) + 1, val)
                        expression.remove(dividend)
                        expression.remove(divisor)
                        expression.remove(item)
                    elif item == '%':
                        dividend = expression[operatorIndex - 1]
                        divisor = expression[operatorIndex + 1]
                        val = Decimal(dividend % divisor)
                        expression.insert(expression.index(divisor) + 1, val)
                        expression.remove(dividend)
                        expression.remove(divisor)
                        expression.remove(item)
                elif item == '+':
                    addend1 = expression[operatorIndex - 1]
                    addend2 = expression[operatorIndex + 1]
                    val = Decimal(addend1 + addend2)
                    expression.insert(expression.index(addend2) + 1, val)
                    expression.remove(addend1)
                    expression.remove(addend2)
                    expression.remove(item)
                elif item == '-':
                    subtractor1 = expression[operatorIndex - 1]
                    subtractor2 = expression[operatorIndex + 1]
                    val = Decimal(subtractor1 - subtractor2)
                    expression.insert(expression.index(subtractor2) + 1, val)
                    expression.remove(subtractor1)
                    expression.remove(subtractor2)
                    expression.remove(item)
            except Overflow:
                print(Decimal('Infinity'))
                exceptionOccured = True
            except Underflow:
                print(Decimal(0))
                exceptionOccured = True
            except InvalidOperation:
                print(Decimal('NaN'))
                exceptionOccured = True
            except DivisionByZero:
                print('Cannot divide by zero.')
                exceptionOccured = True
            except Inexact:
                print('A rounding error has occured')
                exceptionOccured = True
            except Subnormal:
                print('Decimal Subnormal error.')
                exceptionOccured = True
    if not exceptionOccured:
        print(expression[0])
    if exceptionOccured:
        pass
