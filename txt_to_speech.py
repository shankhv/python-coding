from gtts import gTTS 
import os

mytext = input("enter the text which needed to be converted as speech\n")
speech = gTTS(text=mytext, lang="en", slow=False) 
speech.save("output.mp3")
os.system("start output.mp3") 