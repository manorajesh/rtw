import sys

# Image
image_height = 256
image_width = 256

# Render
print("P3\n%d %d\n255" % (image_width, image_height))

i = 0
j = image_height - 1
while j >= 0:
    sys.stderr.write("\rScanlines remaining: %d" % j)
    while i < image_width:
        r = i / (image_width-1)
        g = j / (image_width-1)
        b = 0.25
        i += 1
        print("%d %d %d" % (int(255*r), int(255*g), int(255*b)))
    i = 0
    j -= 1

sys.stderr.write("Done.")