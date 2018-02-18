from gtts import gTTS
import pygame
def readText(outputText):
	tts = gTTS(text=outputText, lang='en')
	tts.save("./audioOutput.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load("audioOutput.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
    	continue
