class Cat():
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __repr__(self):
        return f'Cat {self.name} {self.age}'
    
if __name__ == '__main__':
    cats = [Cat('Tom', 4), Cat("Angela", 3), Cat('Jack', 5)]
    for cat in cats:
        print(cat)
        