stack = [1, 2, 3, 4, 5, 6]
print("original stack is: ",stack)
stack.append(7)
print("Stack after push operation is: ",stack)
stack.pop()
print("Stack after pop operation is: ",stack)

last_element_index = len(stack)-1
print("Value obtained after peek operation is: ",stack[last_element_index])




