from gtts import gTTS
import os
tts = gTTS(text='Good morning I am a sad robittt oh whale', lang='en')
tts.save("good.mp3")
os.system("mpg123 good.mp3")
