from tkinter import filedialog as fd
from blend_modes import overlay
from PIL import Image as img
import numpy as np
import os
os.system('cls')


def cover_select_file():
    filetypes = [("JPG Files", "*.jpg"), ("PNG Files", "*.png"), ("JPEG Files", "*.jpeg")]
    filename = fd.askopenfilename(title="Open Cover Image File", filetypes=filetypes)
    return filename

cover1 = cover_select_file()
cover2 = cover_select_file()
opacity = float(input("Opacity (in multipliers, so 70% would be 0.7): "))

cover1_img = img.open(cover1)
cover1_img = cover1_img.convert("RGBA")
cover1_img = cover1_img.resize((1080, 1080))
cover1_img = np.array(cover1_img)
cover1_img = cover1_img.astype(float)

cover2_img = img.open(cover2)
cover2_img = cover2_img.convert("RGBA")
cover2_img = cover2_img.resize((1080, 1080))
cover2_img = np.array(cover2_img)
cover2_img = cover2_img.astype(float)

blended_img = overlay(cover1_img, cover2_img, opacity)
blended_img = img.fromarray(np.uint8(blended_img))
blended_img.save("blended.png")