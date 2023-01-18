queue = [1, 2, 3, 4, 5, 6]
print("original queue is: ",queue)
queue.append(7)
print("queue after push operation is: ",queue)
queue.pop(0)
print("queue after pop operation is: ",queue)

last_element_index = len(queue)-1

print("Value obtained after peek operation is: ",queue[last_element_index])


