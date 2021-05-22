from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

video = askopenfilename()
clip = VideoFileClip(video)
clip.write_gif("mygif.gif", fps = 10)
#Download the packages if you do not have them installed previously. 
#Just Run this code and select the correct file

