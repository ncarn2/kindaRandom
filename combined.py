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


#ffmpeg debugger
#import logging

call = False

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


import os 
import platform
import sys

operatingSystem = sys.platform
print ("Operating System: " + operatingSystem)


if (operatingSystem == 'linux'):
    from gtts import gTTS
    tts = gTTS(text=quote, lang='en')

    tts.save("good.wav")
#    os.system("mpg123 good.wav")

    tts.save(file)

    sound = AudioSegment.from_mp3(file)
    sound.export("quote.wav", format="wav")

    file = "./" + file
    sound = AudioSegment.from_mp3(file)
    sound.export("quote.wav", format="wav")

    print ("Playing: " + wav_file)
    mixer.init()
    mixer.music.load(wav_file)
    mixer.music.play()

    mixer.quit()
    print ("Done Playing")
if (operatingSystem == 'win32'):
    from comtypes.client import CreateObject
    
    engine = CreateObject("SAPI.SpVoice")
    stream = CreateObject("SAPI.SpFileStream")

    from comtypes.gen import SpeechLib

    stream.Open(wav_file, SpeechLib.SSFMCreateForWrite)
    engine.AudioOutputStream = stream
    engine.speak(quote)
    stream.Close()

    print ("Playing: " + wav_file)
    mixer.init()
    mixer.music.load(os.getcwd()+'\\'+wav_file)
    mixer.music.play()

    mixer.quit()
    print ("Done Playing")
#wav_file = "quote.wav"
while mixer.music.get_busy():
    time.sleep(0.1) #Decrease cpu effort


#r = sr.Recognizer()
#with sr.AudioFile(wav_file) as source:
#    audio = r.record(source)
#
#try:
#    with open("spokenQuote Transcript.txt", "w+") as tf:
#        tf.write(r.recognize_sphinx(audio)+ "\n")
#    #t2 = time.time()
#        #print("Transcript Complete for " + str(splice))
#        #print("Time: %.2f seconds" % round(t2-t1,2))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))
#
#

if call:
    from flask import Flask
    from twilio.twiml.voice_response import VoiceResponse
    from twilio.rest import Client

    app = Flask(__name__)


    lastTelephone = "who touch ugh my spaghet"

    query = ''.join(quote.split())

    account_sid = 'AC7119e83de9a686d0d56bc8491d80526a'
    auth_token = 'fcf3e5c1691051282836a49d26ff38c4'
    client = Client(account_sid, auth_token)

    call = client.calls.create (
            url = 'https://handler.twilio.com/twiml/EH06f621851a96b743015a43371effcf68?Message=' + query,  
            to='+17203181646',
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
