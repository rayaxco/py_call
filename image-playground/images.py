# from PIL import Image,ImageFilter
#
# image=Image.open('./pokedex/pikachu.jpg')
# # print(dir(image))
# # print(image)
# # blur=image.filter(ImageFilter.BLUR)
# # blur.save('blurred.png','png')
#
# effect=image.filter(ImageFilter.SHARPEN)
# effect.save('sharp.jpg')
# grey=image.convert('L')
# res=grey.resize((300,300))
# res.save('resized.png','png')
# print(res.size)
from PIL import Image,ImageFilter
img=Image.open('./pokedex/jan-hrdlicka-lKepw6_yvVQ-unsplash.jpg')
img.thumbnail((400,200))
img.save('thumb-resi-road.png','png')