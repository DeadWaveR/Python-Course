'''
Задание №7
Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод
родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.
'''

class Animal:
    num_of_animals = 0
    def voice(self):
        pass

    def __init__(self):
        Animal.num_of_animals= Animal.num_of_animals + 1

    def print_num():
        print(Animal.num_of_animals)
    print_num=staticmethod(print_num)

class Cat(Animal):
    def voice(self):
        print('Meow')

class Dog(Animal):
    def voice(self):
        print('Woof')

class Goose(Animal):
    def voice(self):
        print('Honk')

barsik = Cat()
baron = Dog()
boris = Goose()

Animal.print_num()

