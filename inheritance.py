class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        return None
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __del__(self):
        return f"Deleted object with name {self.name}"


class Worker(Person): # Passing Person class inside the Worker class to "inherit" it's attributes.
    def __init__(self, name, age, salary):
        
        # Super accesses the parent class, and gets its attributes through the __init__() method
        # in this case the "Person" class, and attributes = name and age.
        super(Worker, self).__init__(name, age)
        self.salary = salary # Assigning salary to the object since it is not inherited.
        return None
    
    def __str__(self):
        # Using super() to access the __str__() of the parent class and use it in Worker class.
        # We are then taking a step further and storing it in a variable called "text"
        # We can add the "salary" attribute from the "current" class and print out all "three" attributes.
        text = super().__str__()
        text += f", Salary: {self.salary}"
        return text
    
    def calc_yearly_salary(self):
        return self.salary * 12
    
    def __del__(self):
        return super().__del__() # Using super() to access the __del__() of the parent class and use it in Worker class.
    
worker1 = Worker(name="Sam", age=20, salary=4000)
yearly_salary = worker1.calc_yearly_salary()
print(worker1) # Printing all attributes of worker1
print("Yearly salary: " + str(yearly_salary))
del worker1
    
# Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    
    # Overloading the addition operator to add two vectors
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overloading the subtraction operator to add two vectors
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"
    
    def __del__(self):
        return "Deleted Object"
    
v1 = Vector(2,5)
v2 = Vector(4,3)

print(v1)
print(v2)

# We can directly use the "+" operator to add two vectors and it's output will be stored in v3
# This was possible due to the __add__() function that we defined. It overloaded the "+" operator
# in order to handle addition of objects being created from custom classes.
v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)