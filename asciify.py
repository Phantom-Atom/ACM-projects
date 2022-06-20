# Import libraries
from PIL import Image, ImageDraw, ImageFont
import math

# Setting up a character databse based on the pixel brightness and intensity
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

# Setting up scale and character attributes
scaleFactor = 0.2

oneCharWidth = 10
oneCharHeight = 10

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

im = Image.open("Images\Input\filename").convert('RGB')

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

# Calculating height/width ratio to check whether the output image matches it
print(height/width)

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

twidth, theight = outputImage.size
print(theight/twidth)

# Converting the image into greyscale first, then turning it back into RGB
for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

outputImage.save('output.jpg')
