'''from comtypes.client import CreateObject
engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
infile = "randomQuote.txt"
outfile = "test_quote.wav"
from comtypes.gen import SpeechLib
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
f = open(infile, 'r')
theText = f.read()
f.close()
engine.speak(theText)
stream.Close()
'''
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("This is the pc voice speaking")
