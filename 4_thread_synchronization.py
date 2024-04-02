import threading
import time


x = 8192

lock = threading.Lock() # This lock object will allow us to forbid other functions from accessing a variable
# or a resource when some other function is using it. It will prevent what happened in (1) --- (2)

def double():
    global x # Accessing a variable outside the scope of a function. Making it "global" --- (0)
    global lock # Making the lock global to access it inside this function. --- (4)
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the maximum")
    lock.release() # Releasing the lock after execution is finished. --- (5)

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum")
    lock.release()

thread1 = threading.Thread(target=half)
thread2 = threading.Thread(target=double)

# This will run both the threads in parallel.
# But when you run the in parallel, it will reach a point where double() will go for doubling the "x" and right after that
# half() will make the half of it. This will continue in a loop and never end. --- (1)

# thread1.start()
# thread2.start()


# Semaphores can also be used to limit the access to a resource. These do not lock the resource completely,
# but rather limit the access based on values. Ex: A function can access a resource only 5 times in continuity. --- (6)
semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access.")
    time.sleep(8)
    print(f"{thread_number} was released.")
    semaphore.release()

for thread_number in range(10):
    t = threading.Thread(target=access, args=(thread_number,)) # Passing the thread_number as an argument.
    # Remember that args expects a tuple. So even if you have one parameter, you need to add a "comma" after it.
    t.start()
    time.sleep(1)