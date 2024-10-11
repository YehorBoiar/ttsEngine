# TTS Engine

This is a Text-to-Speech (TTS) Engine API built using FastAPI. It provides endpoints for converting text to speech using two different models: a custom Coqui-AI VITS model and Amazon Polly. The application is designed to serve as a backend service for converting input text into speech and returning the audio data in hexadecimal format.

## Overview

The TTS Engine API allows users to synthesize speech from text using two models:

- **Standard TTS**: Utilizes a Coqui-AI VITS model to generate natural-sounding speech.
- **Polly TTS**: Leverages Amazon Polly to convert text into speech using AWS services.

Both endpoints return the audio data as a hexadecimal string that can be used in various applications for playback.

## Features

- **Custom Model Support**: Synthesize speech using the Coqui-AI VITS model.
- **AWS Polly Integration**: Utilize Amazon Polly for high-quality, cloud-based TTS.
- **CORS Enabled**: Allows cross-origin requests from any domain.
- **Hexadecimal Audio Output**: Returns audio data as a hex string for easy transfer and playback.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/tts-engine.git
   cd tts-engine

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up AWS credentials for Amazon Polly** (ensure you have valid AWS access keys):

```bash
export AWS_ACCESS_KEY_ID='your-access-key-id'
export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
export AWS_REGION='your-region'
```
Alternatively, you can configure AWS credentials using a ~/.aws/credentials file or AWS IAM roles if deployed on a cloud service.

5. **Run the application:**

```bash
uvicorn app:app --host 0.0.0.0 --port 8001 --reload
```

6. **Open your browser and navigate to `http://localhost:8001/docs` to access the interactive API documentation.**