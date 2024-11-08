import json

def rjson():
    with open('sample3.json','r') as jsfl:
        x=json.load(jsfl)
        print(x)
        for i in x:
            print(i)
# rjson()
def wjson():
    with open('sample3.json','a') as jsfl:
        li={'sadfg':'asfdg'}
        x=json.dump(li,jsfl)
        print(x)
wjson()