import sys
import os
from PIL import Image

input=sys.argv[1]
print(input)
output=sys.argv[2]
print(output)

if input in os.listdir():
    if not os.path.exists(output):
        os.makedirs(output)
    for item in os.listdir(input):
        image=Image.open(input+'/'+item)
        # print(image)
        # print(item)
        savename=item.removesuffix('.jpg')
        # print(savename)
        image.save(output+'/'+savename+'.png','png')
else:
    print('No such directory')