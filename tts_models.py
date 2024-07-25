import nltk
import nemo.collections.tts as nemo_tts
import torch


nltk.download('punkt')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tacotron2_model_name = 'tts_en_tacotron2'  
hifigan_model_name = 'tts_en_hifigan'  

tacotron2_model = nemo_tts.models.Tacotron2Model.from_pretrained(model_name=tacotron2_model_name)
tacotron2_model.to(device)

hifigan_model = nemo_tts.models.HifiGanModel.from_pretrained(model_name=hifigan_model_name)
hifigan_model.to(device)