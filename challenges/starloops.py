#!/usr/bin/env python3
def main():
        global symbol
        symbol = input("please enter single letter or number ")
        display(symbol)

def display(symbol):
        array= []
        for x in range(0, 5):
                array.append(symbol)
                print(" ".join(array))

        for y in range(len(array), 1, -1):
                array.pop()
                print(" ".join(array))
main()
display("3")
