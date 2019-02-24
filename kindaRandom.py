#Displays the pygame window along with its special features
def displayImage():
    
    import os
    import pygame
    import urllib
    import urllib.request
    import time

    pygame.init()

    display_width = 1000
    display_height = 800

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('this statement is false')
    black = (0,0,0)
    white = (255,255,255)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    clock = pygame.time.Clock()
    crashed = False
    #want this to be a random image from that website
    def getFace():
        pygame.draw.rect(gameDisplay,(0,0,255),(100,500,200,50))
        textsurface = myfont.render('Wait...!', False, (255, 255, 255))
        gameDisplay.blit(textsurface,(120,500))
        pygame.display.update()
        f = open('face.png', 'wb')
        f.write(urllib.request.urlopen(urllib.request.Request('https://thispersondoesnotexist.com/image')).read())
        f.close()
        faceImage = pygame.image.load('face.png')

        x =  0#(display_width * 0.2)
        y = 0#(display_height * 0.2)
        image(x, y, faceImage)
        time.sleep(5)

    def image(x, y, imageFile):
        if type(imageFile)==str:
            img = pygame.image.load(imageFile)
            img = pygame.transform.scale(img,(500,200))
            gameDisplay.blit(img, (x,y))
        else:
            gameDisplay.blit(imageFile, (x, y))
        pygame.display.update()

    gameDisplay.fill(white)
    x = display_width/5
    y = display_height/5
    image(x,y, 'Welcome.jpg')
    pygame.display.update()
    time.sleep(2)
    image(x,y, 'Welcome2.jpg')
    pygame.display.update()
    time.sleep(0.5)
    image(x,y, 'Welcome3.jpg')
    pygame.display.update()
    time.sleep(1)
    def drawButtons():
        pygame.draw.rect(gameDisplay,(0,0,255),(100,500,200,50))
        textsurface = myfont.render('Make a face!', False, (255, 255, 255))
        gameDisplay.blit(textsurface,(120,500))
        pygame.draw.rect(gameDisplay,(0,255,0),(700,500,200,50))
        textsurface = myfont.render('Make a call!', False, (255, 255, 255))
        gameDisplay.blit(textsurface,(720,500))
        pygame.draw.rect(gameDisplay,(255,0,0),(400,600,200,50))
        textsurface = myfont.render('QUIT!', False, (255, 255, 255))
        gameDisplay.blit(textsurface,(420,600))
    drawButtons()

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] > 100 and pos[0] < 300 and pos[1] > 500 and pos[1] < 550:
                    getFace()
                    pygame.display.update()
                    image(x,y, 'Welcome3.jpg')
                    drawButtons()
                if pos[0] > 700 and pos[0] < 900 and pos[1] > 500 and pos[1] < 550:
                    textToSpeechBot()
                if pos[0] > 400 and pos[0] < 600 and pos[1] > 600 and pos[1] < 650:
                    exit()
        
        #image(x + 200,y + 300, faceImage)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def textToSpeechBot():
        
    #This program starts off by webscraping a random quotation #It then sends that program from text to speech 
    #It then will convert that speech back to text and speak to itself
    #Similar to the way humans play telephone
    #After doing this, it will call a list of people (only can call one person)
    #Twilio free trial limited us ot only calling one person :(
    #Always more random features to incorporate
    #table number 29

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

    #pause = input("Press any key to continue\n")


    file = "quote.mp3"
    wav_file = "quote.wav"
    #print(file, wav_file)


    import os 
    import platform
    import sys

    #Determine what operating system the user has in order to play audio properly
    operatingSystem = sys.platform
    #print ("Operating System: " + operatingSystem)
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

        stream.Open(wav_file, SpeechLib.SSFMCreateForWrite)       # ERRORS NEAR HERE
        engine.AudioOutputStream = stream                         # MAYBE HERE :(
        engine.speak(quote)
        stream.Close()

        import win32com.client as wincl
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(quote)

    #print ("Playing: " + wav_file)
    #This went to quickyl and slowed down the CPU
    while mixer.music.get_busy():
        time.sleep(0.1)

    mixer.quit()

    #print ("Done Playing")

    #Beginning of the twilio and Flask
    from flask import Flask
    from twilio.twiml.voice_response import VoiceResponse
    from twilio.rest import Client

    app = Flask(__name__)


    lastTelephone = quote 
    phoneNumberToCall = input("What is your phone number ?")
    query = ''.join(quote.split())
    phoneNumberToCall = phoneNumberToCall.replace(' ','').replace('-', '').replace('(', '').replace(')', '')
    print (phoneNumberToCall)
    account_sid = 'AC7119e83de9a686d0d56bc8491d80526a'
    auth_token = 'fcf3e5c1691051282836a49d26ff38c4'
    client = Client(account_sid, auth_token)

    call = client.calls.create (
            url = 'https://handler.twilio.com/twiml/EH06f621851a96b743015a43371effcf68?Message=' + query,  
            to='+1' + phoneNumberToCall,
            from_='+17207704132'
                    )

    print("Calling:",call.sid)

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





displayImage()
textToSpeechBot()


