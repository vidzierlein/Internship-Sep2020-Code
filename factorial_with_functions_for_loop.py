'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.'''


def calculate_factorial(number):
    "Calculate factorial for a given number" 
    """ for number in range of (0, 1000000):
        if number == 1 or number == 0:
            return 1
        else:
            return math.factorial(number) """
    factorial = 1
    for number in range(1,number+1):
        
        factorial = product * number
    return product

def print_factorial_list(): 
    "print the factorial of the given number"
    number= int(input("Enter a number: "))
    factorial = calculate_factorial(number)
    print("The factorial of %d  = %d" %(number, factorial))
    return(factorial)
def factorial(num):
        fac=1
    if num!=0:
        fac= ((fac*i) for i in range(1,number+1)) 
    return fac
    
if __name__ == "__main__":
    print_factorial_list()