# Class of a person
class Person:

    # Class variable
    # It has "one" value that stays the same for all the objects. Since this value is associated
    # with the class, and not with an object. It "belongs" to the class.
    amount = 0

    # Constructor
    # The self parameter needs to be in every function that we define since that refers to the
    # object that we're using right now. "at the current state"
    def __init__(self, 
                 name="Mike", # Sets default to Mike if not given.
                 age="21"
                 ):
        self.name = name # This is an attribute
        self.age = age
        # We do not use self.amount here since "self" refers to the individual object, while when
        # using "Person", we are accessing the "class" as a whole.
        Person.amount += 1  # When we create a new Person() object, increase amount by 1.
        print("Person count = " + str(Person.amount))
        # print ("Name: " + name + "\nAge: " + age)

    # You can also define other function with customized names and access it later on.
    def another_function():
        return "Hello World"
    
    # Normally printing an object returns the Object and it's memory address.
    # To get a summary of all the attributes, you can use the __str__() function.
    def __str__(self):
        return f"Name: {self.name}, and Age: {self.age}"
    
    # Defining a destructor
    def __del__(self):
        Person.amount -= 1
        print("Object Deleted")
        print("Person count = " + str(Person.amount))
    

# An object is the instance of a class.
x = Person()
x2 = Person(name="Sam", age="30")
x3 = Person()
print(x) # Gets the object with memory address
print("Age of x is " + x.age) # Accessing a variable
print(x2)

x2.name = "Samuel" # Change object's name attribute from "Sam" to "Samuel"
print(x2.name)

del x3 # Deletes the x3 object.

# Since Python uses a Garbage Collector, all the memory is released when the program completes execution.
# Thus, at the end, all objects created are deleted. And thus, you might see "Object deleted" printed 2 more
# times at the end of execution.