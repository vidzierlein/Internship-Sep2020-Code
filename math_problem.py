""" task: 1.product of two numbers
2. difference of two numbers """

def calc_product(a,b):
    "This calculates the product of a and b"
    product = a * b
    return product

def calc_difference(a,b):
    "This caluclates the difference between a and b"
    difference = a - b   
    return difference

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(calc_product(a,b))
    print(calc_difference(a,b))
