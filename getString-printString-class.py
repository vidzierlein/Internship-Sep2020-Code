'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
-----------
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.'''

class InputOutString:
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Enter a value: ")

    def printString(self):
        print(self.str.upper())

strObj = InputOutString()
strObj1 = InputOutString()
strObj.getString()
strObj.printString()    
strObj1.printString()