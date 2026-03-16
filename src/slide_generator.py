
def generate_slides(text):
    lines = text.split("\n")
    slides = []
    for i in range(0, len(lines), 3):
        slides.append({
            "title": f"Slide {len(slides)+1}",
            "content": " ".join(lines[i:i+2]),
            "script": " ".join(lines[i:i+2])
        })
    return slides
