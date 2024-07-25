from fastapi import FastAPI, HTTPException
from models import TextToSpeechRequest
from tts_utils import convert_text_to_audio
from tts_models import tacotron2_model, hifigan_model, device
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/synthesize")
async def synthesize_speech(request: TextToSpeechRequest):
    """Convert text to speech and return the raw audio data as a hexadecimal string."""
    try:
        audio_buffer = convert_text_to_audio(tacotron2_model, hifigan_model, device, request.text)
        audio_data = audio_buffer.read()
        audio_hex = audio_data.hex()
        return {"audio": audio_hex}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
