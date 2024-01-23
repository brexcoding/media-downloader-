import customtkinter
import os
from PIL import Image
from customtkinter import CTkOptionMenu
import yt_dlp
from tkinter import Tk




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
     
   
        self.title("BREXCoding")
        width = 400
        height = 460
        self.geometry(f"{width}x{height}")# setting the size of my app 
        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter The Youtube Url")
        self.entry.grid(row=1, column=2, columnspan=2, padx=(111, 120), pady=(50, 0), sticky="nsew")
        
        self.button = customtkinter.CTkButton(self, text="Download", command=self.download_it)
        self.button.grid(row=3, column=1, columnspan=2, padx=(111,120), pady=(50, 00), sticky="nsew" )

        self.dropdown = CTkOptionMenu(self, values=["audio", "video"])  # Replace with your options
        self.dropdown.grid(row=2, column=1, columnspan=2, padx=(111, 120), pady=(50, 0), sticky="nsew")

    def download_it(self):
        url = self.entry.get() 
        download_format = self.dropdown.get()
        print('starting download ...')
        # Replace with your desired output directoryz
        output_path = 'C:/Users/abdel/Desktop/brex_downloads'
        # Options for yt_dlp (YouTube Downloader)
        video = {
            'format': 'best',  # Select the best available format
            'outtmpl': output_path + '%(title)s.%(ext)s',  # Output file template
            'quiet': True,  # Suppress output messages
        }

        # Options for yt_dlp (YouTube Downloader)
        audio = {
            'format': 'bestaudio/best',  # Select the best audio quality
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extract audio using FFmpeg
                'preferredcodec': 'mp3',  # Convert to MP3 format
                'preferredquality': '192',  # Set audio quality
            }],
            'outtmpl': output_path + '%(title)s.%(ext)s',  # Output file template
            'quiet': True,  # Suppress output messages
            'ffmpeg_location': r'C:\Users\abdel\Desktop\venvs\dow\root\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin',  # Replace with your location of FFmpeg executable
        }

        if download_format == "audio":
            download_format = audio
        if download_format =="video":
            download_format = video

        # Initialize YouTube Downloader with the provided options
        with yt_dlp.YoutubeDL(download_format) as ydl:
            def download():
                try:
                    ydl.download([url])  # Download the video/audio
    
                except Exception as e:
                    print(f"Failed to download {url}: {e}")
               
        print('downloading ...')
        download() 
            
         

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
