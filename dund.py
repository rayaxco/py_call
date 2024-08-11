class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        self.mydict={
            'name': 'allen',
            'has_pets': False
        }
    def __str__(self):
        return 'New str method overrides the dunder method but only on objects of this class'

    def __len__(self):
        return 5

    def __del__(self):
        print('deleted!')
    def __call__(self):
        return('yes??')

    def __getitem__(self, item):
        return self.mydict[item]
action_figure=Toy('red',5)
print(str(action_figure))
print(str('this is a string works normally on string arguments'))
print(str(action_figure))
print(len(action_figure)) #overrides dunder on objects of toy class
print(len('Bender'))#works normally on other objects
del action_figure
#print(action_figure())
print(action_figure['name'])