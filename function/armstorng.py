n = int(input("enter the number:"))
def calcualte(n):
    sum = 0
    rem = 0
    num = n
    while(n>0):
        rem = n % 10
        n = n // 10 
        sum = sum + (rem**3)

    if(sum == num ):
        print(num,"is amrstrong")
    else:
        print(num,"is not  amrstrong")
calcualte(n)
    