
class Dog:
    no_of_dogs=0

    def __init__ (self,name, age = 1, weight = 5):
        self.name=name
        print(f"creating dog {self.name}")
        self.age = age
        self.weight = weight
        Dog.no_of_dogs += 1


    def running_speed(self):
        return self.weight / self.age * 10

# nayar_dog = Dog("Speedy",5,10)
# mikaia_dog = ("Foxxy",3,4)

# nayar_dog.name # property name
# nayar_dog.age # property
#print(f"nayar dog running speed is {nayar_dog.running_speed()}")

# print(Dog.no_of_dogs)

# print(nayar_dog.running_speed())

class calculator:
    counter = 0

    @staticmethod
    def add_numbers(a,b):
        return a+b
    
    @staticmethod
    def divide_numbers(a,b):
        return a/b
    
    @classmethod
    def add(cls,a):
        cls.counter += a
        return cls.counter

# Calculator.add_numbers(2,3)
print(calculator.add(1))

print(Dog.no_of_dogs)