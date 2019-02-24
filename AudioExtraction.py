import speech_recognition as sr
from pathlib import Path
import numpy as np
import os
import contextlib
with contextlib.redirect_stdout(None):
    import moviepy.editor as mpy
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
import time
from pocketsphinx import AudioFile
#import splitwav
import wave


TOTAL_TIME = 0


# function for linking text to video time
'''def linkToVid(audio):
    # frames per second
    with contextlib.closing(wave.open(audio,'r')) as f:
        fps = f.getframerate()
    # dictionary holds {word, start time in seconds}
    times = {}
    audioFile = str(audio)
    config = {'audio_file':audioFile}
    af = AudioFile(**config)
    for phrase in af:
        for word in phrase.seg():
            times.update({word.word: word.start_frame/fps}) #100 is default frame rate
    return times'''
def linkToVid(txt, aud):
    global TOTAL_TIME
    with contextlib.closing(wave.open(aud,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
    duration = frames / float(rate)
    # empty dict that will have {time,word}
    times = {}
    words = txt.split(' ')
    # use pydub library to get wav file length
    for i in range(len(words)):
      times[(duration/(len(words))*(i))+TOTAL_TIME]=words[i]
    TOTAL_TIME += duration
    return times

'''
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
movieFile = askopenfilename()
while not movieFile.endswith(('.webm', '.wav')):
    if movieFile == '':
        exit()
    print('Invalid file.')
    movieFile = askopenfilename() # show an "Open" dialog box and return the path to the selected file

baseName = movieFile[:movieFile.rfind('.')]
audioFile = baseName+' Audio.wav'
textFile = baseName+' Transcript.txt'
linkFile = baseName + ' Times.txt'

if (movieFile.endswith('.webm')):
    clip = mpy.VideoFileClip(movieFile)
    clip.audio.write_audiofile(audioFile) #Places audio in same location as py file
    clip.close()
    #Add Else?
'''
#INPUTS OF THE FOLLOWING FUNCTION
#input_file (string, required),
    #Input audio file
#output_dir (string, optional, default '.'),
    #Output directory for the split wav files
#silence_length (float (seconds), optional, default 3.0),
    #Minimum silence length to split
#silence_threshold (float btwn 0.0 and 1.0, optional, default 1e-6),
    #Energy level below which is to be considered 'silent'
#step_duration (float, seconds, optional, default = silence_length/10.0),
    #Seconds to jump forward after finding a silent spot
#dry_run (boolean, optional, default False)
    #Don't write any output files
t = time.time()
#print("Starting Audio Split")
#splitwav.splitThatWav(audioFile, baseName, 2, 0.0001)
#splices = Path(baseName).glob('./*')
t0 = time.time()
#print("Audio Split Complete")
#print("Time: %.2f seconds" % round(t0-t,2))
#for splice in splices: #iterator
r = sr.Recognizer()
with sr.AudioFile("C:\\Users\\Arthur Mayer\\OneDrive\\Documents\\HackCU_V\\spokenQuote.wav") as source:
    audio = r.record(source)  # read the entire audio file

    #print("Audio Extraction Complete for " + str(splice))
    #print("Time: %.2f seconds" % round(t1-t0,2))
# recognize speech using PocketSphinx (in speech_recognition)

'''try:
    with open(textFile, 'w') as tf:
        tf.write(r.recognize_sphinx(audio))
        tf.close()
        t2 = time.time()
        print("Transcript Complete")
        print("Time: %.2f seconds" % round(t2-t1,2))
        print("Starting Linking")
        times = linkToVid(textFile, audioFile)
        t3 = time.time()
        print("Linking Complete")
        print("Time: %.2f seconds" % round(t3-t2,2))
        timeSheet = open(linkFile, 'w')
        timeSheet.write(str(times))
        timeSheet.close()
        print("Total Time: %.2f seconds" % round(t3-t,2))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))'''

try:
    with open("C:\\Users\\Arthur Mayer\\OneDrive\\Documents\\HackCU_V\\spokenQuote Transcript.txt", "w+") as tf:
        tf.write(r.recognize_sphinx(audio)+ "\n")
    #t2 = time.time()
        #print("Transcript Complete for " + str(splice))
        #print("Time: %.2f seconds" % round(t2-t1,2))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
'''
print("Starting Linking")
splices = Path(baseName).glob('./*') #Have to reset since it is an iterator
for splice in splices:
    tf = open(textFile)
    ts = tf.read()
    tf.close()
    times = linkToVid(ts, str(splice))
    with open(linkFile, "a+") as f:
        f.write(str(times) + "\n")
    print("Linking Complete for " + str(splice))
#print("Time: %.2f seconds" % round(t3-t2,2))
#print(times)
t3 = time.time()
print("Total Time: %.2f seconds" % round(t3-t,2))

'''
