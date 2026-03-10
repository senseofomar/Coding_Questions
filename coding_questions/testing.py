#Install an external module and use it to perform an operation of your interest
import pyttsx3
#This module is used to speak aloud what the program says
sound = pyttsx3.init()
sound.say("Hi Omar, How its going?")
sound.runAndWait()