num1 = int(input("Enter the 1st Number:"))
num2 = int(input("Enter the 2nd Number:"))
num3 = int(input("Enter the 3nd Number:"))
if num1>=num2:
    if num1>=num3:
        print("Largest Number is:"+ str(num1))
    else:
       print("Largest Number is:"+ str(num3) ) 
else:
    
    if num2>=num3:
        print("Largest Number is:"+ str(num2))
    else:
       print("Largest Number is:"+ str(num3) )          