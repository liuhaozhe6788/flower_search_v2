# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"./to_be_uploaded/camelia_2.jpeg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image

newsize = (3000, 2000)
im1 = im.resize(newsize)
# Shows the image in image viewer
im1.show()