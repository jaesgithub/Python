from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive = True, file_extension = 'mp4')
        highest_res_stream = stream.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Download complete.")

    except Exception as e:
        print(e)

url = "https://www.youtube.com/watch?v=K0Y8I24gXs4"
save_path = "/Users/jaewoongshin/Desktop"

download_video(url, save_path)