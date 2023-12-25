#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
            

def square_integers(int_list):
    # code goes here!
    square_list = []
    for x in int_list:
        square_list.append(x * x)
    return square_list

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        is_multiple_of_3 = "Fizz" if i % 3 == 0 else ""
        is_multiple_of_5 = "Buzz" if i % 5 == 0 else ""
        if not (is_multiple_of_3 or is_multiple_of_5):
            print(i)
        else:
            print(str(is_multiple_of_3 + is_multiple_of_5))
        
