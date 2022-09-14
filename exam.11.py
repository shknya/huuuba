# n1
#def chislo(x,y):
#     if y == 0:
#         return 1
#     if x % 2 == 0:
#        return chislo(x, y/2)**2
#     else:
#         return x*chislo(x, y-1)
# x = int(input())
# y = int(input())
# print(chislo(x,y))

# n2
# def initil(x):
#     try:
#         int(x)
#         return True
#     except ValueError:
#         return False
#
# print(int(input()))
# n5
# class Animal:
#     def make_a_sound(self):
#         print("Издает звук")
#
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__()
#     def scratch(self):
#         print("Царапать мебель")
#     def make_a_sound(self):
#         print('мяу')
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#     def dig(self):
#         print("Рыть землю")
#     def make_a_sound(self):
#         print('рык')
#
# cat = Cat()
# cat.make_a_sound()
# dog = Dog()
# dog.make_a_sound()

class IceCream:
    def __init__(self, chenado):
        self.chenado = chenado
    def info(self):
        if self.chenado == 'нет':
            print('vanila')
        else:
            print(f'Добавки {self.chenado}')


ok = IceCream('нет')
ok.info()
ok2= IceCream('шоколадное')
ok2.info()



