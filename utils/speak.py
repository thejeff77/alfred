import pyttsx3
from gtts import gTTS
import os

class Speak:

    #def __init__(self):
        # self.engine = pyttsx3.init()

    # def speak(self, text):
    #
    #     self.engine.say('Good morning.')
    #     self.engine.runAndWait()

    def speak(self, text):

        tts = gTTS(text=text, lang='en')
        tts.save("latestResponse.mp3")
        os.system("mpg321 latestResponse.mp3")