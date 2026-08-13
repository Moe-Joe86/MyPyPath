#viele Variablen sind Platzhalter und werden später verwendet
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
print(f"Das Wetter ist {weather}. Dunkle Wolken ziehen schnell vorbei. Von den Wolken gehen immer wieder Blitze und {noise} aus.")
print("Verwirrt fragst du dich, wo du bist und wie du hier gelandet bist.")
print("Du richtest dich auf und siehst vor dir ein kleines Dorf.")

villagename = input("Wie soll dein Dorf heißen? ") #den input hätte ich normalerweise anders gestaltet und direkt in den Dialog des NPCs gepackt. Aber aufgrund der F-String aufgabe so gestaltet

print("Als du dich dem Dorf näherst, fällt dir auf, dass es menschenleer ist. Du Rufst einmal ganz laut.")
print("HAAALLLLOOOO")
print()
print()
print()
noise = "Stille"
print(f"Aber niemand antwortet. Es herrscht {noise}.") 
print("In drei Häusern brennt noch Licht. Du beschließt zu einem dieser Häuser zu gehen.")
print("Haus 1 ist das größte und liegt im Zentrum des Dorfes. Haus zwei wirkt verwahrlost und wuchert von allen Seiten mit unterschiedlichsten Pflanzen und Kräutern zu. Aus Haus drei hörst du klirrende Geräusche und es steigt Rauch aus dem Schornstein")

house_choice = input(f"Du gehst zu Haus Nr und klopfst")
print(type(house_choice))

print ("Von drinnen kommt eine Antwort: Ja? Wer da?")

player_name = input("Ich heiße ")

print(type(player_name))
print(f"Fremder: Hallo {player_name}. Ich bin der {profession} von {villagename}. Was suchst du hier?")