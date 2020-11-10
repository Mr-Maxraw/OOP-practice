from module import summ as s, b as bigB

s()
print(bigB)

class Fruit():
    size = 1

    def ch_size(self, newsize):
        self.size = newsize
    
    def prt(self):
        pass

class Apple(Fruit):
    colour = 'red'
    col = 0

    def __init__(self, name):
        print("Apple was made")
        Apple.col += 1
        self.name = name

    def __str__(self):
        return self.name

    def prt(self):
        print ("this is apple with size " + str(self.size) + " and of colour " + str(self.colour))

class A():
    __nam = "asdjhg"

    def ch_name(self, newname):
        self.__nam = newname

    def get_name(self):
        return self.__nam

a = A()
b = A()
a.ch_name("abc")
print()

apl = Apple('a')
apl.ch_size(2)
print(apl)
apl.prt()
applefarm = [Apple('b'), Apple('c'), Apple('d')]
# for i in applefarm:
#     print(i)
# print(Apple.col)
print(delattr(apl, 'name'))
print(apl.name)
# hasattr()
# setattr()
# delattr()