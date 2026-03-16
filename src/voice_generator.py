
from gtts import gTTS

def generate_voice(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)
    return output_file
