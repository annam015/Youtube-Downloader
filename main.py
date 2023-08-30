import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os


def download(url):
    try:
        YouTube(url).streams.filter(progressive=True).order_by('resolution').desc().first(). \
            download(output_path=os.path.expanduser('~/Downloads'), filename="video.mp4")
        messagebox.showinfo("Download Complete", "The video has been successfully downloaded to the Downloads folder.")
    except Exception as error:
        messagebox.showerror("Error", "An error occurred: " + str(error))
    inputTxt.delete("1.0", "end")


window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("450x200")

text = Label(window, text="Enter the URL:", font=("Helvetica", 18))
text.place(x=145, y=30)

inputTxt = tk.Text(window, height=1, width=45)
inputTxt.place(x=40, y=90)

downloadButton = tk.Button(window, text="Download", font=("Helvetica", 10),
                           command=lambda:download(inputTxt.get("1.0", "end")))
downloadButton.place(x=180, y=140)

window.mainloop()