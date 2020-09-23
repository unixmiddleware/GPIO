import os
from gtts import gTTS

text='Get Ready Player 1. The play will be rough. Are you ready to Rumble!'
engine=gTTS(text)
engine.save('gtts.mp3')
os.system('mpg123 gtts.mp3')
