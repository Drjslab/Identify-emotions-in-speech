from Utility import Utility
from Transcription import Transcription
from SignalAnalysis import SignalAnalysis
import torch


def detect_emotion(pitch, energy, duration):
    if pitch.mean() > 250 and energy.mean() > 0.5:
        return "Happiness"
    elif pitch.mean() < 150 and energy.mean() < 0.3 and duration > 1.5:
        return "Sadness"
    elif pitch.mean() > 300 and energy.mean() > 0.7 and duration < 1.0:
        return "Anger"
    else:
        return "Neutral"


if __name__ == "__main__":
    transcription = Transcription()
    signalAnalysis = SignalAnalysis()
    utility = Utility()
    _,waveform, sample_rate = utility.readVoice(fileName="03-01-08-01-01-01-04.wav")
    # _,waveform, sample_rate = utility.recordVoice(fileName="myAudio.wav")

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

    pitch, energy, duration = transcription.getProsodicFeature(waveform=waveform, sample_rate=sample_rate)
    print(pitch, energy, duration) 
    signalAnalysis.showPitch(pitch)

    emotion = detect_emotion(pitch, energy, duration )
    print(emotion)





