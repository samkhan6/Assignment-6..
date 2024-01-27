# Pitfall: Ambiguous Method Resolution
class Base1:
    def method(self):
        print("Base1 method")

class Base2:
    def method(self):
        print("Base2 method")

class Derived(Base1, Base2):
    def method(self):
        super().method()  # Calling the method in the superclass explicitly
        print("Derived method")

# Example usage:
obj = Derived()
obj.method()  

# Pitfall: Inconsistent Attribute Names
class Parent1:
    common_attribute = "Parent1 attribute"

class Parent2:
    common_attribute = "Parent2 attribute"

class Child(Parent1, Parent2):
    def get_common_attribute(self):
        return super().common_attribute  # Accessing attribute in the superclass explicitly

#Q2: Address potential pitfalls and provide illustrative examples of multiple inheritances.

# Example usage:
obj = Child()
print(obj.get_common_attribute())  

# Pitfall: Increased Complexity
# Multiple inheritance can lead to complex code.
# It is crucial to document the class hierarchy and use it judiciously.
