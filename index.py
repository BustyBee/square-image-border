from PIL import Image
import os
import sys

# border_size = int(input("Enter your desired border size (0=<): "))
# imgquality = int(input("Enter your desired quality (1-100): "))

border_size = 300
imgquality = 95

imagefiles = ['input/' + sub for sub in os.listdir('input')]

if imagefiles == []:
    print("No images found. Put your images in the 'input' folder.")
    sys.exit()

print(f"Loaded {len(imagefiles)} images")

x = 1
for i in imagefiles:
    
    old_im = Image.open(i)
    old_size = old_im.size

    square_size = 0

    if old_im.width > old_im.height:
        square_size = old_im.width

    else:
        square_size = old_im.height

    square_size += border_size

    new_size = (square_size, square_size)
    new_im = Image.new("RGB", new_size, "White")   ## luckily, this is already black!
    box = tuple((n - o) // 2 for n, o in zip(new_size, old_size))
    new_im.paste(old_im, box)

    # new_im.show()
    new_im.save("output/square_"+i.split("/")[1], quality=imgquality)
    print(f"Image {x} / {len(imagefiles)}")
    x += 1

print(f"Finished, {x} images total")