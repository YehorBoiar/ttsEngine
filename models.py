from pydantic import BaseModel

class TextToSpeechRequest(BaseModel):
    text: str