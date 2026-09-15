import time
import random

player_name = None
player_class = None
KLASSEN = ("soldat", "heavy", "engineer", "medic")


#equipment
rapid_deployer = None        #für engineer kurz RD-4
cellforge_3000 = None             #NanoFix, Med-Ray 500, SyntheCell 8
heavy_machinegun = None
machinegun = None


#stats
health = 100
damage = 10
armor = 5
exp = 0
kern_integritaet = 100

#resouces
ammo_max = 40
core_max = 100
geladen = 5
magazin_groesse = 5
munitionskiste = 30

inventory = []
max_inventory = 10
recruts = 0

balken_laenge = 10


wave_to_evacuation = 20
enemy = []
reload_necessary = False
enemy_in_sight = True
radiomessage_transmitted = None
answere = None
bekannte_gegnertypen = set()
freigeschaltet = set()



#------------------------------------------------------------------------------------------------------
#DAS DEPOT / VORRAT

waren = {"medkit": 25, "munitionskiste": 15, "panzerplatte": 90, "reparaturkit": 60}   #Preisangabe, keine Menge!
stapelbar = {"medkit": False, "munitionskiste": True, "panzerplatte": False, "reparaturkit": False}   #Wird nur für Waren und Depot benötigt. 

UPGRADES = {"zielhilfe": 60, "grossmagazin": 80, "schnellfeuer": 120} #Preisangabe, keine Menge!

verkaufswerte = {"chitinpanzer": 3, "organ": 5, "saeuredruese": 8}

vorrat = {"vaporium": 100, "munition": 40, "chitinpanzer": 2, "organ": 1, "saeuredruese": 0} #Mengenangabe!!!

GEGNERTYPEN = {"kriecher":
                {
                "kurz": "Der Kriecher tritt fast ausschließlich in riesigen Schwärmen auf, um den Feind blitzschnell zu überrennen.", 
                "lang": "Der Kriecher wurde vom der Brut zu einer perfektionierten Tötungsmaschine mutiert. Von der Größe eines großen Hundes, greift er mit messerscharfen Sensenklauen und kraftvollen Beißwerkzeugen an. Ihre wahre Stärke liegt in ihrer Masse und ihrer enormen Fortbewegungsgeschwindigkeit. Einzeln sind sie leicht zu eliminieren, doch im Kollektiv fluten sie die Schlachtfelder, umgehen Verteidigungslinien und überrennen selbst stark befestigte Stellungen in Sekundenschnelle durch ihre schiere Überzahl.",
                "zeichen": "K"
                },
            "speier":
                {
                "kurz": "Der Speier ist die vielseitige Fernkampfeinheit der Brut.", 
                "lang": "Diese berüchtigte Variante der Brut wurde von Veteranen bereits seit den ersten intergalaktischen Konflikten als „Speier“ bezeichnet. Er ist in der Lage dichte Salven agressiver Säure über mittlere Distanzen auf Boden- und Luftziele zu verspritzen. Die Substanz verätzt organische Materie in Sekundenschnelle und ist in der Lage, selbst die hochentwickelte Neostahl-Panzerung terranischer Marines in kurzer Zeit zu zersetzen.",
                "zeichen": "S"
                },
            "panzerbrut":
                {
                "kurz": "Die Panzerbrut ist ein wandelnder Festungsorganismus aus nahezu unzerstörbarem Chitin.", 
                "lang": "Die Panzerbrut ist ein biologisches Meisterwerk der defensiven Evolution. Sie ist darauf ausgelegt ist, jede Agression zu annihilieren. Ihr gesamter Körper besteht aus einer zentimeterdicken, wellenartig geschichteten Knochenpanzerung, die durch die Bildung seltener Oberflächenkristalle eine extreme Dichte erreicht hat. Gewöhnliche Projektile prallen meist wirkungslos von den Oberflächen ab. Lediglich panzerbrechende HEAT-Munition zeigt eine Wirkung, indem sie sich typischerweise beim Aufprall in eine verflüssigte Kupfernadel verwandelt, welche mit Mach 30 den Panzer durchdringt und die Eingeweide zerreißt.",
                "zeichen": "P"
                }
            }

anzeigenamen = {"medkit": "MedKit", "munitionskiste": "Munitionskiste(30 Schuss)", "panzerplatte": "Panzerplatte", "organ": "Organ",
    "vaporium": "Vaporium", "chitinpanzer": "Chitinpanzer", "saeuredruese": "Säuredrüse", "datenkern": "Datenkern", "reparaturkit": "Reparaturkit",
    "medic": "Medic", "heavy": "Heavy", "soldat": "Soldat", "engineer": "Engineer", "zielhilfe": "Zielhilfe", "grossmagazin": "Großmagazin", "schnellfeuer": "Schnellfeuer",
    "panzerbrut": "Panzerbrut", "speier": "Speier", "kiecher": "Kriecher"}

stufenaufstieg = {"stufe1": 100, "stufe2": 300, "stufe3": 900, "stufe4": 3000, "stufe5": 10000}
stufe = 0
        
inventory = []
loot_table = ["chitinpanzer", "organ", "saeuredruese", "datenkern"]
loot = []



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
        "beschreibung": "Die zentrale Bunkeranlage des Außenpostens.", "nachbarn": {
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

aktueller_sektor = sectors["depot"]


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

#-------------------------------------------------------------------------------------------------------------------
#Klassenauswahl

print("Rekrut, welches spezialisierte Training haben Sie durchlaufen?")

for klassenwahl in KLASSEN:
    print(anzeigenamen.get(klassenwahl, klassenwahl))

player_class = input("Wähle eine Klasse und gebe den Namen ein:  ")
player_class = player_class.lower().strip()

if player_class not in KLASSEN:
    player_class = input("Falsche Eingabe. Gib Soldier, Medic, Heavy oder Engineer ein: ")
    player_class = player_class.lower().strip()
elif player_class == "soldat":
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


print()

print(ascii_kopf)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#Start der Wellen
for wave in range(1, wave_to_evacuation + 1):

    round_nr = 1
    gegner_pos = []
    spawnende_gegnertypen = []
    moegliche_gegnertypen = set()

    if "grossmagazin" in freigeschaltet:
        magazin_groesse = round(magazin_groesse * 1.5)    


#SPAWN    
    if wave >= 1:
        moegliche_gegnertypen.add("kriecher")
    if wave > 3 and wave < 8:
        moegliche_gegnertypen.add("speier")
    if wave > 7:
        moegliche_gegnertypen.add("panzerbrut")
    
    for info in moegliche_gegnertypen:
        if info in bekannte_gegnertypen:
            print(GEGNERTYPEN[info]["kurz"])        
        else:
            print(GEGNERTYPEN[info]["lang"])
            bekannte_gegnertypen.add(info)

    for spawn in range(wave):
        if spawn == 0 and "panzerbrut" in moegliche_gegnertypen:
            gegner_pos.append(10)
            spawnende_gegnertypen.append("panzerbrut")
        elif (spawn == 0 and "speier" in moegliche_gegnertypen) or (spawn == 1 and "speier" not in spawnende_gegnertypen):
            gegner_pos.append(10)
            spawnende_gegnertypen.append("speier")
        else:
            gegner_pos.append(10)
            spawnende_gegnertypen.append("kriecher")



#wellenstatus
    print(f"--- Welle {wave} von {wave_to_evacuation} ---")
    print()    
    print(f"{len(gegner_pos)} Gegner befinden sich im Anmarsch.")


#Start der Runden
    while len(gegner_pos) > 0 and (kern_integritaet > 0 and health > 0):
        
        stufe = 0

        for up in stufenaufstieg:
            if exp >= stufenaufstieg[up]:   
                stufe += 1
        
        print()
        print(f"Welle {wave} | Runde {round_nr}")

# DIE ANMARSCHBAHN
        anmarschbahn = ["."] * 10
        closest_enemy = min(gegner_pos)
        
        for anmarsch_pos in range(len(gegner_pos)):     
            if gegner_pos[anmarsch_pos] > 0:            
                anmarschbahn[-gegner_pos[anmarsch_pos]] = GEGNERTYPEN[spawnende_gegnertypen[anmarsch_pos]]["zeichen"]
        
        print("Das Loch @ " + "".join(pos_on_map) + " /-\ Vorposten")


#AUSFÜHRBARE AKTIONEN       
        print("Wähle eine der Aktionen:\n--beenden --feuer --status --nachladen --inventar --umsehen --gehe --waren --kaufe x --verkaufe --upgrades --upgrade x --map --bestiarium")
        action = input("--").lower().split()   #test,schaden sind entwicklerwerkzeuge
        print()

        if len(action) == 0:
            print("Gib etwas ein")
        else:
            word1 = action[0]
            word2 = ""
            if len(action) > 1:
                word2 = action[1]
            if word1 == "feuer" or word1 == "feuern":
                if reload_necessary:
                    print("Magazin leer.")
                else:                
                    if "schnellfeuer" in freigeschaltet:
                        gegner_pos.remove(closest_enemy)
                        exp += 10
                        geladen -= 1
                        loot.append(random.choice(loot_table))
                        if geladen == 0:
                            print("Magazin ist jetzt leer!")
                            reload_necessary = True
                if reload_necessary:
                    print("Magazin leer.")
                elif len(gegner_pos) > 0: #muss zwangsweise immer größer 0 sein ohne schnellfeuer
                    gegner_pos.remove(closest_enemy)
                    geladen -= 1
                    exp += 10
                    round_nr += 1
                    loot.append(random.choice(loot_table))  
                    if geladen == 0:
                        print("Das Magazin ist jetzt leer!")
                        reload_necessary = True                        
                    for move in range(len(gegner_pos)):
                        gegner_pos[move] -= 1

                kern_integritaet -= len(gegner_pos) * 2
                health -= len(gegner_pos) * 1        

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


                kern_integritaet -= len(gegner_pos) * 2
                reload_necessary = False                  
                for move in range(len(gegner_pos)):
                    gegner_pos[move] -= 1

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
                    if len(action) == 2 and word2 in sectors[aktueller_sektor]["nachbarn"]:
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
                            if anzahl < 1:
                                print("Ungültige Eingabe.")
                            if vorrat["vaporium"] < (waren[word2] * anzahl):
                                print("Du besitzt nicht genügend Vaporium.")
                            else:                                                       # aktuell NUR MUNITION ALS STAPELBAR!!!!!
                                vorrat["munition"] += (munitionskiste * anzahl)
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

            elif word1 == "upgrades":
                if aktueller_sektor != sectors["depot"]:
                    print("Gehe zum Depot. Hier gibt es keine Upgrades.")
                for verbesserung in UPGRADES:
                    if verbesserung not in freigeschaltet:
                        print(f"{anzeigenamen.get(verbesserung, verbesserung)}: {UPGRADES[verbesserung]} Vaporium")
                    else:
                        print(f"{anzeigenamen.get(verbesserung, verbesserung)}: bereits erworben.") 

            elif word1 == "upgrade":   
                if aktueller_sektor != sectors["depot"]:
                    print("Gehe zum Depot. Hier kann man nichts kaufen.")
                elif len(action) == 1:
                    print("Kein Upgrade ausgewählt. Gebe --upgrades ein, um die Upgrades zu sehen.")                    
                elif word2 not in UPGRADES:
                    print("Dieses Upgrade ist nicht verfügbar.")
                elif vorrat["vaporium"] < UPGRADES[word2]:
                    print("Du besitzt nicht genügend Vaporium.")
                elif word2 in freigeschaltet:
                    print("Bereits erworben.")
                else:
                    vorrat["vaporium"] -= UPGRADES[word2]
                    freigeschaltet.add(word2)
                    print(f"{word2} erworben.")                    
                        
            elif word1 == "map":
                print(karte)
            
            elif word1 == "bestiarium" and len(word2) == 0:
                for gegnerauflistung in bekannte_gegnertypen:
                    print(f"{anzeigenamen.get(gegnerauflistung, gegnerauflistung)}: {GEGNERTYPEN[gegnerauflistung]["kurz"]}")
                print(f"Du hast {len(bekannte_gegnertypen)} von {len(GEGNERTYPEN)} entdeckt.")

            elif word1 == "bestiarium" and len(word2) > 0:
                if word2 not in GEGNERTYPEN:
                    print("Diesen Gegner gibt es nicht.")
                elif word2 not in bekannte_gegnertypen and word2 in GEGNERTYPEN:
                    print("Zu diesem Gegner konnten unsere Marines noch keine Informationen sammeln.")
                elif word2 in bekannte_gegnertypen and word2 in GEGNERTYPEN:
                    print(GEGNERTYPEN[word2]["lang"])
                                

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
                print(f"Gegner: {gegner_pos}")
                print(f"Erfahrung: {exp}")
                print(f"Stufe: {stufe}")
                print(f"Nachladen nötig: {reload_necessary}")
                print(f"Loot:{loot}")
                
                """
                print("Kern      [" + ("#" * kern_balken) + ("·" * kern_rest) + "]")
                print("Health    [" + ("#" * health_balken) + ("·" * health_rest) + "]")
                print("Munition  [" + ("#" * ammo_balken) + ("·" * ammo_rest) + "]")"""
    


    if kern_integritaet <= 0:        
        print("Deine Basis wurde zerstört.")
        break
        
    elif health <= 0:
        print("Du bist gestorben.")
        break
        
        

