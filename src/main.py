
import sys
from extractor import extract_text
from slide_generator import generate_slides
from voice_generator import generate_voice
from video_generator import create_video

def run_pipeline(input_file):
    text = extract_text(input_file)
    slides = generate_slides(text)

    videos = []
    for i, slide in enumerate(slides):
        audio = generate_voice(slide["script"], f"output/audio_{i}.mp3")
        video = create_video(slide["title"], slide["content"], audio, f"output/video_{i}.mp4")
        videos.append(video)

    print("Video generation completed")

if __name__ == "__main__":
    run_pipeline(sys.argv[1])
