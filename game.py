import time
import random

player_class = None
player_name = None

#equipment
rapid_deployer = None        #für engineer kurz RD-4
cellforge_3000 = None             #NanoFix, Med-Ray 500, SyntheCell 8
heavy_machinegun = None
machinegun = None


#stats
health = 100
damage = 10
armor = 5
exp = 99
kern_integritaet = 100

#resouces
ammo_max = 40
core_max = 100
magazin = 30   #Menge an Munition pro Magazin
geladen = 5
magazin_groesse = 5

inventory = []
max_inventory = 10
recruts = 0
medkit = None
reparaturkit = None

balken_laenge = 10


wave_to_evacuation = 20
enemy = []
reload_necessary = False
enemy_in_sight = None
radiomessage_transmitted = None
answere = None

#------------------------------------------------------------------------------------------------------
#DAS DEPOT / VORRAT

waren = {"medkit": 25, "magazin": 15, "panzerplatte": 90}   #Preisangabe, keine Menge!
verkaufswerte = {"chitinpanzer": 3, "organ": 5, "saeuredruese": 8}

stapelbar = {"medkit": False, "magazin": True, "panzerplatte": False, "munition": True, "chitinpanzer": True, "organ": True, "saeuredruese": True}   #Wird nur für Waren und Depot benötigt. 

vorrat = {"vaporium": 100, "munition": 40, "chitinpanzer": 2, "organ": 1, "saeuredruese": 0} #Mengenangabe!!!

anzeigenamen = {"medkit": "MedKit", "munition": "Munition", "panzerplatte": "Panzerplatte", "organ": "Organ",
    "vaporium": "Vaporium", "chitinpanzer": "Chitinpanzer", "saeuredruese": "Säuredrüse", "magazin": "Magazin(30 Schuss)"}

stufenaufstieg = {"stufe1": 100, "stufe2": 300, "stufe3": 900, "stufe4": 3000, "stufe5": 10000}
stufe = 0
        



#----------------------------------------------------------------------------------------------------
#DIE MAP
karte = """
               +---------------+

               |    Nordtor    |
               |               |
               +-------+-------+
                       |
                       |
+---------------+------+-------+---------------+------------------+

|     Depot     |     Kern     |    Osttor     | Landeplattform   |
|                                              |(nicht angebunden)|
+---------------+------+-------+---------------+------------------+
                       |
                       |
               +-------+-------+

               |   Werkstatt   |
               |               |
               +---------------+
"""

sectors = {
    "nordtor":{
        "beschreibung": "Du stehst am nördlichen Tor.", "integritaet": 100, "nachbarn": {
            "sueden": "kern"}},
    "osttor":{
        "beschreibung": "Du stehst am östlichen Tor. Der Weg ist verschüttet. Dahinter liegt die Landeplattform.", "integritaet": 100, "nachbarn": {
            "westen": "kern"}},
    "kern":{
        "beschreibung": "Die zentrale Bunkeranlage des Außenpostens.", "integritaet": 100, "nachbarn": {
            "sueden": "werkstatt", "norden": "nordtor", "osten": "osttor", "westen": "depot"}},
    "depot":{
        "beschreibung": "Hier kann man Gegenstände kaufen.", "integritaet": 100, "nachbarn": {
            "osten": "kern"}},
    "werkstatt":{
        "beschreibung": "In der Werkstatt lassen sich Gegenstände und Gebäude bauen.", "integritaet": 100, "nachbarn": {
            "norden": "kern"}}, 
 #   "landeplattform":{
 #           "beschreibung": "Hier landet das Shuttle für die Evakuierung,", "integritaet": 100, "nachbarn": {
 #               "norden": "werkstatt"}},

}

aktueller_sektor = sectors["nordtor"]


#---------------------------------------------------------------------------------------------------------------------------

ascii_kopf = """
                                VORPOSTEN              
  /------------------------------------------------------------------\ 
 / *  *  *  *  *  *  *  *  *  *  * --- *  *  *  *  *  *  *  *  *  *  *\ 
/                                 |   |                                \ 
"""


last_message = "Kzzz... Brauchen dringend Verstärkung! kschhh... Wir werden überrannt! Kzzz... Beeilt euch! ...chhh"
lights = "Notbeleuchtung" # kürzere Sichtweite?


print(f"Health: {health} | Ammo: {vorrat['munition']} | Vaporium: {vorrat['vaporium']} | Rekruten: {recruts} | Wellen bis zur Evakuierung: {wave_to_evacuation} ")

"""
print(f"Aufgezeichnete Durchsage: {last_message}")
print()
time.sleep(2)
print("ALLE REKRUTEN STILLGESTANDEN!")
player_name = input("WIE HEIßEN SIE SOLDAT? ")
print(f"Rekrut {player_name}, es ist ihre Aufgabe die Verteidiger zu unterstützen und die Stellung zu halten! ")
"""
print()
time.sleep(1)
print()

print("Rekrut, welches spezialisierte Training haben Sie durchlaufen?")
print()
print("-Soldier")
print("-Medic")
print("-Heavy")
print("-Engineer")
print()
player_class = input("Wähle eine Klasse und gebe den Namen ein:  ")
player_class = player_class.lower().strip()

if player_class != "soldier" and player_class != "medic" and player_class != "heavy" and player_class != "engineer": # hiermit möchte ich Auftrag 3 ohne else erfüllen. Diese Bedingung kann ich auch mit == und einem else erfüllen, ist aber kostspieliger. bewusste entscheidung gegen die Aufgabe!
    player_class = input("Falsche Eingabe. Gib Soldier, Medic, Heavy oder Engineer ein: ")
    player_class = player_class.lower().strip()

if player_class == "soldier":
    health = 100
    damage = 10
    armor = 5

    machinegun = True
elif player_class == "medic":
    health = int(health * 0.8)
    damage = int(damage * 0.6)
    armor = int(armor * 0.6)
    cellforge_3000 = True
elif player_class == "heavy":
    health = int(health * 1.4)
    damage = int(damage * 1.4)
    armor = int(armor * 2)
    heavy_machinegun = True
elif player_class == "engineer":
    health = int(health * 0.9)
    damage = int(damage * 0.7)
    armor = int(armor * 0.8)
    rapid_deployer = True

health_max = health

print()
print(f"Klasse: {player_class}")
print(f"Health: {health}")
print(f"Damage: {damage}")
print(f"Armor: {armor}")

print()
time.sleep(1)
print()

print(f"Wir haben nur noch {vorrat['munition']} Munition übrig.")
print(f"Die Kernintegrität unserer Einrichtung beträgt zwar noch {kern_integritaet}%,")
print(f"aber uns verbleiben nur noch {vorrat['vaporium']} Vaporium.")

print()
time.sleep(1)

print(f"Aufgezeichnete Durchsage: {last_message}")

print()
time.sleep(1)
print()

"""
print("Feinde nähern sich. Du siehst etwas ungewöhnliches. Setzt du einen Funkspruch ab?")
answere = input("Ja oder Nein > ")
answere = answere.lower().strip()

repeat = True
while repeat:
    if answere == "ja":
        radiomessage_transmitted = True
        print("Ein Funkspruch wurde abgesetzt.")
        repeat = False
    elif answere == "nein":
        radiomessage_transmitted = False
        print("Du hast keinen Funkspruch abgesetzt.")
        repeat = False
    else:
        answere = input("Falsche Eingabe. Schreibe Ja oder Nein: ")

"""

enemy_in_sight = True
print()

print(ascii_kopf)

inventory = []
loot_table = ["chitinpanzer", "organ", "saeuredruese", "datenkern"]
loot = []

#--------------------------------------------------------------------------------------------------------------------
#WELLEN UND RUNDEN INITIALISIEREN
#GEGNER SPAWNEN

for wave in range(1, wave_to_evacuation + 1):
    print(f"--- Welle {wave} von {wave_to_evacuation} ---")

    
    round_nr = 1
    enemy = []

    for spawn in range(wave):
        enemy.append(5)

    print()    
    print(f"{len(enemy)} Gegner befinden sich im Anmarsch.")
    

    while len(enemy) > 0 and (kern_integritaet > 0 and health > 0):
        
        stufe = 0

        for up in stufenaufstieg:
            if exp > stufenaufstieg[up]:   
                stufe += 1
        
        print()
        print(f"Welle {wave} | Runde {round_nr}")

#------------------------------------------------------------------------------------------------------------------------
# DIE ANMARSCHBAHN

        pos_on_map = ["."] * 5
        closest_enemy = min(enemy)
        
        for enemy_pos in range(len(enemy)):
            if enemy[enemy_pos] > 0:
                pos_on_map[-enemy[enemy_pos]] = "k"
        print("Das Loch @ " + "".join(pos_on_map) + " /-\ Vorposten")


#------------------------------------------------------------------------------------------------------------------------
#AUSFÜHRBARE AKTIONEN       
 
        print("Wähle eine der Aktionen:\n--beenden --feuer --status --nachladen --inventar --umsehen --gehe --waren --kaufe --map")
        action = input("--").lower().split()   #test,schaden sind entwicklerwerkzeuge
        print()

        if len(action) == 0:
            print("Gib etwas ein")
        else:
            word1 = action[0]
            word2 = ""
            if len(action) > 1:
                word2 = action[1]
            if word1 == "feuer" or (word1 == "feuer" and word2 == "frei"):
                if reload_necessary:
                    print("Magazin leer.")
                else:
                    print("Feuer frei!")
                    geladen -= 1
                
                    enemy.remove(closest_enemy)
                    exp += 10
                    round_nr += 1
                    kern_integritaet -= len(enemy) * 2 
                    health -= len(enemy) * 1
                    loot.append(random.choice(loot_table))
                    if geladen == 0:
                        print("Das Magazin ist jetzt leer!")
                        reload_necessary = True                        
                    for move in range(len(enemy)):
                        enemy[move] -= 1

            elif word1 == "nachladen" or (word1 == "lade" and word2 == "nach") :
                round_nr += 1
                reloaded = False
                while vorrat["munition"] > 0 and geladen < magazin_groesse:
                    vorrat["munition"] -= 1
                    geladen += 1
                    reloaded = True
                    reload_necessary = False
                if vorrat["munition"] == 0:
                    print("Munitionsmangel.")
                elif reloaded == True:
                    print("Nachgeladen.")


                kern_integritaet -= len(enemy) * 2
                reload_necessary = False                  
                for move in range(len(enemy)):
                    enemy[move] -= 1

            elif word1 == "beenden" or (word1 == "welle" and word2 == "beenden"):
                print(f"Welle {wave} beendet")
                break

            elif word1 == "inventar" or (word1 == "inventar" and word2 == "anzeigen"):
                print("Gegenstände und Vorrat:")
                for gegenstand in inventory:
                    print(f"- {anzeigenamen.get(gegenstand, gegenstand)}")
                for gegenstand in vorrat:
                    print(f"- {vorrat[gegenstand]} {anzeigenamen.get(gegenstand, gegenstand)}")

            elif word1 == "nimm":
                if len(action) == 1:
                    print("Nichts ausgewählt.")
                else:
                    if word2 in loot:
                        if stapelbar[word2] == False:
                            if len(inventory) >= max_inventory:
                                print("Inventar ist voll.")
                            else:
                                inventory.append(word2)
                                loot.remove(word2)
                                print(f"{anzeigenamen.get(word2, word2)} aufgenommen.")
                        else:
                            vorrat[word2] += 1
                            loot.remove(word2)
                            print(f"{anzeigenamen.get(word2, word2)} aufgenommen.")
                    else:
                        print("Das liegt hier nicht.")
            
            elif word1 == "lege":
                if len(action) == 1:
                    print("Nichts ausgewählt.")
                else:
                    if len(action) == 2 and word2 in inventory:
                        inventory.remove(word2)
                        loot.append(word2)
                        print(f"{anzeigenamen.get(word2, word2)} abgelegt.")
                    else:
                        print("Das besitze ich nicht.")

            elif word1 == "umsehen":
                print(aktueller_sektor["beschreibung"])     #alles in einem Print?              
                print(f"Nachbarsektoren: {aktueller_sektor['nachbarn']}")
                if "integritaet" in aktueller_sektor:
                    print(f"Integritaet: {aktueller_sektor['integritaet']}")  
                else:
                    print(f"Integritaet: {kern_integritaet}")      

            elif word1 == "gehe":
                if len(action) == 1:
                    print("Keine Richtung ausgewählt. Nutze --umsehen, um Richtungen zu sehen.")
                else:
                    if len(action) == 2 and word2 in sectors:
                        print(f"Ich gehe zum Sektor {word2}.")
                        aktueller_sektor = sectors[word2] #vergeht eine Runde?
                    else:
                        print("Diesen Sektor gibt es nicht.")
            
            elif word1 == "waren":
                if aktueller_sektor != sectors["depot"]:
                    print("Gehe zum Depot. Hier gibt es keine Waren.")
                else:
                    for ware in waren:
                        print(f"{anzeigenamen.get(ware, ware)}: {waren[ware]} Vaporium")
                              #aufgabe 6 muss überarbeitet werden? Alle waren ohne Schleife angezeigt. Ware wird jetzt schon ohne Mehrarbeit ausgegeben?!?!?!?
            
            elif word1 == "kaufe":
                if aktueller_sektor != sectors["depot"]:
                    print("Gehe zum Depot. Hier kann man nichts kaufen.")
                elif len(action) == 1:
                    print("Keine Ware ausgewählt. Gebe --waren ein, um die Waren zu sehen.")                    
                elif word2 not in waren:
                    print("Diese Ware ist nicht verfügbar.")
                elif vorrat["vaporium"] < waren[word2]:
                    print("Du besitzt nicht genügend Vaporium.")
                elif stapelbar[word2] == False and len(inventory) >= max_inventory:
                    print("Dein Inventar ist voll.")
                else:
                    if len(action) == 2:                       
                        if stapelbar[word2] == False:
                            inventory.append(word2)
                            vorrat["vaporium"] -= waren[word2]
                            print(f"{anzeigenamen.get(word2, word2)} erfolgreich gekauft.")   
                        else:
                            anzahl = int(input(f"Wieviele möchtest du kaufen? "))
                            if anzahl < 0:
                                anzahl *= -1
                            if vorrat["vaporium"] < (waren[word2] * anzahl):
                                print("Du besitzt nicht genügend Vaporium.")
                            else:
                                vorrat["munition"] += (magazin * anzahl)
                                vorrat["vaporium"] -= (waren[word2] * anzahl)
                                print(f"{anzahl} {anzeigenamen.get(word2, word2)} erfolgreich gekauft.")                
            
            elif len(action) == 1 and word1 == "verkaufe":
                if aktueller_sektor != sectors["depot"]:
                    print("Gehe zum Depot. Hier kann man nichts verkaufen.")
                else:  
                    bezahlung = 0             
                    for verkauft in verkaufswerte:
                        print(f"{vorrat[verkauft]} {anzeigenamen.get(verkauft, verkauft)} für {(vorrat[verkauft] * verkaufswerte[verkauft])} Vaporium verkauft.")
                        bezahlung += (vorrat[verkauft] * verkaufswerte[verkauft])
                        vorrat[verkauft] = 0                        
                    vorrat["vaporium"] += bezahlung    
                    print()
                    print(f"Du hast insgesamt {bezahlung} Vaporium erhalten.")
                    print(f"Du besitzt jetzt {vorrat['vaporium']} Vaporium.")        

            elif word1 == "map":
                print(karte)

            elif word1 == "status" or (word1 == "status" and  word2 == "anzeigen"):
                """
                kern_balken = round((kern_integritaet / core_max) * balken_laenge)      #Meine Balkenanzeigen rechnen alle Werte auf die Balkenlänge 10 um und übschreiten keine Grenzen.
                ammo_balken = round((vorrat['munition']  / ammo_max) * balken_laenge)
                health_balken = round((health / health_max) * balken_laenge)
                kern_rest = balken_laenge - kern_balken
                ammo_rest = balken_laenge - ammo_balken
                health_rest = balken_laenge - health_balken
                """
                print(f"Kern: {kern_integritaet}")
                print(f"Health: {health}")
                print(f"Armor: {armor}")
                print(f"Vaporium: {vorrat['vaporium']}")
                print(f"Ammo: {vorrat['munition']}")
                print(f"Schaden: {damage}")
                print(f"Rekruten: {recruts}")
                print(f"Gegner: {enemy}")
                print(f"Erfahrung: {exp}")
                print(f"Stufe: {stufe}")
                print(f"Nachladen nötig: {reload_necessary}")
                print(f"Loot:{loot}")
                
                """
                print("Kern      [" + ("#" * kern_balken) + ("·" * kern_rest) + "]")
                print("Health    [" + ("#" * health_balken) + ("·" * health_rest) + "]")
                print("Munition  [" + ("#" * ammo_balken) + ("·" * ammo_rest) + "]")"""


    if kern_integritaet <= 0:        
        break
        print("Deine Basis wurde zerstört.")
    elif health <= 0:
        break
        print("Du bist gestorben.")
        

