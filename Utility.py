import torch
import torchaudio
import sounddevice as sd

class Utility:
    def __init__(self):
        pass
    
    def recordVoice(self, fileName):
        # Parameters
        duration = 10  # seconds
        sample_rate = 44100  # Sample rate in Hz

        # Record audio
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")

        # Convert to tensor
        audio_tensor = torch.from_numpy(audio_data).squeeze()

        # Save the recording as a WAV file using torchaudio
        torchaudio.save(fileName, audio_tensor.unsqueeze(0), sample_rate)
        print(f"Audio saved as {fileName}")
        return fileName, audio_tensor, sample_rate
