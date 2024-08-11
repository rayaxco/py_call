class User:
    def __init__(self, email):
        self.email=email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name,power):
        #User.__init__(self,email)
        #another way to initialize super class and access its attributes
       # super().__init__(email)
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

class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,arrows):
        Wizard.__init__(self,name,power)
        Archer.__init__(self,name,arrows)

hb1=HybridBorg('borgie',100,50)
hb1.attack()

