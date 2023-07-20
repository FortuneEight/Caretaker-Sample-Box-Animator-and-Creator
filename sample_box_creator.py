from PIL import Image, ImageDraw, ImageFont
import os
import time
os.system('cls')

rect_shape = [(320, 193), (759.9, 632.9)]

start = time.time()

# create new transparent image
main_img = Image.new(mode='RGB', size=(1080,1080))

# open cover image and resize

cover_file_path = input("What is the file path to the Sample Box Cover image? ")

cover_img = Image.open(cover_file_path)
cover_img = cover_img.resize((415, 415))

# initialize ImageDraw object and draw rectangle
draw = ImageDraw.Draw(main_img)

# calculate image
direction = round(float(input("What is the direction of the track? ")))

if direction <= -90:
    draw.rectangle(rect_shape, fill = "#ffb4b4")
elif direction <= -80:
    draw.rectangle(rect_shape, fill = "#ff8f9b")
elif direction <= -70:
    draw.rectangle(rect_shape, fill = "#ff688d")
elif direction <= -60:
    draw.rectangle(rect_shape, fill = "#f7438f")
elif direction <= -50:
    draw.rectangle(rect_shape, fill = "#cb3095")
elif direction <= -40:
    draw.rectangle(rect_shape, fill = "#9f1c9b")
elif direction <= -30:
    draw.rectangle(rect_shape, fill = "#a339d1")
elif direction <= -20:
    draw.rectangle(rect_shape, fill = "#a459ff")
elif direction <= -10:
    draw.rectangle(rect_shape, fill = "#a481ff")
elif direction <= -3:
    draw.rectangle(rect_shape, fill = "#b0a4ff")
elif direction <= 2:
    draw.rectangle(rect_shape, fill = "#c4c2ff")
elif direction <= 9:
    draw.rectangle(rect_shape, fill = "#99b0ff")
elif direction <= 19:
    draw.rectangle(rect_shape, fill = "#50b1e5")
elif direction <= 29:
    draw.rectangle(rect_shape, fill = "#1eb480")
elif direction <= 39:
    draw.rectangle(rect_shape, fill = "#00c950")
elif direction <= 49:
    draw.rectangle(rect_shape, fill = "#008a00")
elif direction <= 59:
    draw.rectangle(rect_shape, fill = "#20a300")
elif direction <= 69:
    draw.rectangle(rect_shape, fill = "#49b700")
elif direction <= 79:
    draw.rectangle(rect_shape, fill = "#77c700")
elif direction <= 89:
    draw.rectangle(rect_shape, fill = "#77c700")
elif direction <= 100:
    draw.rectangle(rect_shape, fill = "#e4e400")

# draw cover
main_img.paste(cover_img, (333, 205))

# import fonts
tahoma_reg = ImageFont.truetype("tahoma.ttf", 46)
tahoma_bold = ImageFont.truetype("tahoma_bold.ttf", 53)

y_val = 670.73

# add top text(s) - title of song, semitone value
top_texts = input("Please input your top texts (title of song, semitone value). If you are having multiple lines, seperate them by using the '^' symbol. ").split("^")
for i in range(len(top_texts)):
    w = draw.textlength(top_texts[i], font=tahoma_bold)
    position = ((1080 - w) / 2, y_val)
    bbox = draw.textbbox(position, top_texts[i], font=tahoma_bold)
    draw.rectangle(bbox, fill="black")
    draw.text(position, top_texts[i], font=tahoma_bold, fill=(255,255,255))
    if i == len(top_texts) - 1:
        y_val += (61.33 * 1.2)
    else:
        y_val += (61.33 * 1.2)

# add bottom text(s) - creator, album, year
bottom_texts = input("Please input your bottom texts (creator, album, year). If you are having multiple lines, seperate them by using the '^' symbol. ").split("^")
for i in range(len(bottom_texts)):
    w = draw.textlength(bottom_texts[i], font=tahoma_reg)
    position = ((1080 - w) / 2, y_val)
    bbox = draw.textbbox(position, bottom_texts[i], font=tahoma_reg)
    draw.rectangle(bbox, fill="black")
    draw.text(position, bottom_texts[i], font=tahoma_reg, fill=(255,255,255))
    y_val += (61.33)

# save image
file_name = input("What would you like to title your file? ")
main_img.save(f"{file_name}.png")
end = time.time()

# print(f"Time elapsed: {end-start} seconds")