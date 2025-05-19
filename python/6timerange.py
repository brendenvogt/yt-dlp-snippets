from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

ydl_opts = {
    'download_ranges': lambda info_dict, ydl: [{'start_time': 30, 'end_time': 90}],
    'outtmpl': 'clip.%(ext)s'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
