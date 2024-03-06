import pyttsx3

def text_to_speech_and_play(t):
    a = pyttsx3.init()
    a.say(t)
    a.runAndWait()    
