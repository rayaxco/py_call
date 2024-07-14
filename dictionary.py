def dictionary():
    def dict_functions(di):
        #print(di)
        print(di.get('peter bishop')) #returns olivia bishop
        print(di.get('olivia dunham')) #returns none because no such key
        di.get('kevin garvey','norah durst') #takes key value pair and returns value; doesnot modify the actual dictionary
        print(di)

        #Another way to create a dictionary
        user1=dict(name='olivia')
        print(user1)

        user={
            'basket':[1,2,3],
            'greet':'hello',
            'age':20
        }
        print(user.items()) #.items() returns key value pairs in form of tuple
        user2=user.copy() #.copy() copies dict to dict
        print(user2)
        user.clear() #.clear() deletes everythin in a dictionary
        user2.pop('greet') #.pop(key) delete a specified key value pair
        print(user2)
        user2.update({'age':55}) #.update({key:value}) updates the value of the key, if no such key; it creates new key val pair and pushes to dict
        print(user2)
        user2.popitem() #pops the last item=key+val inthe dict
        print(user2)
        user2.update({'kevin garvey':'norah durst'})
        print(user2)
        user={
            'user1':{'fname':'peter', 'lname':'bishop','type':'user'},
            'user2':{'fname':'olivia', 'lname':['bishop','dunham'],'type':'user'},
            'user3':{'fname':'kevin', 'lname':'garvey','type':'user'},
            'user4':{'fname': 'walter', 'lname': 'bishop', 'type': ['user','creator']},
            ('user','destroyer'):{'fname': 'Norah', 'lname': ['durst','garvey'], 'type': ['user','destroyer']}
        }
        print(user)
        print(('user','destroyer') in user.keys())
        print(user['user4']['type'][0:2]) #use  square brackets when using nested dictionaries
        print(user[user4].get('fname'))
    dic = {
        'peter bishop': 'olivia bishop',
        'walter bishop': 'elizabeth bishop',
        'alistair peck': 'arlette turling'
    }
    dict_functions(dic)


dictionary()
