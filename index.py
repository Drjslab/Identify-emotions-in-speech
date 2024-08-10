from Utility import Utility
from Transcription import Transcription


if __name__ == "__main__":
    transcription = Transcription()
    
    utility = Utility()
    _,waveform, sample_rate = utility.readVoice(fileName="myAudio.wav")
    output = transcription.transcript(waveform=waveform, sample_rate=sample_rate)

    print(output)

