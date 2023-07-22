from pydub import AudioSegment
from PIL import Image
import os
import time
import moviepy.video.io.ImageSequenceClip
import winsound

os.system("cls")

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


def normalize(array):
    maximum = max(array)
    multiplier = 1 / maximum
    new_array = []
    for item in array:
        item *= multiplier
        new_array.append(item)
    return new_array


def sample_box(requested_function):
    if requested_function == 0:
        img_file_name = input("What is the file name of the image? ")
        asset = Image.open(img_file_name)

        sng_file_name = input("What is the file name of the comparison mp3/wav/flac? ")
        song = AudioSegment.from_file(sng_file_name)

        smoothness = int(
            input(
                "How smooth do you want the animation to be? (24 is recommended, 10 or less is 'snappy', more is smoother.) "
            )
        )

        normalize_opt = int(
            input("Would you like to normalize the volumes? Y=1, N=0: ")
        )

        leng = int(song.duration_seconds * 1000)

        print("Calculating Volume Levels...")
        vol_levels = []
        i = 0
        while i < leng:
            try:
                vol_level = 10 ** (song[round(i)].dBFS / 20)
                vol_levels.append(min(vol_level, 1))
            except:
                vol_levels.append(0)
            i += 1000 / 60

        print(max(vol_levels), min(vol_levels))

        if normalize_opt == 1:
            print("Normalizing Volumes 1...")
            vol_levels = normalize(vol_levels)

        print("Calculating Moving Averages...")
        vol_levels = moving_average(vol_levels, smoothness)

        if normalize_opt == 1:
            print("Normalizing Volumes 2...")
            vol_levels = normalize(vol_levels)

        print("Amount of Images = " + str(len(vol_levels)))
        print(
            "Approximate amount of storage needed for images: "
            + str(len(vol_levels) * 358)
            + " KB."
        )
        # print(f"Approximate amount of storage needed for avi video: {str(len(vol_levels) * 1709)} KB.")
        print(
            f"Approximate amount of storage needed for mp4 video: {str(len(vol_levels) * 4)} KB."
        )
        print(
            "Approximate amount of time needed: "
            + str(round(len(vol_levels) * 0.01905349, 2))
            + " seconds."
        )

        if (
            input("Are you sure you want to continue? Type 'y' if you are sure. ")
            == "y"
        ):
            print("Saving Pictures to /Sample_Box_Images directory...")
            i = 0
            percent_hit = int(len(vol_levels) / 10)
            images = []
            start = time.time()
            for value in vol_levels:
                temp_img = asset
                temp_img.putalpha(int(value * 255))
                bg = Image.new("RGB", temp_img.size, (0, 0, 0))
                bg.paste(temp_img, temp_img)
                bg.save(f"Sample_Box_Images\image{str(i).zfill(6)}.jpg")
                i += 1
                if i % percent_hit == 0:
                    print(f"{round((i / len(vol_levels)) * 100)}% complete.")
            end = time.time()
            print(f"Time elapsed in seconds: {round(end - start, 2)}")

    if requested_function == 1:
        vid_file_name = input("What would you like to name the video? ")
        image_folder = input("What is the image_folder? ")  # make sure to use your folder
        save_folder = input("Where would you like to save the video to? ")
        print("Generating Video and Saving...")

        # video_name = f'{vid_file_name}.avi'
        os.chdir(image_folder)

        images = [
            img
            for img in os.listdir(image_folder)
            if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")
        ]

        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps=60)
        clip.write_videofile(f"{save_folder}{vid_file_name}.mp4")


sample_box(0)
sample_box(1)
winsound.Beep(440, 10)