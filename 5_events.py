import threading
import time

eventA = threading.Event() # Creating an event. That can further be triggered. --- (0)

def myfunction():
    print("Waiting for the event A to triggered.\n\n")
    eventA.wait() # This makes our function wait until the event A is triggered. --- (1)
    print("Performing action XYZ now...") # Reaction after the event is triggered. --- (2)

t1 = threading.Thread(target=myfunction)
t1.start()

x = input("Do you want to trigger the event? (y/n): ")
if x == "y":
    eventA.set() # Setting the event, means triggering the event. Meaning, it is activated/triggered --- (3)


# Daemon threads --- Running in the background even after the script terminates.
# They are not tied to the program. Programs usually waits for all threads to stop before completing execution.
# Although, that is not the case when it comes to Daemon threads. --- (4)


path = "assets/text.txt"
text = ""

def read_file():
    global path, text
    while True:
        with open(path, "r") as file:
            text = file.read()
        time.sleep(3)

def print_loop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file, daemon=True) # Specifying that this thread is a "daemon" thread --- (5)
# Note that "t1" will adapt to the changes in the "text.txt" --- (6)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()