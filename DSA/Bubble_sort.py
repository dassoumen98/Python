a = []
n = int(input("Enter total number of elements:"))
print("Enter list element:")
for i in range(0,n):
    temp = int(input())
    a.append(temp)
print("the list before sorting: ",a)

for i in range(0,n):
    for j in  range(0 , n-i-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("The sorted list is: ",a)
            