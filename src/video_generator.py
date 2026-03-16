
from moviepy.editor import *
from PIL import Image, ImageDraw

def create_slide(title, text, file):
    img = Image.new("RGB", (1280,720), "white")
    draw = ImageDraw.Draw(img)
    draw.text((100,100), title, fill="black")
    draw.text((100,250), text, fill="black")
    img.save(file)

def create_video(title, text, audio_file, output):
    slide_file = "temp_slide.png"
    create_slide(title, text, slide_file)
    audio = AudioFileClip(audio_file)
    clip = ImageClip(slide_file).set_duration(audio.duration)
    video = clip.set_audio(audio)
    video.write_videofile(output, fps=24)
    return output
