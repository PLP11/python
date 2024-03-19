#njeriedith350@gmail.com
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")


person1 = Person("Edith", 26, "Female")
person1.introduce()
