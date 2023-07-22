from PIL import Image as img
from PIL import ImageDraw, ImageFont
import os
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
os.system('cls')

COVER_FILE_PATH = None
TOP_FONT_TTF_PATH = None
BOTTOM_FONT_TTF_PATH = None
SAVE_FILE_NAME = None

# FORTUNE SETTINGS
# Tahoma Bold for Top Font (53 pt)
# Tahoma Regular for Bottom Font (46 pt)


def sample_box_creator(cover_file_path, direction, top_font_ttf, top_font_size, bottom_font_ttf, bottom_font_size, top_texts, bottom_texts, save_file_name):
    rect_shape = [(320, 193), (759.9, 632.9)]

    # create new transparent image
    main_img = img.new(mode='RGB', size=(1080,1080))

    # open cover image and resize
    cover_img = img.open(cover_file_path)
    cover_img = cover_img.resize((415, 415))

    # initialize ImageDraw object and draw rectangle
    draw = ImageDraw.Draw(main_img)

    # calculate image
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
    top_font = ImageFont.truetype(top_font_ttf, top_font_size)
    bottom_font = ImageFont.truetype(bottom_font_ttf, bottom_font_size)

    top_font_px = top_font_size * (4/3)
    bottom_font_px = bottom_font_size * (4/3)

    y_val = 670.73

    # add top text(s) - title of song, semitone value
    for i in range(len(top_texts)):
        w = draw.textlength(top_texts[i], font=top_font)
        position = ((1080 - w) / 2, y_val)
        bbox = draw.textbbox(position, top_texts[i], font=top_font)
        draw.rectangle(bbox, fill="black")
        draw.text(position, top_texts[i], font=top_font, fill=(255,255,255))
        if i == len(top_texts) - 1:
            y_val += (bottom_font_px * 1.2)
        else:
            y_val += (bottom_font_px * 1.2)

    # add bottom text(s) - creator, album, year
    for i in range(len(bottom_texts)):
        w = draw.textlength(bottom_texts[i], font=bottom_font)
        position = ((1080 - w) / 2, y_val)
        bbox = draw.textbbox(position, bottom_texts[i], font=bottom_font)
        draw.rectangle(bbox, fill="black")
        draw.text(position, bottom_texts[i], font=bottom_font, fill=(255,255,255))
        y_val += (bottom_font_px)

    # save image
    main_img.save(f"{save_file_name}.png")


def cover_select_file():
    global COVER_FILE_PATH
    filetypes = [("JPG Files", "*.jpg"), ("PNG Files", "*.png"), ("JPEG Files", "*.jpeg")]
    filename = fd.askopenfilename(title="Open Cover Image File", filetypes=filetypes)
    COVER_FILE_PATH = filename

def topttf_select_file():
    global TOP_FONT_TTF_PATH
    filetypes = [("TTF Files", "*.ttf")]
    filename = fd.askopenfilename(title="Open Top TTF File", filetypes=filetypes)
    TOP_FONT_TTF_PATH = filename

def bottomttf_select_file():
    global BOTTOM_FONT_TTF_PATH
    filetypes = [("TTF Files", "*.ttf")]
    filename = fd.askopenfilename(title="Open Bottom TTF File", filetypes=filetypes)
    BOTTOM_FONT_TTF_PATH = filename

def update_progress_bar(value):
    pb['value'] = value

def generate_sample_box():
    global COVER_FILE_PATH
    global TOP_FONT_TTF_PATH
    global BOTTOM_FONT_TTF_PATH
    global SAVE_FILE_NAME

    update_progress_bar(0)

    direction = int(txt_01.get(1.0, "end-1c"))
    top_font_size = int(txt_02.get(1.0, "end-1c"))
    bottom_font_size = int(txt_03.get(1.0, "end-1c"))
    top_texts = txt_04.get(1.0, "end-1c").split("^")
    bottom_texts = txt_05.get(1.0, "end-1c").split("^")

    filetypes = [("PNG Files", "*.png")]
    SAVE_FILE_NAME = fd.asksaveasfilename(title="Save as PNG File", filetypes=filetypes)

    update_progress_bar(50)

    sample_box_creator(COVER_FILE_PATH, direction, TOP_FONT_TTF_PATH, top_font_size, BOTTOM_FONT_TTF_PATH, bottom_font_size, top_texts, bottom_texts, SAVE_FILE_NAME)

    update_progress_bar(100)

    showinfo(message="File saved successfully!")

app = Tk()
app.title("F8's Sample Box Generator")

lbl_title = Label(app, text = "F8's Sample Box Generator", font="Helvetica 18 bold")
lbl_title.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

lbl_01 = Label(app, text="Open Cover File: ", font="Helvetica")
lbl_01.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_02 = Label(app, text="Direction: ", font="Helvetica")
lbl_02.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_03 = Label(app, text="Open Top font TTF: ", font="Helvetica")
lbl_03.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_04 = Label(app, text="Open Bottom font TTF: ", font="Helvetica")
lbl_04.grid(row=4, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_05 = Label(app, text="Top font size: ", font="Helvetica")
lbl_05.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_06 = Label(app, text="Bottom font size: ", font="Helvetica")
lbl_06.grid(row=6, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_07 = Label(app, text="Top texts (seperate lines by ^): ", font="Helvetica")
lbl_07.grid(row=7, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_08 = Label(app, text="Bottom texts (seperate lines by ^): ", font="Helvetica")
lbl_08.grid(row=8, column=0, columnspan=1, padx=5, pady=5, sticky="w")

btn_01 = Button(app, text="Open", command=cover_select_file)
btn_01.grid(row=1, column=1, columnspan=1, padx=5, pady=5)

btn_02 = Button(app, text="Open", command=topttf_select_file)
btn_02.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

btn_03 = Button(app, text="Open", command=bottomttf_select_file)
btn_03.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

btn_04 = Button(app, text="Save", command=generate_sample_box)
btn_04.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

txt_01 = Text(app, height=1, width=8, font="Helvetica")
txt_01.grid(row=2, column=1, padx=5, pady=5, sticky="w")

txt_02 = Text(app, height=1, width=8, font="Helvetica")
txt_02.grid(row=5, column=1, padx=5, pady=5, sticky="w")

txt_03 = Text(app, height=1, width=8, font="Helvetica")
txt_03.grid(row=6, column=1, padx=5, pady=5, sticky="w")

txt_04 = Text(app, height=1, width=8, font="Helvetica")
txt_04.grid(row=7, column=1, padx=5, pady=5, sticky="w")

txt_05 = Text(app, height=1, width=8, font="Helvetica")
txt_05.grid(row=8, column=1, padx=5, pady=5)

pb = Progressbar(app, orient='horizontal', mode='determinate', length=300)
pb.grid(row=10,column=0, padx=5, pady=5, columnspan=2)

app.mainloop()

# THINGS ARE CLOUDY O SO CLOUYD SINCE YOSU WETN AWAY :O :O :O: O O: O 
# ITS ALL FORGOTTEN NOW, THE TROUBLE AND THE PAIN :fire:
# bro the singer sounds like a woman because of the weird pitch

# D6 is the most fire thing on earth
# i love D6 so much

# that stardust melody...
# the melody of love's refrain.