from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

with YoutubeDL() as ydl:
    info = ydl.extract_info(url, download=False)
    print(info['title'])
    print(info['duration'])
    print(info['uploader'])
