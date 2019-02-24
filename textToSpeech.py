import contextlib #To supress output of pygame import
with contextlib.redirect_stdout(None): #Supress output of pygame import
    from pygame import mixer #Playing music
    import pygame
from gtts import gTTS
import os
tts = gTTS(text='Good morning I am a sad robittt oh whale', lang='en')
tts.save("good.wav")
#os.system("mpg123 good.mp3")

mixer.init()
mixer.music.load("good.wav")
mixer.music.play()
