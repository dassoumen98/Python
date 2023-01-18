import math
a = int(input("Enter the First side of Traingle"))
b = int(input("Enter the Second side of Traingle"))
c = int(input("Enter the Third side of Traingle"))
s = (a+b+c)/2
Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
Perimeter = (a+b+c)
print("The area of Triangel is ",Area)
print("The area of Triangel is ",Perimeter)

