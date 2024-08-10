import torch
import torchaudio
import whisper
import torchaudio.transforms as T
import torchaudio.functional as F


class Transcription:
    def __init__(self, modelType="base"):
        # Load the Whisper model
        self.model = whisper.load_model(modelType)
        
    def transcript(self,waveform,sample_rate):
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
    
    def getSpectrogram(self, waveform):
        # spectrogram = torchaudio.transforms.Spectrogram()(waveform)
        transform = T.Spectrogram(n_fft=1024, win_length=None, hop_length=None, power=None)
        spectrogram = transform(waveform)
        return spectrogram
    
    def inverseSpectrograpm(self, spectrogram):
        # Convert spectrogram back to waveform using ISTFT
        inverse_transform = T.InverseSpectrogram(n_fft=1024, win_length=None, hop_length=None)
        reconstructed_waveform = inverse_transform(spectrogram)
        return reconstructed_waveform
    
    def getProsodicFeature(self, waveform, sample_rate):
        # Define the transform to extract pitch
        pitch =  F.detect_pitch_frequency(waveform, sample_rate)


        energy = torch.sqrt(torch.mean(waveform**2, dim=1))
        duration = waveform.size(1) /sample_rate

        return pitch, energy, duration

