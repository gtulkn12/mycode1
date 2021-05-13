#!/usr/bin/env python3
from os import closerange
import operator

def main():
        global operations, operation, num1, num2
        operations= {
        "+" : operator.add,
        "-" : operator.sub,
        "/" : operator.truediv,
        "*" : operator.mul}

        valid= False
        while valid is False:
                try:
                        operation= (input("Please enter operation? ")).lower().strip()
                        if operation not in operations.keys():
                            print("That's not a valid operation.")
                            continue
                        num1= float(input("Please enter 1st number: "))
                        num2= float(input("Please enter 2nd number: "))
                        valid= True
                except ValueError:
                        print("Please enter a valid number: ex. 4 or 4.0 ")

        for elm in operations:
                if elm == operation:
                        print(calc1(num1, num2, elm))

def calc1 (num1, num2, operator):
        solution = operations[operator](num1, num2)
        return solution
main()
