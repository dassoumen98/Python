a=int(input("Enter the Principle Amount:"))
b=int(input("Enter the Time in Years:"))
c=int(input("Enter the Annual Rate of Interset:"))
def Compound_interset(p,n,r):
   
    #A = p*(pow((1+r/100), n))
    A= p*(1+r/100)**n
    ci = A-p
    print("Compound Interest is:" +str(ci))

Compound_interset(a , b , c)


