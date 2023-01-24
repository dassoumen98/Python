a = []
n = int(input( "Enter the list limit: "))
print("Enter the list items: ")
for i in range(0,n):
    temp = int(input())
    a.append(temp)

element = int(input("Enter the search elemnts: "))

loc = -1
for i in range(0,n):
    if a[i] == element:
        loc = i+1

if(loc == -1):
    print("Element not found: ")
else:
    print("Element found at position: " , loc)
          