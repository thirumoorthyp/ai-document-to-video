
# AI Document to Video Generator (POC)

## Overview
This project converts a document (DOCX/TXT) into a narrated video automatically using AI concepts.
Pipeline:
Document → Text Extraction → Slide Generation → Voice Over → Video

## Features
- Document text extraction
- Slide generation
- AI-ready architecture
- Text-to-speech narration
- Video generation
- Modular Python structure

## Project Structure
src/
  main.py
  extractor.py
  slide_generator.py
  voice_generator.py
  video_generator.py
  utils/
samples/
output/

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python src/main.py samples/sample.txt
```

Output video will appear in `/output`.

## Optimization
- Modular architecture
- Streaming text processing
- Efficient slide rendering
- Lazy loading of resources

## Security Considerations
- Input validation for document files
- Path sanitization
- No external command execution
- Environment variable support for API keys

## Performance Improvements
- Batch slide rendering
- Parallel audio generation (future enhancement)
- Caching processed documents
- GPU-based video rendering (optional)

## Future Enhancements
- PDF support
- Real AI voice synthesis
- Animated slides
- Web UI

