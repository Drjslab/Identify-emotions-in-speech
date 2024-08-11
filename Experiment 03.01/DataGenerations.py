# Simple script to Generate Datasets

import os
import csv
import sys
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utility import Utility
from Transcription import Transcription
from SignalAnalysis import SignalAnalysis
# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def scan_directories(base_dir, csv_file):
    # Open the CSV file for writing
    transcription = Transcription()
    signalAnalysis = SignalAnalysis()
    utility = Utility()
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'File Path', 'Labels', "sample_rate", "emotions"])

        # Walk through the base directory
        for root, dirs, files in os.walk(base_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                emotion = file_name.split("-")[2]
                _,waveform, sample_rate = utility.readVoice(fileName=file_path)
                print(file_name)
                try:
                    output = transcription.transcript(waveform=waveform, sample_rate=sample_rate)
                    print(file_name, output, emotion)
                    writer.writerow([file_name, file_path, output, sample_rate, emotion])
                except Exception as e:
                    logging.error(f"Pygame error: {e} for file {file_name}")

if __name__ == "__main__":
    base_directory = f"{os.getcwd()}/RAVDEES"  # Use the current working directory
    output_csv = 'file_list.csv'  # Name of the output CSV file
    scan_directories(base_directory, output_csv)
    print(f"CSV file '{output_csv}' has been created.")
