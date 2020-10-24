'''  Ques.1  Write a function that takes the lengths of three sides : 
 side1, side2 and side3 of the triangle as the in put from the user using input function and 
 return the area and perimeter of the triangle as a tuple. Also , assert that sum of the length of  
 any two sides is greater than the third side

'''


import math

def Calculate(side1,side2,side3): # For calculating perimeter and area
    area = 0
    perimeter = 0
    
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2 :
       print("Given sides  forms a Triangle ")
       perimeter = side1 + side2 + side3
       s = perimeter / 2
       area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))
       
    else :
       print("Given sides Does not form a Triangle ")
       
    return perimeter,area
    
def main(): 
    side1 = int(input("Enter first  side : "))
    side2 = int(input("Enter second side : "))
    side3 = int(input("Enter third  side : "))
    
    perimeter , area = Calculate(side1 , side2 , side3)
    print()
    print("Perimeter : ", perimeter)
    print("Area      : ", int(area))
  
main()