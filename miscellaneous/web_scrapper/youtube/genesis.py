import os
import pydub
from pydub import AudioSegment

# The directory containing the audio files
directory = "tracks/"

# Get the duration of the crossfade in milliseconds
fade_duration = 3000

# Create an empty audio segment to hold the mixed tracks
mixed_track = AudioSegment.empty()

# Track start times list
track_start_times = []

# Iterate through the files in the directory
for filename in os.listdir(directory):
    # Check if the file is an audio file
    if filename.endswith(".mp3"):
        # Open the audio file
        track = AudioSegment.from_file(directory + filename)
        # Fade in the track
        track = track.fade_in(fade_duration)
        # Add the track to the mixed track
        mixed_track = mixed_track + track
        # Append the start time of the track
        track_start_times.append(str(mixed_track.duration_seconds - track.duration_seconds))

# Add meta data to the output file
mixed_track.export("mixed_track.mp3", format="mp3", tags={
    "artist": "Various Artists",
    "album": "Mix Tape",
    "track_start_times": track_start_times
})
