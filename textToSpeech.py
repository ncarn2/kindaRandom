from gtts import gTTS

import os 
import platform
import sys

operatingSystem = sys.platform
print ("Operating System: " + operatingSystem)

words = 'Good morning I am a sad robittt oh whale'
tts = gTTS(text=words, lang='en')

tts.save("good.wav")
os.system("mpg123 good.wav")
