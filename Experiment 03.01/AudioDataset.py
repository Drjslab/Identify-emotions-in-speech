import torch
from torch.utils.data import Dataset
import torchaudio
import pandas as pd 

class AudioDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        audio_file = self.data.iloc[idx,1]  # Assuming the first column is the audio file path
        label = self.data.iloc[idx, 2] 
        emotion = self.data.iloc[idx, 4]       # Assuming the second column is the label

        label = {"text": label, "emotions": emotion}

        waveform, sample_rate = torchaudio.load(audio_file)

        if self.transform:
            waveform = self.transform(waveform)

        return waveform, label
