#Q4: Illuminate the process of metaclass mechanics in Python, perhaps accompanied by an illustrative example?
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Modify the class creation process
        dct['custom_attribute'] = 42
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    def __init__(self):
        print(f"MyClass instance created with custom_attribute: {self.custom_attribute}")

# Example usage:
obj = MyClass()
