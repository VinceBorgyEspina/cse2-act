#class about a person and car
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and my car is {self.age}.")

#objects
person1 = Person("Cletus", "lambo")
person2 = Person("Elsid", "toyota")

# calling class
person1.introduce()
person2.introduce()
