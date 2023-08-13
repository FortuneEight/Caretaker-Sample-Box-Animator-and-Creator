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
TRANSPARENT_BACKGROUND = None

# FORTUNE SETTINGS
# Tahoma Bold for Top Font (53 pt)
# Tahoma Regular for Bottom Font (46 pt)


def sample_box_creator(cover_file_path, direction, top_font_ttf, top_font_size, bottom_font_ttf, bottom_font_size, top_texts, bottom_texts, save_file_name, transparent):
    rect_shape = [(320, 193), (759.9, 632.9)]

    # create new transparent image
    if transparent == True:
        main_img = img.new('RGBA', (1080,1080), (0,0,0,0))
    else:
        main_img = img.new('RGB', (1080,1080), (0,0,0))

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
        if transparent == False:
            draw.rectangle(bbox, fill="black")
        draw.text(position, top_texts[i], font=top_font, fill=(255,255,255))
        if i == len(top_texts) - 1:
            y_val += (bottom_font_px)
        else:
            y_val += (top_font_px)

    # add bottom text(s) - creator, album, year
    for i in range(len(bottom_texts)):
        w = draw.textlength(bottom_texts[i], font=bottom_font)
        position = ((1080 - w) / 2, y_val)
        bbox = draw.textbbox(position, bottom_texts[i], font=bottom_font)
        if transparent == False:
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
    global TRANSPARENT_BACKGROUND

    update_progress_bar(0)

    direction = int(txt_01.get(1.0, "end-1c"))
    top_font_size = int(txt_02.get(1.0, "end-1c"))
    bottom_font_size = int(txt_03.get(1.0, "end-1c"))
    top_texts = txt_04.get(1.0, "end-1c").split("^")
    bottom_texts = txt_05.get(1.0, "end-1c").split("^")
    TRANSPARENT_BACKGROUND = True if var1.get() == 1 else False

    filetypes = [("PNG Files", "*.png")]
    SAVE_FILE_NAME = fd.asksaveasfilename(title="Save as PNG File", filetypes=filetypes)

    update_progress_bar(50)

    sample_box_creator(COVER_FILE_PATH, direction, TOP_FONT_TTF_PATH, top_font_size, BOTTOM_FONT_TTF_PATH, bottom_font_size, top_texts, bottom_texts, SAVE_FILE_NAME, TRANSPARENT_BACKGROUND)

    update_progress_bar(100)

    showinfo(message="File saved successfully!")

app = Tk()
app.title("F8's Sample Box Generator")

ic = "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"


app.iconphoto(True, PhotoImage(data=ic))

var1 = IntVar()

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

lbl_09 = Label(app, text="Transparent background? ", font="Helvetica")
lbl_09.grid(row=9, column=0, columnspan=1, padx=5, pady=5, sticky="w")

btn_01 = Button(app, text="Open", command=cover_select_file)
btn_01.grid(row=1, column=1, columnspan=1, padx=5, pady=5, sticky="e")

btn_02 = Button(app, text="Open", command=topttf_select_file)
btn_02.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="e")

btn_03 = Button(app, text="Open", command=bottomttf_select_file)
btn_03.grid(row=4, column=1, columnspan=1, padx=5, pady=5, sticky="e")

btn_04 = Button(app, text="Save", command=generate_sample_box)
btn_04.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

txt_01 = Text(app, height=1, width=8, font="Helvetica")
txt_01.grid(row=2, column=1, padx=5, pady=5, sticky="e")

txt_02 = Text(app, height=1, width=8, font="Helvetica")
txt_02.grid(row=5, column=1, padx=5, pady=5, sticky="e")

txt_03 = Text(app, height=1, width=8, font="Helvetica")
txt_03.grid(row=6, column=1, padx=5, pady=5, sticky="e")

txt_04 = Text(app, height=2, width=18, font="Helvetica")
txt_04.grid(row=7, column=1, padx=5, pady=5, sticky="e")

txt_05 = Text(app, height=2, width=18, font="Helvetica")
txt_05.grid(row=8, column=1, padx=5, pady=5, sticky="e")

chk_01 = Checkbutton(app, variable=var1, onvalue=1, offvalue=0)
chk_01.grid(row=9, column=1, padx=5, pady=5)

pb = Progressbar(app, orient='horizontal', mode='determinate', length=350)
pb.grid(row=11,column=0, padx=5, pady=5, columnspan=2)

app.mainloop()

# THINGS ARE CLOUDY O SO CLOUYD SINCE YOSU WETN AWAY :O :O :O: O O: O 
# ITS ALL FORGOTTEN NOW, THE TROUBLE AND THE PAIN :fire:
# bro the singer sounds like a woman because of the weird pitch

# D6 is the most fire thing on earth
# i love D6 so much

# that stardust melody...
# the melody of love's refrain.