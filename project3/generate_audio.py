#pip install gTTs
from gtts import gTTS 
import os
import random
import tensorflow as tf

with open('symbols.txt', 'r') as file:
    symbols = file.read().replace('\n', '')
#symbols
#mkdir audio_captchas
for j in range(25000):
  s = ''
  for i in range(8):
    s = s + str(symbols[random.randint(0,len(symbols)-1)])
  mytext = s
  language = 'en'
  myobj = gTTS(text=mytext, lang=language, slow=False) 
  myobj.save("C:/Users/spanda/Desktop/Trinity/projects/scalable/project3/audio_captchas2/"+s+".mp3")
  if j % 300 == 0:
    print(str(j)+' done')
    
