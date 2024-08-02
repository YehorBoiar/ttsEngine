from pydantic import BaseModel

class TextToSpeechRequest(BaseModel):
    text: str

class PollyTTSRequest(BaseModel):
    text: str
    region: str
    publicKey: str
    secretKey: str
    voice_id: str="Joanna"