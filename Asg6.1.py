#Q1: Diamond Problem Resolution: Implement classes using multiple inheritance in a way that resolves the diamond problem (ambiguous method resolution).

class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(B, C):
    def method(self):
        super().method()  # Calling the method in the superclass explicitly
        print("D method")

# Example usage:
obj = D()
obj.method()  
