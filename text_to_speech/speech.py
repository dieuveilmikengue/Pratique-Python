import pyttsx3 #Biblioteque python qui permet d'ecouter le texte

machine = pyttsx3.init() #On initialise la machine dans la variable machine

machine.say("Bonjour les gens") #Le texte que la machine va lire
machine.say("T'aurais pas due faire cela")

machine.runAndWait() #On demarre la machine