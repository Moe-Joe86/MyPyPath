#viele Variablen sind Platzhalter und werden später verwendet
import time

timeofday = None
weather = "unheimlich"
smell = None
sounds = None
villagename = None
profession = "Schmied" # dient als Platzhalter und wird später eine liste/dict????? so weit bin ich noch nicht
house_choice = None
player_name = None
noise = "Donner"
saw_something = None


print("Willkommen im Spiel!")
player_name = input("Wie ist dein Name?")
print(f"{player_name} öffnet langsam deine Augen und schaut gegen den Himmel. ")
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
print(f"Haus 1 ist das größte und liegt im Zentrum des Dorfes {villagename}. Das zweite ist ein verwahrlostes Haus und wuchert von allen Seiten mit unterschiedlichsten Pflanzen und seltsamen Kräutern zu.  Aus dem dritten Haus hörst das Klirren des von Metall im inneren.")

house_choice = input(f"Aus einem der Häuser kommt jemand. (Wähle eine Hausnummer): ")

if house_choice == 1:
    print(f"Eine Gestalt verlässt das große Haus und kommt auf dich zu. Du erkennst, dass es der {profession} ist.")
elif house_choice == 2:
    print(f"Eine Gestalt verlässt das zugewucherte Haus und kommt auf dich zu. Du erkennst, dass es der {profession} ist.")
else:
    print(f"Eine Gestalt verlässt das große Haus und kommt auf dich zu. Du erkennst, dass es der {profession} ist.")

print(f"Der/die {profession} bleibt vor dir stehen und schaut dich misstrauisch an.")
print(f"Hallo {player_name}, du bist also auch noch da? Hast du mitbekommen, was mit den anderen Dorfbewohnern passiert ist? ")

print("Antwort 1: Ja ich habe etwas gesehen [Lügen]")
print("Antwort 2: Nein, ich habe nichts gesehen.")

saw_something = input("Wähle eine Antwort: ")
antwort = saw_something.lower().strip()

if antwort == "ja":
    print("Was hast du gesehen?") # später steigt die variable "trust" der jeweiligen Person. Listen/dics noch nicht gelernt
    trust = trust + 1
elif antwort == "nein":
    print("text ausdenken")
