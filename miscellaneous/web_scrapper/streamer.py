import vlc
import requests
import re

url = "https://www.youtube.com/watch?v=yQfdYIDc5Mg"

def extract_links(html):
    return re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', html)

def play_songs(songs):
    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    player.set_fullscreen(True)
    player.set_fullscreen(False)

    for song in songs:
        media = instance.media_new(song)
        player.set_media(media)
        player.play()
        while player.get_state() != vlc.State.Ended:
            continue

html = requests.get(url).text
songs = extract_links(html)
play_songs(songs)