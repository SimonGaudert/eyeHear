#In main .py file type "from textToSpeech import speech" then pass a string to the speech() function
#This solution will only work with linux machines

import os

def speech(text):
	os.system("say " + text) 

