class student:
    def __init__(self,name,age):
        self.name = name.strip().title()  # Clean + Proper case
        self.age = age
    
    def display(self):
        return f" Name: {self.name} Age: {self.age}"