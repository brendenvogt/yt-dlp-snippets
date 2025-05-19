from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    'format': 'bv+ba/best',
    'merge_output_format': 'mp4'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

