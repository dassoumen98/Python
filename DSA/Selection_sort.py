a = []
n = int(input("Enter the total numbers of elements: "))
print("Enter list element")
for i in range(0 , n):
    temp =int(input())
    a.append(temp)
print("The list before sorting: ",a)

for i in range(0,n):
    loc = i
    for j in range(i+1,n):
        if a[j]<a[loc]:
            loc = j
    a[i] , a[loc] = a[loc] , a[i]

print("The sorted list is: ",a)            