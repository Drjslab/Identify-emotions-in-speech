import matplotlib.pyplot as plt
import torchaudio
import torchaudio.functional as F

class SignalAnalysis:
    def __init__(self):
        pass
    
    def showSignal(self, waveform, sample_rate):
        plt.figure(figsize=(10,4))
        plt.plot(waveform.t().numpy())
        plt.title("Waveform")
        plt.xlabel("Time (samples)")
        plt.ylabel("Amplitude")
        plt.show()


    def showSpectrogram(self, spectrogramData):
        plt.figure(figsize=(10, 4))
        plt.imshow(spectrogramData.log2().numpy(), cmap="viridis", origin="lower", aspect="auto")
        plt.colorbar(format="%+2.0f dB")
        plt.title("Spectrogram")
        plt.xlabel("Time")
        plt.ylabel("Frequency")
        plt.show()


    def showPitch(self, pitchData):
        print("#"*10)
        print("To be Implemented...")
        print("#"*10)
        