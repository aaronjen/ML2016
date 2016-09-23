from PIL import Image
import sys
import numpy

fileName = sys.argv[1]

im = Image.open(fileName)

width, height = im.size
imArray = numpy.asarray(im)

imArray = [i for i in imArray]

newIm = Image.new("L", (width, height))

for y in range(height):
    for x in range(width):
        putx = width - x - 1
        puty = height - y - 1
        newIm.putpixel((putx, puty), int(imArray[y][x]))


newIm.save('new.png')
