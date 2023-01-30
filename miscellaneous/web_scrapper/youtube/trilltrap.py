#
import youtube_dl

def download_video(url, path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{path}/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=36c9ZweCKFE"
    path = "/Users/jordan/projects/python-1/miscellaneous/web_scrapper/youtube/tracks"
    download_video(url, path)
