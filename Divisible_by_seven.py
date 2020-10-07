'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

def divisible_by_seven():
    "determine if the number is divisble by 7"
    numbers = []
    for number in range(2000, 3201):
        if number % 7 == 0 and number % 5 != 0:
            numbers.append(str(number))
    return numbers

def print_output(numbers):
    "print the numbers with the comma seperated string"
    print("," .join(numbers))

if __name__ == "__main__":
    
    numbers = (divisible_by_seven())
    print(numbers)
    print_output(numbers)
   
        