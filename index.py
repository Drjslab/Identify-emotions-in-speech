from Utility import Utility
from Transcription import Transcription
from SignalAnalysis import SignalAnalysis
import torch


if __name__ == "__main__":
    transcription = Transcription()
    signalAnalysis = SignalAnalysis()
    utility = Utility()
    _,waveform, sample_rate = utility.readVoice(fileName="myAudio.wav")

    # output = transcription.transcript(waveform=waveform, sample_rate=sample_rate)
    # print(output)
    signalAnalysis.showSignal(waveform, sample_rate)

    # show Spectrogrph 
    spectrogramData = transcription.getSpectrogram(waveform=waveform)
    # signalAnalysis.showSpectrogram(spectrogramData=torch.abs(spectrogramData[0]))

    # [TODO] Update/Modify Spectorgram and generate reverse Waveform to save as File

    # inverse Spectrograph
    # inverSptec = transcription.inverseSpectrograpm(spectrogram=spectrogramData)
    # signalAnalysis.showSpectrogram(spectrogramData=torch.abs(inverSptec))
    # signalAnalysis.showSignal(waveform=inverSptec, sample_rate=sample_rate)
    # utility.saveVoice(fileName="new.wav", waveform=inverSptec, sample_rate=sample_rate)






