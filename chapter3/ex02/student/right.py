# Write your program here

def sides(side1, side2, side3):
    return side1 % 2 == 0 and side2 % 2 == 0 and side3 % 2 == 0





side1 = float(input("How long is the first side of the triangle?: "))
side2 = float(input("How long is the second side of the triangle?: ")) 
side3 = float(input("How long is the third side of the triangle?: ")) 


if sides(side1, side2, side3):
    print ("The triangle is a right triangle") 
else:
    print("This is not a right triangle") 




