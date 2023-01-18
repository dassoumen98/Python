a = []
n = int(input("Enter total number of elements:"))
print("Enter list element:")
for i in range(0,n):
    temp = int(input())
    a.append(temp)
print("the list before sorting: ",a)

for i in range(1,n):
    temp = a[i]
    j = i-1
    while j >= 0 and temp < a[j]:
        a[j+1] == a[j]
        j = j-1
    a[j+1] = temp

print("The sorted list is: ",a)            