
# Python3 program to check if three 
# sides form a  triangle or not  

class validateTriangle:
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        "initializing"
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        number_of_sides = 3
 
    def checkValidity(self):  
        "function to check if three sides form a triangle or not"  
        # check condition  
        if (self.angle1 + self.angle2 + self.angle3 == 180):
            print("This is a triangle")
            return True
        else: 
            print("This is not a traingle")  
            return False
               


validateTriangle_one = validateTriangle(30, 20, 40)
validateTriangle_one.checkValidity()

