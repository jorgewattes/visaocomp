from PIL import Image


img = Image.open('Aula03/vegies.png')

region = (20,20,100,100)
img_crop = img.crop(region)
img_crop.show(title='cropped')

img_rot = img.rotate(45.0)
img_rot.show(title='rotated')

img_crop.save('Aula03/vegies_cropped.png')
img_rot.save('Aula03/vegies_rotated.png')