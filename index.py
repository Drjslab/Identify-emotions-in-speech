from Utility import Utility
from Transcription import Transcription
from SignalAnalysis import SignalAnalysis


if __name__ == "__main__":
    transcription = Transcription()
    signalAnalysis = SignalAnalysis()
    utility = Utility()
    _,waveform, sample_rate = utility.readVoice(fileName="myAudio.wav")
    # output = transcription.transcript(waveform=waveform, sample_rate=sample_rate)
    # print(output)
    # signalAnalysis.showSignal(waveform, sample_rate)

    # show Spectrogrph 
    spectrogramData = transcription.getSpectrogram(waveform=waveform)
    inverSptec = transcription.inverseSpectrograpm(spectrogram=spectrogramData, sample_rate=sample_rate)
    print("inverSptec", inverSptec)
    # signalAnalysis.showSpectrogram(spectrogramData=spectrogramData)
    # signalAnalysis.showSpectrogram(spectrogramData=inverSptec)






