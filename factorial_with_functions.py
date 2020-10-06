'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.'''

def calculate_factorial(number):
    "Calculate factorial for a given number" 
    if number == 1 or number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)

def print_factorial_list(): 
    "print the factorial of the given number"
    number = int(input("Enter a number: "))
    number_list = calculate_factorial(number)
    print(number_list)
    

if __name__ == "__main__":
    #calculate_factorial(number)
    print_factorial_list()