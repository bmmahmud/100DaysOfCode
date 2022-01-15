### Create Class - 15/01/2022
class Dog():
    """" A Simple attempt to model a Dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def roll_over(self):
        """"Simulate Rolling Over in Response to a command."""
        print(self.name.title() + " rolled over!")
    def sit(self):
        print(self.name.title() + " is now sitting.")

#making an Instance from a Class
my_dog = Dog('willie',6)

print("My dog's name is "+my_dog.name.title()+".")
print(f"My dog is {str(my_dog.age)} years old.")

# Calling a method
my_dog.sit()
my_dog.roll_over()

print("#"*30)
# another instance
your_dog = Dog('Max',5)

print("Your dog's name is "+your_dog.name.title()+".")
print(f"Your dog is {str(your_dog.age)} years old.")
# Calling a method
your_dog.sit()
your_dog.roll_over()