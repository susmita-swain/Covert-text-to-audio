from gtts import gTTS #Google Text To Speech

import os

mytext="Welcome to SushiCode what typeof help you need please say kindly in here"

language='en'
    
myobj=gTTS(text=mytext,lang=language,slow=False)

myobj.save("welcome.mp3")

os.system("welcome.mp3") 




# male voice

import pyttsx3

import os

engine = pyttsx3.init()

# Set the voice ID to a male voice

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

mytext = "Welcome to SushiCode. What type of help do you need? Please kindly say it here."

engine.save_to_file(mytext, 'welcome.mp3')

engine.runAndWait()

# Play the generated audio file using the default system player

os.system("welcome.mp3")

