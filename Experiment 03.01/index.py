# load Datasets and finetune 

from AudioDataset import AudioDataset
from torch.utils.data import DataLoader
from transformers import Wav2Vec2Processor

# load Dataset 
audioDataset = AudioDataset(csv_file="file_list.csv")
datas = DataLoader(audioDataset, shuffle=True)

# Load the processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")



