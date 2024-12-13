image_name = 'img.png'

with open(image_name, 'rb') as f:
    image_bytes = f.read()

print(image_bytes)

with open('new_image.png', 'wb') as f:

    f.write(image_bytes)