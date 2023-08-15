class Cat:
    type = 'a pet'

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'My name is {self.name} and my age {self.age}'
    
barsik = Cat("Barsik", 1)
print(barsik)

class Car:
    
    def __init__(self, color: str, mileage: int) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f'The {self.color} car has {self.mileage} miles.'
    
toyota = Car("Blue", 20000)
print(toyota)