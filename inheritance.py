class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')
    


class Cat(Mammal):
    def be_annoying(self):
        print('annoying')


dog1 = Dog()
dog1.bark()
cat1 = Mammal()
cat1.walk()
cat2 = Cat()
cat2.be_annoying()




    