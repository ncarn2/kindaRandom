import contextlib #To supress output of pygame import
with contextlib.redirect_stdout(None): #Supress output of pygame import
    from pygame import mixer #Playing music
    import pygame
from gtts import gTTS
import time

words = 'Good morning I am a sad robit oh whale,,,'
file = "quote.mp3"


tts = gTTS(text=words, lang='en')
tts.save(file)

mixer.init()
mixer.music.load(file)
mixer.music.play()

while mixer.music.get_busy():
    time.sleep(0.1) #Decrease cpu effort

mixer.quit()
