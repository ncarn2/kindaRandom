import contextlib #To supress output of pygame import
with contextlib.redirect_stdout(None): #Supress output of pygame import
    from pygame import mixer #Playing music
    import pygame
from gtts import gTTS
import os
import system
import sys

operatingSystem = sys.platform
print ("Operating System: " + operatingSystem)

words = 'Good morning I am a sad robittt oh whale'
tts = gTTS(text=words, lang='en')
tts.save("good.mp3")
#os.system("mpg123 good.mp3")

mixer.init()
mixer.music.load("good.mp3")
mixer.music.play()
