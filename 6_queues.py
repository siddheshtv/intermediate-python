import queue

numbers = [10,20,30,40,50,60,70]

# Say we have 3 threads here. t1, t2, t3 that would be accessing this list for some calculation. So when the t1 will access
# this list, it will pick up the zeroth element [10]. While t2 will then pick up first element [20], and t3 will pick up
# second element [30].

# The problem with this is that when these threads are done with the calculations, they need a way to figure that
# if 20 was already used, it should not be used again. So meaning, the first three elements were used, pick the next
# three elements namely 40, 50, 60.

counter = 0
# Also, say that two threads finished execution at the same time, then the counter will be moved up by 2. And one element
# from the list will be skipped.

# This is where queues are used.

q = queue.Queue() # Creating a queue object. (Default to FIFO)

# Queue operates sequentially. So when t1 will access an element from queue, it will be removed from the queue and next
# element will be pushed up the queue. (First in, first out.)

for number in numbers:
    q.put(number) # Putting numbers into the queue.

print(q.get()) # Will print 10.
print(q.get()) # Will print 20 (Taking up the next element and so on.)

q2 = queue.LifoQueue() # Creating a last in first out queue. (LIFO)

for x in numbers:
    q2.put(number)

print(q2.get()) # Will print 70

q3 = queue.PriorityQueue() # Will create a priority queue that has priority to it's elements.

priority = [1,2,3,4,5,6,7] # Lower the number, higher the priority.

number_priority_pairs = sorted(zip(numbers, priority), key=lambda x: x[1]) # Zips the numbers and priorities together

for pair in number_priority_pairs:
    q3.put(pair)

print(f"Q3 Element 1: {q3.get()}") # Prints number 10, which has highest priority = 1