import contextlib #To supress output of pygame import
with contextlib.redirect_stdout(None): #Supress output of pygame import
    from pygame import mixer #Playing music
    import pygame
from gtts import gTTS
import time
import lxml
import urllib.request
from bs4 import BeautifulSoup
import random
import speech_recognition as sr
from pathlib import Path
import os
import contextlib
with contextlib.redirect_stdout(None):
    import moviepy.editor as mpy
from pydub import AudioSegment
#from pocketsphinx import AudioFile
import wave
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
url = "http://www.quotationspage.com/random.php"
request = urllib.request.Request(url)
html = urllib.request.urlopen(request)
soup = BeautifulSoup(html, 'lxml')
links = soup.findAll('a', {"title":"Click for further information about this quotation"})
quotes=[]
for a in links:
    quotes.append(str(a)[str(a).find('>')+1:str(a).rfind('<')])

quote = random.choice(quotes)
print(quote)
file = "quote.mp3"
wav_file = "quote.wav"
print(file, wav_file)


engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")

stream.Open(wav_file, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
engine.speak(quote)
stream.Close()

#tts = gTTS(text=quote, lang='en')
#tts.save(file)

#sound = AudioSegment.from_mp3(file)
#sound.export("quote.wav", format="wav")

print ("Playing: " + wav_file)
#wav_file = "quote.wav"

mixer.init()
mixer.music.load(os.getcwd()+'\\'+wav_file)
mixer.music.play()

while mixer.music.get_busy():
    time.sleep(0.1) #Decrease cpu effort

mixer.quit()
print ("Done Playing")

r = sr.Recognizer()
with sr.AudioFile(wav_file) as source:
    audio = r.record(source)

try:
    with open("spokenQuote Transcript.txt", "w+") as tf:
        tf.write(r.recognize_sphinx(audio)+ "\n")
    #t2 = time.time()
        #print("Transcript Complete for " + str(splice))
        #print("Time: %.2f seconds" % round(t2-t1,2))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

