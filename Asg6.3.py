# a. Method Resolution Order (MRO)
class Base:
    def method(self):
        print("Base method")

class Mixin1(Base):
    def method(self):
        print("Mixin1 method")
        super().method()

class Mixin2(Base):
    def method(self):
        print("Mixin2 method")
        super().method()

class MyClass(Mixin1, Mixin2):
    def method(self):
        print("MyClass method")
        super().method()

# Example usage:
obj = MyClass()
obj.method()  

# b. Super() Function
class Parent:
    def __init__(self):
        self.value = 42

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value *= 2

#Q3: Elaborate on the nuances of employing multiple inheritance in Python.   
# Example usage:
obj = Child()
print(obj.value)  

# c. Composition Over Inheritance
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

# Example usage:
my_car = Car()
my_car.engine.start()  # Composition over inheritance
