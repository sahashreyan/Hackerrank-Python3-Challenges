import pytube
from pytube import YouTube

video_link = input("Enter the video link here: ")
yt = pytube.YouTube(video_link)

video = yt.streams.first()
#Add the path where the video will be saved in the next line
video.download("Add path here")

print("Downloaded 😁")
