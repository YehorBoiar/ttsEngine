import os


MAX_TEXT_LENGTH = 150  
MODEL_NAME = 'tts_models/en/ljspeech/vits'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')