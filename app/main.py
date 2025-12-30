class Animal:
    animals = set()
    def __init__(self,
                 name: str,
                 appetite: int,
                 is_hungry = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry
        Animal.animals.add(self)
    
    def print_name(self) -> str:
        return f"Hello, I'am {self.name}"

    def seed(self) -> int:
        
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0

    def __repr__(self):
        return f"name: {self.name}, appetite: {self.appetite}"
    
class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry = True
                 ) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(self.name, 3)
    
    def catch_mouse(self):
        print("The hunt began!")

class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry = True
                 ) -> None:
        self.name = name
        self.is_hungry = is_hungry
        super().__init__(self.name, 7)
    
    def bring_slippers(self):
        print("The slippers delivered!")

def feed_animals(animals : list) -> int:
    suma = sum(x.appetite for x in animals)
    print(suma)