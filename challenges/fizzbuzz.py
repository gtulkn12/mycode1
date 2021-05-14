#!/usr/bin/env python3
def fizzBuzz(x, y):
        for number in range(x, y):
                if number % 15 == 0:
                        print("FizzBuzz")
                elif number % 3 is 0:
                        print("Fizz")
                elif number % 5 is 0:
                        print("Buzz")
                else:
                        print(number)

fizzBuzz(1, 101)
