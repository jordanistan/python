import pydub
from pydub import AudioSegment

# Open the large audio file
large_audio = AudioSegment.from_file("large_audio.mp3")

# Get the meta data of the large audio file
meta_data = large_audio.meta_data

# Get the track start times from the meta data
track_start_times = meta_data["track_start_times"]

# Iterate through the track start times
for i, start_time in enumerate(track_start_times):
    # Get the start and end times of the track
    start_time = int(start_time) * 1000
    end_time = (int(start_time) + int(track_duration)) * 1000
    # Extract the track from the large audio file
    track = large_audio[start_time:end_time]
    # Export the track to a new file
    track.export(f"track{i+1}.mp3", format="mp3")
