from datasets import load_dataset
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
import Levenshtein

# Load the MIDI dataset
dataset = load_dataset("roszcz/internship-midi-data-science", split="train")

# Function to calculate the Edit distance between two sequences
def calculate_edit_distance(seq1, seq2):
    return Levenshtein.distance(seq1, seq2)

# Function to calculate the DTW distance between two sequences
def calculate_dtw_distance(seq1, seq2):
    distance, _ = fastdtw(seq1, seq2, dist=euclidean)
    return distance

# Function to find similar sequences inside all available records
def find_similar_sequences(target_sequence, dataset, similarity_metric):
    similar_sequences = []

    for record in dataset:
        sequence = record["notes"]
        similarity = similarity_metric(target_sequence, sequence)
        similar_sequences.append((record, similarity))

    # Sort the similar sequences by their similarity score
    similar_sequences.sort(key=lambda x: x[1])
    return similar_sequences

# Example usage:
# Assume 'target_sequence' is the sequence of notes that we want to find similar sequences to
target_sequence = [60, 62, 64, 65, 67]
similar_sequences_edit_distance = find_similar_sequences(target_sequence, dataset, calculate_edit_distance)
similar_sequences_dtw = find_similar_sequences(target_sequence, dataset, calculate_dtw_distance)

# Print the results
print("Similar sequences using Edit distance:")
for record, similarity in similar_sequences_edit_distance[:5]:
    print("Similarity:", similarity)
    print("Notes:", record["notes"])

print("\nSimilar sequences using DTW:")
for record, similarity in similar_sequences_dtw[:5]:
    print("Similarity:", similarity)
    print("Notes:", record["notes"])
