#viele Variablen sind Platzhalter und werden später verwendet
import time

timeofday = None
weather = "unheimlich"
smell = None
sounds = None
villagename = None
profession = "Händler" # dient als Platzhalter und wird später eine liste/dict????? so weit bin ich noch nicht
house_choice = None
player_name = None
noise = "Donner"
saw_something = None
weiter = True
trust = 1.0     #wird spätervertrauenssystem

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
print()
print()
print("In zwei Häusern im Dorf brennt noch Licht. Du beschließt zu einem der Häuser zu gehen.")
print()
print(f"Haus 1 ist die Villa des reichen {profession} und liegt im Zentrum des Dorfes {villagename}.")
print()
print(f"Das zweite ist das Haus der {profession} und wuchert von allen Seiten")
print("mit unterschiedlichsten Pflanzen und seltsamen Kräutern zu.")
print()
print("Du wolltest gerade in Richtung eines der beiden  Häuser gehen,")
print("da bemerkst du einen Fremden auf der anderen Straßenseite.")
print()
house_choice = input("Wo gehst du hin? Tippe Villa, Hexenhaus oder Fremder ein: ")
print()
print()
Antwort = house_choice.lower().strip()

while weiter:
    if house_choice == "villa":
        print(f"Du entscheidest dich zum reichen Geschäftsmann zu gehen und klopfst an der Türe.")
        weiter = False
    elif house_choice == "hexenhaus":
        print("Eine Gestalt verlässt das zugewucherte Haus, als du dich näherst,")
        print(f"und kommt auf dich zu. Es ist die {profession}.")
        weiter = False
    elif house_choice == "fremder":
        print("Der Fremde rennt weg, als er dich siehtn")
        print("Du schaffst es ihn einzuholen und stellst ihn zur Rede.")
        weiter = False
    else:
        print("Ungültige Eingabe. Tippe Villa, Hexenhaus oder Fremder ein.")

weiter = True         # damit ich die variable wieder verwenden kann

print(f"Der/die {profession} steht vor dir und schaut dich misstrauisch an.")
print(f"Hallo {player_name}. Du bist ja auch noch da. Weist du warum alle verschwunden sind? Hast du etwas gesehen?")     # der dialog passt nicht zu verschiedenen personen. ich kann es noch nicht besser und mehr print text geht an der übung vorbei. muss später verbessert werden.
print()
print("Antwort 1: Ja ich habe etwas gesehen [Lügen]")
print("Antwort 2: Nein, ich habe nichts gesehen.")
print()

saw_something = input("Wähle eine Antwort: Ja/Nein")
antwort = saw_something.lower().strip()

if antwort == "ja": 
    print("Was hast du gesehen?") # später steigt die variable "trust" der jeweiligen Person. Listen/dics noch nicht gelernt
    trust = trust + 0.2 # entpuppt sich später als schlechte Entscheidung. Damit wird Schritt 6 erfüllt.
elif antwort == "nein":
    print("Mist, was sollen wir jetzt machen?")
else:
    print(f"Der/Die {profession} weicht ängstlich vor deiner dämonischen Aussprache zurück.")
    trust = trust - 0.2

print()

if trust >= 1.0 and weather == unheimlich:
    print("Komm erstmal rein. Wir reden drinnen weiter.")