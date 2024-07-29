from fastapi import FastAPI, HTTPException
from models import TextToSpeechRequest
import coqui_aiModels.vits as vits
from fastapi.middleware.cors import CORSMiddleware
from const import MODEL_NAME


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
        device = vits.init_device()
        audio_buffer = vits.synthesize_speech(request.text, device=device, model_name=MODEL_NAME)
        audio_data = audio_buffer.read()
        audio_hex = audio_data.hex()
        return {"audio": audio_hex}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
