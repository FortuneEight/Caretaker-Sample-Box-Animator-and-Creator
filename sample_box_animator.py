from pydub import AudioSegment
import PIL.Image
import base64
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import os
import time
import moviepy.audio.io.AudioFileClip
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
import moviepy.video.io.ImageSequenceClip
import winsound
import threading
import queue
from functools import partial

from tkinter.filedialog import *

IMAGE_FILE_PATH = None
AUDIO_FILE_PATH = None
FOLDER_FILE_PATH = None
SAVE_FILE_PATH = None

os.system("cls")

app = Tk()
q = queue.Queue()

# Always have it on top
app.attributes('-topmost', True)
app.title("F8's Sample Box Animator")

icon = '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'
app.iconphoto(True, PhotoImage(data=icon, format="png"))

# copied from geeksforgeeks lol
def moving_average(array, window_size):
    moving_averages = []
    i = 0
    while i < len(array):
        window = array[i : min(i + window_size, len(array) - 1)]
        window_average = sum(window) / window_size
        moving_averages.append(window_average)
        i += 1
    return moving_averages

chunk_length = 1 # chunk_length is defined in seconds in case you think of changing this param


def normalize(array):
    maximum = max(array)
    multiplier = 1 / maximum
    new_array = []
    for item in array:
        item *= multiplier
        new_array.append(item)
    return new_array


def sample_box(img_file_name, sng_file_name, image_folder, smoothness, framerate, img_scale, normalize_opt, add_audio, save_video, q, app):
    asset = PIL.Image.open(img_file_name)
    w, h = asset.size

    song = AudioSegment.from_file(sng_file_name)

    leng = int(song.duration_seconds * 1000)

    vol_levels = []
    i = 0
    while i < leng:
        try:
            vol_level = 10 ** (song[round(i)].dBFS / 20)
            vol_levels.append(min(vol_level, 1))
        except:
            vol_levels.append(0)
        i += 1000 / framerate

    print(max(vol_levels), min(vol_levels))

    if normalize_opt == 1:
        vol_levels = normalize(vol_levels)

    vol_levels = moving_average(vol_levels, smoothness)

    if normalize_opt == 1:
        vol_levels = normalize(vol_levels)

    i = 0
    images = []
    start = time.time()
    for value in vol_levels:
        temp_img = asset
        temp_img.putalpha(int(value * 255))
        temp_size = (int(round(img_scale * w)), int(round(img_scale * h)))
        temp_img = temp_img.resize((int(s*img_scale) for s in temp_img.size))

        bg = PIL.Image.new("RGB", temp_img.size, (0, 0, 0))
        bg.paste(temp_img, temp_img) 
        bg.save(f"{image_folder}\image{str(i).zfill(6)}.jpg")
        images.append("image" + str(i).zfill(6) + ".jpg")
        i += 1
        # print(str(i) + "/" + str(len(vol_levels)) + " images generated (" + str(round(i/len(vol_levels)*100, 2)) + "%).")
        q.put((50*i)/len(vol_levels))
        app.event_generate("<<Progress>>")
        # update_progress_bar((50*i)/len(vol_levels))
    end = time.time()

    os.chdir(image_folder)
    temp_videos = []

    for i in range(int(len(images)/(framerate * chunk_length) + 1)):
        temp_clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images[framerate * chunk_length*i : min(framerate * chunk_length*(i + 1), len(images))], fps=framerate)
        temp_clip.write_videofile(f"{image_folder}/temp_video{str(i).zfill(6)}.mp4")
        temp_videos.append(VideoFileClip(str(image_folder) + "/temp_video" + str(i).zfill(6) + ".mp4"))
        # print(str(int(i + 1)) + "/" + str(int(len(images)/(framerate * chunk_length) + 1)) + " chunks rendered (" + str(round(100*(i+1)/(int(len(images)/(framerate * chunk_length) + 1)), 2)) + "%).")
        q.put(((50*(i+1))/(int(len(images)/(framerate * chunk_length) + 1))) + 50)
        # update_progress_bar(((50*(i+1))/(int(len(images)/(framerate * chunk_length) + 1))) + 50)
        app.event_generate("<<Progress>>")

    clip = concatenate_videoclips(temp_videos)

    if add_audio == "y":
        audioclip = AudioFileClip(sng_file_name)
        new_audioclip = CompositeAudioClip([audioclip])
        clip.audio = new_audioclip

    clip.write_videofile(f"{save_video}")

    for fname in os.listdir(image_folder):
        if fname.startswith("image") or fname.startswith("temp_video"):
            os.remove(os.path.join(image_folder, fname))

    winsound.Beep(440, 1000)

def openaudio():
    global AUDIO_FILE_PATH
    files = [('All files', '*.*'), ('MPEG audio Layer-3 (MP3) files', '*.mp3'), ('Microsoft Wave files', '*.wav'), ('Free Lossless Audio Codec (FLAC) files', '*.flac')]
    file = fd.askopenfilename(filetypes = files, defaultextension = files, title = 'Select audio file...', parent = app)
    AUDIO_FILE_PATH = file
    return file

def openimage():
    global IMAGE_FILE_PATH
    files = [('All files', '*.*'), ('PNG files', '*.png'), ('JPEG files', '*.jpeg'), ('JPG files', '*.jpg')]
    file = fd.askopenfilename(filetypes = files, defaultextension = files, title = 'Select image file...', parent = app)
    IMAGE_FILE_PATH = file
    return file

def savevideo():
    global SAVE_FILE_PATH
    files = [('Moving Picture Expert Group-4 (MP4) file', '*.mp4')]
    file = fd.asksaveasfilename(filetypes = files, defaultextension = files, title = 'Save video as...', parent = app)
    SAVE_FILE_PATH = file
    return file

def temp_image_folder():
    global FOLDER_FILE_PATH
    folder = fd.askdirectory(title = 'Select image/video folder...', parent = app)
    FOLDER_FILE_PATH = folder
    return folder

def checkRescale():
    if rescale.get() == 1:
        txt_03.config(state=NORMAL, background="white")
        return
    txt_03.config(state=DISABLED, background="light gray")

def generate_sbox_video():
    global IMAGE_FILE_PATH
    global AUDIO_FILE_PATH
    global FOLDER_FILE_PATH
    global SAVE_FILE_PATH
    global q
    global app
    savevideo()
    smoothness = int(txt_01.get(1.0, "end-1c"))
    fps = int(txt_02.get(1.0, "end-1c"))
    rescale_val = 1 if rescale.get() == 0 else int(txt_03.get(1.0, "end-1c")) / 100
    normal_val = normal.get()
    add_selected_val = "y" if add_selected.get() == 1 else "n"
    thread = threading.Thread(target=sample_box, args=(IMAGE_FILE_PATH, AUDIO_FILE_PATH, FOLDER_FILE_PATH, smoothness, fps, rescale_val, normal_val, add_selected_val, SAVE_FILE_PATH, q, app), daemon=True)
    thread.start()

def update_progress_bar(pb, q, event):
    pb['value'] = q.get()

rescale = IntVar()
normal = IntVar()
add_selected = IntVar()

lbl_title = Label(app, text = "F8's Sample Box Animator", font="Helvetica 18 bold")
lbl_title.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

lbl_01 = Label(app, text="Open Asset File: ", font="Helvetica")
lbl_01.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_02 = Label(app, text="Open Comparison Audio: ", font="Helvetica")
lbl_02.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_03 = Label(app, text="Open Temporary Image Folder: ", font="Helvetica")
lbl_03.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_04 = Label(app, text="Smoothness (integer): ", font="Helvetica")
lbl_04.grid(row=4, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_04 = Label(app, text="FPS (integer): ", font="Helvetica")
lbl_04.grid(row=5, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_05 = Label(app, text="Rescale video? ", font="Helvetica")
lbl_05.grid(row=6, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_06 = Label(app, text="\tPercentage to rescale to: ", font="Helvetica")
lbl_06.grid(row=7, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_07 = Label(app, text="Normalize Volume? ", font="Helvetica")
lbl_07.grid(row=8, column=0, columnspan=1, padx=5, pady=5, sticky="w")

lbl_08 = Label(app, text="Add selected audio to video? ", font="Helvetica")
lbl_08.grid(row=9, column=0, columnspan=1, padx=5, pady=5, sticky="w")


btn_01 = Button(app, text="Open Image", command=openimage)
btn_01.grid(row=1, column=1, columnspan=1, padx=5, pady=5, sticky="w")

btn_02 = Button(app, text="Open Audio", command=openaudio)
btn_02.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="w")

btn_03 = Button(app, text="Open Folder", command=temp_image_folder)
btn_03.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky="w")

btn_04 = Button(app, text="Save Video", command=generate_sbox_video)
btn_04.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

txt_01 = Text(app, height=1, width=8, font="Helvetica")
txt_01.grid(row=4, column=1, padx=5, pady=5, sticky="w")

txt_02 = Text(app, height=1, width=8, font="Helvetica")
txt_02.grid(row=5, column=1, padx=5, pady=5, sticky="w")

txt_03 = Text(app, height=1, width=8, font="Helvetica", state=DISABLED, background="light gray")
txt_03.grid(row=7, column=1, padx=5, pady=5, sticky="w")

chk_01 = Checkbutton(app, variable=rescale, onvalue=1, offvalue=0, command=checkRescale)
chk_01.grid(row=6, column=1, padx=5, pady=5)

chk_02 = Checkbutton(app, variable=normal, onvalue=1, offvalue=0)
chk_02.grid(row=8, column=1, padx=5, pady=5)

chk_03 = Checkbutton(app, variable=add_selected, onvalue=1, offvalue=0)
chk_03.grid(row=9, column=1, padx=5, pady=5)

pb = Progressbar(app, orient='horizontal', mode='determinate', length=350)
pb.grid(row=11,column=0, padx=5, pady=5, columnspan=2)

update_handler = partial(update_progress_bar, pb, q)
app.bind('<<Progress>>', update_handler)

app.mainloop()