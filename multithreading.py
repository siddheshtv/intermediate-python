import threading # using threading module

def function1():
    for i in range(100):
        print("One")

def function2():
    for i in range(100):
        print("Two")

# Creating an object of the Thread class that resides in the "threading" module
t1 = threading.Thread(target=function1 # We are not calling function1 here, but stating that this is the function that
                      # is to be used.
                      )
t2 = threading.Thread(target=function2)

# This will execute functions sequentially.
# function1()
# function2()

# The value of using "Threads" is that you can use it to make multiple functions work in "parallel"
# instead of running each of them sequentially.

t1.start() # One is printed.

print("Right in the middle.") # This will be printed right in the middle when t1 and t2 are both running parallely.

t2.start() # Two would be printed simultaneously alongside one. Since both will run in parallel.

t1.join() # This will make sure to not move forward (to the next function/statement) until t1 has finished execution.

# Thus, "Hello World will be printed only after t1 has completed execution. Make no mistake, t2 might still be running."
print("Hello World")