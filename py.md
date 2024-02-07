1.Program to calculate the length and check occurrence:

```py
def check_list(lst):
    if len(lst) == 8 and lst.count(lst[4]) == 3:
        return True
    else:
        return False

# Test the function
test_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(check_list(test_list))  # Example usage

```

2.Program to compute distance between two points:

```py
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between the points:", distance)


```

3.Program to find the number of stones in each pile:

```py
n = int(input("Enter the number of stone piles: "))

stones = []
total = 0
for i in range(n):
    stones.append((total + (i + 1)))
    total += (i + 1)

print("Number of stones in each pile:", stones)
```

4.Program to find the longest string in a list of strings:

```py
def longest_string(strings):
    return max(strings, key=len)

# Example usage:
string_list = ['apple', 'banana', 'kiwi', 'strawberry']
print("Longest string:", longest_string(string_list))

```

5.Program using a while loop to print a countdown:

```py
number = int(input("Enter a number to countdown from: "))

while number >= 0:
    print(number)
    number -= 1

```

6.Recursive function to calculate the factorial of a number:

```py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
print(factorial(5))

```

7.Function to convert temperature from Celsius to Fahrenheit:

```py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
print(celsius_to_fahrenheit(20))

```

8.Recursive function to generate the Fibonacci sequence:

```py
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
for i in range(10):
    print(fibonacci(i))

```

9.Function to calculate simple interest:

```py
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Example usage:
print(simple_interest(1000, 5, 2))

```

10.Recursive function to find the greatest common divisor (GCD) using the Euclidean algorithm:

```py
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage:
print(gcd(48, 18))
```

11.Recursive function to count occurrences of a specific character in a string:

```py
def count_char(string, char):
    if not string:
        return 0
    elif string[0] == char:
        return 1 + count_char(string[1:], char)
    else:
        return count_char(string[1:], char)

# Example usage:
print(count_char("hello world", 'l'))

```

12.Recursive function to reverse the order of elements in a list:

```py
def reverse_list(lst):
    if len(lst) == 0:
        return lst
    else:
        return reverse_list(lst[1:]) + [lst[0]]

# Example usage:
print(reverse_list([1, 2, 3, 4, 5]))

```

13.Function to check if a number is even or odd:

```py
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Example usage:
print(check_even_odd(5))
```

14.Function to find the maximum value in a list of numbers:

```py
def find_max(numbers):
    return max(numbers)

# Example usage:
print(find_max([1, 5, 3, 9, 2]))

```

15.Program to check if a key exists in a dictionary:

```py
def check_key(dictionary, key):
    if key in dictionary:
        print("Key exists in the dictionary.")
    else:
        print("Key does not exist in the dictionary.")

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
check_key(sample_dict, 'b')

```

16.Program to calculate the number of key-value pairs in a dictionary:

```py
def count_pairs(dictionary):
    return len(dictionary)

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
print("Number of key-value pairs:", count_pairs(sample_dict))

```

17.Program to add, update, and remove key-value pairs in a dictionary:

```py
def modify_dictionary(dictionary):
    dictionary['d'] = 4  # Adding a new key-value pair
    dictionary['a'] = 10  # Updating an existing key-value pair
    del dictionary['b']  # Removing a key-value pair
    print("Modified dictionary:", dictionary)

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
modify_dictionary(sample_dict)

```

18.Program to sort the keys or values of a dictionary:

```py
def sort_dictionary(dictionary, by_key=True, ascending=True):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0 if by_key else 1], reverse=not ascending))
    print("Sorted dictionary:", sorted_dict)

# Example usage:
sample_dict = {'b': 2, 'a': 1, 'c': 3}
sort_dictionary(sample_dict)  # Sort by key, ascending
sort_dictionary(sample_dict, by_key=False, ascending=False)  # Sort by value, descending

```

19.Program to merge two dictionaries:

```py
def merge_dicts(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merge_dicts(dict1, dict2)

```

20.Program to compute and print the union and intersection of two sets:

```py
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

```

21.Program to check if an element exists in a set:

```py
def check_element_exists(some_set, element):
    if element in some_set:
        print("Element exists in the set.")
    else:
        print("Element does not exist in the set.")

# Example usage:
sample_set = {1, 2, 3, 4, 5}
check_element_exists(sample_set, 3)

```

22.Program to update one set with the elements of another set:

```py
def update_set(set1, set2):
    set1.update(set2)
    print("Updated set:", set1)

# Example usage:
set1 = {1, 2, 3}
set2 = {4, 5, 6}
update_set(set1, set2)

```

23.Program to calculate and print the number of elements in a set:

```py
def count_elements(some_set):
    return len(some_set)

# Example usage:
sample_set = {1, 2, 3, 4, 5}
print("Number of elements in the set:", count_elements(sample_set))

```

24.Program to check if a particular element exists in a set:

```py
def check_element_exists(some_set, element):
    if element in some_set:
        print("Element exists in the set.")
    else:
        print("Element does not exist in the set.")

# Example usage:
sample_set = {1, 2, 3, 4, 5}
check_element_exists(sample_set, 3)

```

25.Recursive function to check if a word or phrase is a palindrome:

```py
def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

# Example usage:
print(is_palindrome("radar"))

```

26.Program to compare two sets and print whether they are equal or one is a subset of the other:

```py
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

if set1 == set2:
    print("Sets are equal.")
elif set1.issubset(set2):
    print("Set 1 is a subset of Set 2.")
elif set2.issubset(set1):
    print("Set 2 is a subset of Set 1.")
else:
    print("Sets are neither equal nor subsets of each other.")

```

27.Program to remove duplicates from a list and convert it into a set:

```py
original_list = [1, 2, 3, 2, 4, 5, 6, 4]
unique_set = set(original_list)
print("Set with duplicates removed:", unique_set)

```

28.Program to find missing numbers in sets:

```py
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

missing_in_set1 = set2 - set1
missing_in_set2 = set1 - set2

print("Missing numbers in set 1:", missing_in_set1)
print("Missing numbers in set 2:", missing_in_set2)

```

29.Program to find the third largest number in a list using sets:

```py
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]

unique_numbers = set(numbers)
unique_numbers_sorted = sorted(unique_numbers)

if len(unique_numbers_sorted) >= 3:
    third_largest = unique_numbers_sorted[-3]
    print("Third largest number:", third_largest)
else:
    print("There are less than 3 unique numbers.")

```

30.Program to check if a given value is present in a set:

```py
def check_value_in_set(some_set, value):
    if value in some_set:
        print("Value is present in the set.")
    else:
        print("Value is not present in the set.")

# Example usage:
sample_set = {1, 2, 3, 4, 5}
check_value_in_set(sample_set, 3)


```
