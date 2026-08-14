#viele Variablen sind Platzhalter und werden später verwendet
import time

timeofday = None
weather = "unheimlich"
smell = None
sounds = None
villagename = None
profession = "Schmied"
house_choice = None
player_name = None
noise = "Donner"


print("Willkommen im Spiel!")
print("Du öffnest langsam deine Augen und schaust aud den Himmel. ")
smell = "Sommerregen"
print(f"Das Wetter ist {weather}. Dunkle Wolken ziehen schnell vorbei. Von den Wolken gehen immer wieder Blitze und {noise} aus. Es riecht nach frischem {smell}.")
print("Verwirrt fragst du dich, wo du bist und wie du hier gelandet bist.")
print("Du richtest dich auf und siehst, dass du mitten auf dem Marktplatz deines Dorfes aufgewacht bist. Du kannst niemanden sehen")

villagename = input("Wie soll dein Dorf heißen? ") #den input hätte ich normalerweise anders gestaltet und direkt in den Dialog des NPCs gepackt. Aber aufgrund der F-String aufgabe so gestaltet
print("Du rufst ganz laut.")
print("HAAALLLLOOOO?")
print()
time.sleep(1)
print()
time.sleep(1)
print()
noise = "Stille"
print(f"Niemand antwortet. Es herrscht {noise}.") 
print("In drei Häusern im Dorf brennt noch Licht. Du beschließt zu einem der Häuser zu gehen.")
print(f"Haus 1 ist das größte und liegt im Zentrum des Dorfes, es ist das Haus des {profession} von {villagename}. Das zweite ist das verwahrloste Haus der {profession} und wuchert von allen Seiten mit unterschiedlichsten Pflanzen und seltsamen Kräutern zu.  Das dritte Haus ist das des {profession}. Du hörst das Klirren des Amboss im inneren.")

house_choice = input("Du gehst zu Haus Nr und klopfst. (Wähle eine Hausnummer): ")

print ("Von drinnen kommt eine Antwort: Ja? Wer da?")

player_name = input("Ich bin es, ")
print(f"Ach {player_name}, du bist es. Komm schnell rein.")