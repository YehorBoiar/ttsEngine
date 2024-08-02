from fastapi import FastAPI, HTTPException
from models import TextToSpeechRequest, PollyTTSRequest
import coqui_aiModels.vits as vits
from fastapi.middleware.cors import CORSMiddleware
from const import MODEL_NAME
import boto3
import logging
from botocore.exceptions import BotoCoreError, ClientError


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/standard")
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

@app.post("/polly")
def synthesize_polly_speech(request: PollyTTSRequest):
    logger.info("Received request for Polly TTS synthesis")
    logger.info(f"Request text: {request.text}")
    logger.info(f"Using AWS region: {request.region}")
    logger.info(f"Voice ID: {request.voice_id}")
    
    try:
        polly_client = boto3.client(
            'polly',
            aws_access_key_id=request.publicKey,
            aws_secret_access_key=request.secretKey,
            region_name=request.region
        )
        logger.info("Polly client initialized successfully")

        response = polly_client.synthesize_speech(
            Text=request.text,
            OutputFormat='mp3',
            VoiceId=request.voice_id
        )
        logger.info("Polly synthesis request sent successfully")

        if "AudioStream" in response:
            audio_stream = response["AudioStream"].read()
            logger.info("Audio stream received successfully")
            return {"audio": audio_stream.hex()}
        else:
            logger.error("Error in synthesizing speech: No AudioStream in response")
            raise HTTPException(status_code=500, detail="Error in synthesizing speech")

    except (BotoCoreError, ClientError) as error:
        logger.error(f"Exception during Polly TTS synthesis: {error}")
        raise HTTPException(status_code=500, detail=str(error))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
