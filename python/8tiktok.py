from yt_dlp import YoutubeDL

url = "https://www.tiktok.com/@dudeperfect/video/7491728228093152558"

with YoutubeDL({'outtmpl': 'tiktok/%(title)s.%(ext)s'}) as ydl:
    ydl.download([url])