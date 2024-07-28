import soundfile as sf
from pydub import AudioSegment
import torch
from io import BytesIO
import numpy as np
from typing import List
from const import MAX_TEXT_LENGTH

def load_model(model_class, model_name: str, device: torch.device):
    """Load a pre-trained model and move it to the specified device."""
    model = model_class.from_pretrained(model_name=model_name)
    model.to(device)
    return model

def generate_spectrogram(tacotron2, sentence: str, device: torch.device) -> torch.Tensor:
    """Generate a spectrogram from a sentence using Tacotron2."""
    tokens = tacotron2.parse(sentence)
    with torch.no_grad():
        spectrogram = tacotron2.generate_spectrogram(tokens=tokens.to(device))
    return spectrogram

def convert_text_to_audio(tacotron2, hifigan, device: torch.device, text: str) -> BytesIO:
    """Convert text to audio using Tacotron2 and HiFi-GAN, and return the raw audio data as BytesIO."""
    if len(text) > MAX_TEXT_LENGTH:
        raise ValueError(f"Text length exceeds the maximum allowed length of {MAX_TEXT_LENGTH} characters.")
    
    spectrogram = generate_spectrogram(tacotron2, text, device)
    with torch.no_grad():
        audio = hifigan.convert_spectrogram_to_audio(spec=spectrogram)
    audio_numpy = audio.squeeze().cpu().numpy()
    
    # Save the audio as WAV in a buffer
    wav_buffer = BytesIO()
    sf.write(wav_buffer, audio_numpy, samplerate=22050, format='WAV')
    wav_buffer.seek(0)
    
    # Convert WAV to MP3
    audio_segment = AudioSegment.from_wav(wav_buffer)
    mp3_buffer = BytesIO()
    audio_segment.export(mp3_buffer, format='mp3')
    mp3_buffer.seek(0)
    
    return mp3_buffer