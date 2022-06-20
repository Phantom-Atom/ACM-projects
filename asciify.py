from PIL import Image, ImageDraw, ImageFont
import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

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

print(height/width)

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

twidth, theight = outputImage.size
print(theight/twidth)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

outputImage.save('output.jpg')