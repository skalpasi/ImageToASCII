import PIL.Image
import sys

f = PIL.Image.open(sys.argv[1])
img = f.load()

charset = [' ','.','°','*','o','O','#','@']
for width in range(f.size[1]):
    for height in range(f.size[0]):
        r = img[height, width][0]
        g = img[height, width][1]
        b = img[height, width][2]
        shade = (r + g + b)/3  # brightness of pixel
        percShade = shade/256  # percentage of brightess (1 for maximum brightness)
        charIndex = int(percShade * len(charset))  # pick character from charset according to the % brightness
        # 100% brightness (percShade = 1) will pick the last element of charset which has the highest brightness
        print(charset[charIndex], end=" ")
    print()
