import yt_dlp
import requests
import os
import uuid
import re

def _prepare_path(ext="mp4"):
    output_dir = "downloads"
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, f"{uuid.uuid4()}.{ext}")

def download_youtube(link):
    path = _prepare_path()
    try:
        with yt_dlp.YoutubeDL({'format': 'best[ext=mp4]', 'outtmpl': path, 'quiet': True}) as ydl:
            ydl.download([link])
        return path
    except Exception as e:
        return str(e)

def download_tiktok(link):
    try:
        session = requests.Session()
        headers = { "User-Agent": "Mozilla/5.0" }
        r = session.post("https://ttdownloader.com/req/", data={"url": link, "format": "", "token": ""}, headers=headers)
        links = re.findall(r'href="(https://[^"]+)"', r.text)
        video_links = [l for l in links if 'tiktok' in l and 'watermark' not in l]
        if not video_links:
            return None
        url = video_links[0]
        path = _prepare_path()
        with requests.get(url, stream=True) as r:
            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): f.write(chunk)
        return path
    except Exception as e:
        return str(e)

def download_instagram(link):
    path = _prepare_path()
    try:
        with yt_dlp.YoutubeDL({'format': 'best[ext=mp4]', 'outtmpl': path, 'quiet': True}) as ydl:
            ydl.download([link])
        return path
    except Exception as e:
        return str(e)

def download_facebook(link):
    path = _prepare_path()
    try:
        with yt_dlp.YoutubeDL({'format': 'best[ext=mp4]', 'outtmpl': path, 'quiet': True}) as ydl:
            ydl.download([link])
        return path
    except Exception as e:
        return str(e)

def download_twitter(link):
    path = _prepare_path()
    try:
        with yt_dlp.YoutubeDL({'format': 'best[ext=mp4]', 'outtmpl': path, 'quiet': True}) as ydl:
            ydl.download([link])
        return path
    except Exception as e:
        return str(e)

def download_soundcloud(link):
    path = _prepare_path("mp3")
    try:
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': path,
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return path
    except Exception as e:
        return str(e)