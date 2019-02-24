import os 
import platform
import sys

operatingSystem = sys.platform
print ("Operating System: " + operatingSystem)

words = 'Good morning I am a sad robittt oh whale'

if (operatingSystem == 'linux'):
    from gtts import gTTS
    tts = gTTS(text=words, lang='en')

    tts.save("good.wav")
    os.system("mpg123 good.wav")
if (operatingSystem == 'win32'):
    import pyttsx
    engine = pyttsx.init()
    engine.say(words)
    engine.runAndWait()
