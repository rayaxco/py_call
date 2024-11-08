import os
import sys
from PIL import Image

fr=sys.argv[0]
to=sys.argv[1]
print(fr,to)
a=fr
b=to
if a in os.listdir(os.getcwd()):
    if not os.path.exists('./converted'):
        os.makedirs(b)
    for elem in os.listdir('./pokedex/'):
        image = Image.open('./pokedex/' + elem)
        name=elem.removesuffix('.jpg')
        # print(elem)

        image.save('./converted/'+name+'.png','png')

else:
    print('no such directory')