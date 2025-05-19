from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/playlist?list=PLQ-uHSnFig5NiVuzlrKsrDbaPx3MO-v0V"

ydl_opts = {
    'outtmpl': '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])