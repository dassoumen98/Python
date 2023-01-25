a = []
n = int(input("Enter thle list limit: "))
print("Enter the list item: ")
for i in range(0 , n):
    temp = int(input())
    a.append(temp)

element = int(input("Enter the search elemnts: "))
loc = -1 
low = 0
high = n-1
while(low <= high):
    mid = (low+high)//2
    if a[mid]== element:
        loc = mid
        break

    elif element < a[mid]:
        high = mid -1
    
    elif element > a[mid]:
        low = mid +1

if loc == -1:
    print("element not found")
else:
    print("element found at position ",loc+1)