import PIL.Image
import sys
img = PIL.Image.open(sys.argv[1])
img1 = img.load()
charset = [' ','.','°','*','o','O','#','@']
for y in range(img.size[1]):
    for x in range(img.size[0]):
        print(charset[int(((img1[x,y][0]+img1[x,y][1]+img1[x,y][2]))/768*len(charset))],end=" ")
    print()
