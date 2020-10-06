'''
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
With a given integral number n, write a program to generate a dictionary 
that contains (i, i*i) such that is an integral number between 1 and n 
(both included). and then the program should print the dictionar'''

def calculate_square(number):
    square = number * number
    return square

def print_square():
    square_dictionary = {}
    n = int(input("Enter a number: "))
    for key in range (1, n+1):
        square = calculate_square(key)
        square_dictionary[key] = square
    print(square_dictionary)

print_square()
