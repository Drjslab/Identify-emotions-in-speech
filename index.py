from Utility import Utility
from Transcription import Transcription


if __name__ == "__main__":
    utility = Utility()
    transcription = Transcription()

    _,waveform, sample_rate = utility.recordVoice(fileName="myAudio.wav")
    output = transcription.transcriptFromData(waveform=waveform, sample_rate=sample_rate)
    print(output)