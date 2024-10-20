from PIL import Image, ImageFilter

# JPG to PNG converter
img = Image.open('./pokemon/pikachu.jpg')

filtered_img = img.convert('L')
filtered_img.save('gray', 'png')
filtered_img.show()
