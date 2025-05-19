
from yt_dlp import YoutubeDL

url = "https://www.instagram.com/reel/DJoaAM1xE49/"

ydl_opts = {
    'outtmpl': 'downloads/instagram.mp4',
    'cookies': 'cookies.txt',
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])