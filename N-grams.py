import pandas as pd
from collections import defaultdict

# Assuming you have the MIDI data loaded into a pandas DataFrame named 'df'
# The 'notes' column holds a list of events describing the pianist's actions on the keyboard

# Calculate the note distances for each note event
df['note_distance'] = df['start'].diff()

# Choose the number of tokens used to quantize the note distance
# Let's choose 5 tokens for this example
num_tokens = 5

# Quantize the note distances into 'num_tokens' bins
df['note_distance_quantized'] = pd.cut(df['note_distance'], bins=num_tokens, labels=False)

# Find the most popular 2-grams, 3-grams, and 4-grams based on note distance
def find_ngrams(data, n):
    ngrams = defaultdict(int)
    for i in range(len(data) - n + 1):
        ngram = tuple(data[i:i + n])
        ngrams[ngram] += 1
    return ngrams

# Generate n-grams for the quantized note distances
two_grams = find_ngrams(df['note_distance_quantized'], 2)
three_grams = find_ngrams(df['note_distance_quantized'], 3)
four_grams = find_ngrams(df['note_distance_quantized'], 4)

# Sort the n-grams based on their frequency
sorted_two_grams = sorted(two_grams.items(), key=lambda x: x[1], reverse=True)
sorted_three_grams = sorted(three_grams.items(), key=lambda x: x[1], reverse=True)
sorted_four_grams = sorted(four_grams.items(), key=lambda x: x[1], reverse=True)

# Print the results
print("Most popular 2-grams based on note distance:")
for ngram, frequency in sorted_two_grams[:10]:
    print(ngram, frequency)

print("\nMost popular 3-grams based on note distance:")
for ngram, frequency in sorted_three_grams[:10]:
    print(ngram, frequency)

print("\nMost popular 4-grams based on note distance:")
for ngram, frequency in sorted_four_grams[:10]:
    print(ngram, frequency)
