from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'skip_download': True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])