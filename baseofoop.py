class playercharacter:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print('run')

    def shout(self):
        print(f'hi i am {self.name} and i am {self.age} years old')

player1=playercharacter('rayaxco',27)
player1.shout()
