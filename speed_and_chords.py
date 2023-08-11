import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have the MIDI data loaded into a pandas DataFrame named 'df'
# The 'notes' column holds a list of events describing the pianist's actions on the keyboard
from datasets import load_dataset

dataset = load_dataset("roszcz/internship-midi-data-science", split="train")
import pandas as pd

record = dataset[0]
df = pd.DataFrame(record["notes"])
print(df.head())
# Task 1: Time vs. Speed
# Calculate the duration of the record
duration = df['end'].max()
if duration > 120:
    duration_minutes = duration / 60
    time_unit = "Minutes"
else:
    duration_minutes = duration
    time_unit = "Seconds"

# Calculate the speed (notes played per second) for each note
df['speed'] = 1 / (df['end'] - df['start'])

# Create the chart
plt.figure(figsize=(10, 6))
plt.plot(df['start'], df['speed'], marker='o', linestyle='-', color='b')
plt.xlabel("Time ({})".format(time_unit))
plt.ylabel("Speed (Notes per Second)")
plt.title("Time vs. Speed - MIDI Recording")
plt.grid(True)
plt.show()

# Task 2: Number of Notes Pressed at the Same Time
# Experiment with different thresholds (number of simultaneous notes)
thresholds = [1, 2, 3, 4, 5]  # You can adjust the thresholds as per your preference
num_notes_pressed = []

for threshold in thresholds:
    # Count the number of notes pressed at the same time (based on the threshold)
    notes_pressed = df.groupby('start').size().reset_index(name='count')
    notes_pressed = notes_pressed[notes_pressed['count'] >= threshold]
    num_notes_pressed.append(len(notes_pressed))

# Create the chart
plt.figure(figsize=(10, 6))
plt.bar(thresholds, num_notes_pressed, color='g')
plt.xlabel("Threshold (Number of Simultaneous Notes)")
plt.ylabel("Number of Occurrences")
plt.title("Number of Notes Pressed Simultaneously - MIDI Recording")
plt.grid(True)
plt.show()
