# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from hopfield import Hopfield


def convert_image(fileName):
    img = Image.open(fileName).convert('L')
    arr = np.zeros(img.size)
    img = np.array(img)

    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] > 128:
                arr[i][j] = 1
            else:
                arr[i][j] = -1
    return arr

print("Enter the images you want to store\n(comma separated, with extention e.g: foo.png, bar.jpg)")
print("important: all images must have the same number of pixels!")

userInput = str(raw_input())

print("Do you want to follow the progress? [Y/N]")
yesNo = str(raw_input())
view = False
if yesNo == 'Y' or yesNo == 'y':
	view = True

userInput = userInput.replace(" ", "")

fileList = userInput.split(",")

patterns = []

for image in fileList:
    array = convert_image(image)
    patterns.append(array)

hop = Hopfield()

hop.memorize_patterns(patterns, view = view)

print("Training complete. Do you want to see the weight matrices? [Y/N]")
yesNo = str(raw_input())
if yesNo == 'Y' or yesNo == 'y':
    hop.show_patterns()

print("Stating restoration...")

corruptedImage = convert_image('corrupted.png')
originalCorr = corruptedImage
newImage = hop.update(corruptedImage)

i = 0
while corruptedImage.all() != newImage.all():
    print("update #{}".format(i))
    corruptedImage = newImage
    newImage = hop.update(corruptedImage)
    i += 1
    if i > 10000:
        print("Warning: forced break!")
        break

plt.subplot(211)
plt.imshow(originalCorr,
           cmap=plt.cm.BuPu_r,
           interpolation='none')
plt.title('Corrupted image:')

plt.subplot(212)
plt.imshow(newImage,
           cmap=plt.cm.BuPu_r,
           interpolation='none')
plt.title('Restored Image:')

plt.show()
