#This program starts off by webscraping a random quotation
#It then sends that program from text to speech 
#It then will convert that speech back to text and speak to itself
#Similar to the way humans play telephone
#After doing this, it will call a list of people (only can call one person)
#Twilio free trial limited us ot only calling one person :(
#Always more random features to incorporate

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
from gtts import gTTS

pygame.init()

#ffmpeg debugger
#import logging

#Grab the quote from the web
url = "http://www.quotationspage.com/random.php"
request = urllib.request.Request(url)
html = urllib.request.urlopen(request)
soup = BeautifulSoup(html, 'lxml')
links = soup.findAll('a', {"title":"Click for further information about this quotation"})
quotes=[]
for a in links:
    quotes.append(str(a)[str(a).find('>')+1:str(a).rfind('<')])

quote = random.choice(quotes)
print("Random Web Quote: " + quote)
pause = input("Press any key to continue\n")

file = "quote.mp3"
wav_file = "quote.wav"
print(file, wav_file)


import os 
import platform
import sys

#Determine what operating system the user has in order to play audio properly
operatingSystem = sys.platform
print ("Operating System: " + operatingSystem)
#Have to create the files and initialize mixers for both OS's

from gtts import gTTS
tts = gTTS(text=quote, lang='en')
tts.save(file)

mixer.init(frequency=22050, size=-16, channels=2, buffer=-4096)

#linux play and convert wav file
if (operatingSystem == 'linux'):

    #sound = AudioSegment.from_mp3(file)
    #sound.export(wav_file, format="wav")

    file = "./" + file
    sound = AudioSegment.from_mp3(file)
    sound.export(wav_file, format="wav")

    #mixer.init()
    mixer.music.load(wav_file)
    mixer.music.play()

#windows system play and convert wav file
if (operatingSystem == 'win32'):
    from comtypes.client import CreateObject
    
    engine = CreateObject("SAPI.SpVoice")
    stream = CreateObject("SAPI.SpFileStream")

    from comtypes.gen import SpeechLib

    #stream.Open(wav_file, SpeechLib.SSFMCreateForWrite)        ERRORS NEAR HERE
    #engine.AudioOutputStream = stream                          MAYBE HERE :(
    #engine.speak(quote)
    #stream.Close()

    mixer.music.load(wav_file)
    mixer.music.play()

print ("Playing: " + wav_file)
#This went to quickyl and slowed down the CPU
while mixer.music.get_busy():
    time.sleep(0.1)

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



#Beginning of the twilio and Flask
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)


lastTelephone = quote 

query = ''.join(quote.split())

account_sid = 'AC7119e83de9a686d0d56bc8491d80526a'
auth_token = 'fcf3e5c1691051282836a49d26ff38c4'
client = Client(account_sid, auth_token)

call = client.calls.create (
        url = 'https://handler.twilio.com/twiml/EH06f621851a96b743015a43371effcf68?Message=' + query,  
#Commented out so we dont spam each other        to='+17203181646',
        from_='+17207704132'
                )

print(call.sid)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say(query)

    return str(resp)


#if __name__ == "__main__":
#    app.run(debug=True)
