#wondersOfPython - 1
#cs50 2019 - lecture 6 - pyhton 
#https://www.youtube.com/watch?v=fL308_-Kbt0
#01:38:37

import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

print("Google Speech Recognition thinks you said: ")
print(recognizer.recognize_google(audio))   