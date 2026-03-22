import tkinter as tk

import numpy as np
from PIL import Image, ImageTk


charset = "$@B%8&WM#*oahkbdpqwmZO0QLCJU Xzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^'. "

myimgPath = "../examples/images/skull.png"

image = Image.open(myimgPath)

ascii_width = 80

ratio = image.height / image.width

ascii_height = int (ascii_width * ratio * 0.55)

processImage = image.resize((ascii_width, ascii_height)).convert("L")

gray = np.array(processImage)

print(processImage.width, processImage.height, image.filename, "Mode : ", processImage.mode)

maxBrightness = 0
minBrightness = 255
meanBrightness = 0

with open("../examples/result/Skull_ascii.txt", "w") as f:
    for y in range(processImage.height):
        for x in range(processImage.width):
            pixel_brightness = int(gray[y][x])
            ascii_char = charset[pixel_brightness * len(charset) // 256]
            if pixel_brightness > maxBrightness:
                maxBrightness = pixel_brightness
            if pixel_brightness < minBrightness:
                minBrightness = pixel_brightness
            meanBrightness += pixel_brightness
            f.write(ascii_char)
        f.write("\n")

meanBrightness = meanBrightness / (processImage.width * processImage.height)
print("Max brightness : ", maxBrightness)
print("Min brightness : ", minBrightness)
print("Mean brightness : ", meanBrightness)

#fenetre = tk.Tk()
#photo = ImageTk.PhotoImage(processImage)
#label = tk.Label(fenetre, image=photo)
#label.pack()
#fenetre.mainloop()