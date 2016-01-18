#!/usr/bin/env python
import speech_recognition as sr
import sys

if __name__ == '__main__':
  
  wavFname = sys.argv[1]
  txt_f = sys.argv[2]
  txt = ''
  list_ = []

  r = sr.Recognizer('en-GB')
  with sr.WavFile(wavFname) as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

  # try:
  list_ = r.recognize(audio, True)
  for prediction in list:
      print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
  # except LookupError:                               # speech is unintelligible
  #   print("Could not understand audio")


  with open(txt_f, 'w') as f:
    f.write(txt)


