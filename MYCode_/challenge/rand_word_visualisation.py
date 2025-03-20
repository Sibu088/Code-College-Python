# main_script.py
import pandas as pd
import plotly.express as px
from rand_word import RandomWordGenerator  
import string

# Function to calculate letter frequencies
def calculate_letter_frequencies(words):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    for word in words:
        for letter in word:
            letter_counts[letter] += 1
    return letter_counts

# Generate random words and calculate frequencies
def generate_data(num_words=10000, min_len=3, max_len=8, num_frames=10):
    generator = RandomWordGenerator()
    frames_data = []

    for frame in range(num_frames):
        words = generator.generate_multiple_words(num_words, min_len, max_len)
        letter_counts = calculate_letter_frequencies(words)
        frame_data = pd.DataFrame(list(letter_counts.items()), columns=['Letter', 'Frequency'])
        frame_data['Frame'] = frame + 1  # Frame number for animation
        frames_data.append(frame_data)
    
    # Combine all frames into a single DataFrame
    return pd.concat(frames_data, ignore_index=True)

# Generate the dataset
data = generate_data()

# Create an animated bar chart using Plotly
fig = px.bar(
    data,
    x="Letter",
    y="Frequency",
    color="Letter",
    animation_frame="Frame",
    title="Animated Letter Frequency Distribution",
    labels={"Letter": "Alphabet", "Frequency": "Count"},
    color_discrete_sequence=px.colors.qualitative.Set1
)

# Customize appearance
fig.update_layout(
    xaxis_title="Letter",
    yaxis_title="Frequency",
    plot_bgcolor='whitesmoke'
)

# Show the animation
fig.show()