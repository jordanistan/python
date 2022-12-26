# I use youtube for 2–3 hours every day sometimes even more. Most of my learnings come from youtube because it is free and contains a vast amount of information. There are certain videos that stand out from others that I want to store with me to watch later even when I don’t have an internet connection. This script does the job for me, by downloading the youtube video for me. It uses an external API to do the job.

# Libraries:-
# pytube, is a lightweight Python library for downloading youtube videos.
# Tkinter, is one of the most famous and useful GUI Development Library That Makes It Super Easy to Create Awesome GUIs With Fewer Efforts.

# Why Tkinter:-
# The Whole Concept of the script is to create an interface through which you can download youtube videos by just putting a link. That Interface can’t be our CLI so we are going to create a simple GUI for our script. You Can make it even better by running your python code without a console with just one click.

from pytube import  YouTube  
import pytube  
try:
    video_url = 'https://www.youtube.com/watch?v=lTTajzrSkCw'   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download('C:/Users/abhay/Desktop/')  
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")