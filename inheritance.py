class User:
    def __init__(self, email):
        self.email=email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power,email):
        #User.__init__(self,email)
        #anotherway t o initialize super class and access its attributes
        super().__init__(email)
        self.name=name
        self.power=power
    def attack(self):
        print(f'{self.name} attacking with the power of {self.power}')
class Archer(User):
        def __init__(self, name, num_arrows):
            self.name = name
            self.num_arrows =num_arrows

        def attack(self):
            self.num_arrows=self.num_arrows-1
            print(f'{self.name} attacking with arrows arrows left {self.num_arrows}')
class Ogre(User):
    pass

wizard1=Wizard('merlin',100,'merlin@game.com')
# wizard1.attack()
# archer1=Archer('Robin',50)
# archer1.attack()
# archer1.attack()
print(wizard1.email)
print(dir(wizard1)) #dir provides what methods are associated with the object
