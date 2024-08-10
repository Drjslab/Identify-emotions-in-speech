import torch
import torchaudio
import whisper


class Transcription:
    def __init__(self, modelType="base"):
        # Load the Whisper model
        self.model = whisper.load_model(modelType)
        
    def transcriptFromData(self,waveform,sample_rate):
        # Resample the audio if necessary
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)

        # Convert to numpy array as Whisper requires numpy array input
        audio_numpy = waveform.squeeze().numpy()

        # Transcribe the audio using Whisper
        result = self.model.transcribe(audio_numpy)
        transcription = result['text']
        return transcription        

    def transcriptFromFile(self, fileName, sample_rate):
        # Load the audio file
        waveform, sample_rate = torchaudio.load(fileName)
        return  transcriptFromData(waveform=waveform, sample_rate=sample_rate)
