from gtts import gTTS
import os

mytext = input("Enter the text which needs to be converted to speech:\n")
if len(mytext)==0:
    mytext="PLEASE ENTER THE TEXT WITHOUT ANY WORD CAN NOT CONVERT TO SPEECH"
speech = gTTS(text=mytext, lang="en", slow=False) 
speech.save("output.mp3")

os.system("start output.mp3")