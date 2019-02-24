import gTTS
import ffmpeg #pip install ffmpeg-python

quote = 'mp3 to wav'

file = 'quote.mp3'  

tts = gTTS(text=quote, lang='en')
tts.save(file)

sound = AudioSegment.from_mp3(file)
sound.export("quote", format="wav")

wavFile = ffmpeg.input('file').filter().output('file.wav').run()
