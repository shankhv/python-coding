from gtts import gTTS
import os

mytext = input("Enter the text which needs to be converted to speech:\n")
speech = gTTS(text=mytext, lang="en", slow=False) 
speech.save("welcome.mp3")

os.system("start welcome.mp3")