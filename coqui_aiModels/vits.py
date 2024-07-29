from TTS.api import TTS
from io import BytesIO
from pydub import AudioSegment
import os
import torch


def init_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

def generate_speech(tts, text: str):
    """Generate speech from text and return the audio in a BytesIO buffer."""
    with open("temp_output.wav", "wb") as f:
        tts.tts_to_file(text=text, file_path=f.name)
    
    audio_segment = AudioSegment.from_wav("temp_output.wav")
    mp3_buffer = BytesIO()
    audio_segment.export(mp3_buffer, format='mp3')
    mp3_buffer.seek(0)
    
    os.remove("temp_output.wav")
    
    return mp3_buffer

def synthesize_speech(text: str, device: str, model_name: str) -> BytesIO:
    tts = TTS(model_name).to(device)
    audio_buffer = generate_speech(tts, text)
    return audio_buffer
