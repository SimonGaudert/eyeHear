from gtts import gTTS
import pygame

def readText(outputText,language):
	tts = gTTS(text=outputText, lang=language)
	tts.save("./audioOutput.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load("audioOutput.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
    	continue
