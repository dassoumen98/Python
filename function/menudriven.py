def area_circle(radius):
    return 3.14 * (radius ** 2)

def area_square(side):
    return side ** 2

print("1. Area of Circle")
print("2. Area of Square")
choice = int(input("Enter your choice: "))

if choice == 1:
    radius = int(input("Enter the radius of the circle: "))
    print("Area of the circle is: ", area_circle(radius))

elif choice == 2:
    side = int(input("Enter the side of the square: "))
    print("Area of the square is: ", area_square(side))

else:
    print("Invalid choice")