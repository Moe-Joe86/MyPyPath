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
reload_necessary = False
enemy_in_sight = True
radiomessage_transmitted = None
answere = None
bekannte_gegnertypen = set()    #Jeder Eintrag in bekannte_gegnertypen steht auch als Schlüssel in GEGNERTYPEN.
freigeschaltet = set()   #Jeder Eintrag in freigeschaltet steht auch als Schlüssel in UPGRADES.




#------------------------------------------------------------------------------------------------------
#DAS DEPOT / VORRAT

waren = {"medkit": 25, "munitionskiste": 15, "panzerplatte": 90, "reparaturkit": 60}   #Preisangabe, keine Menge!
stapelbar = {"munitionskiste"}   #Wird nur für Waren und Depot benötigt. 

UPGRADES = {"zielhilfe": 60, "grossmagazin": 80, "schnellfeuer": 120} #Preisangabe, keine Menge!

verkaufswerte = {"chitinpanzer": 3, "organ": 5, "saeuredruese": 8}

vorrat = {"vaporium": 100, "munition": 40, "chitinpanzer": 2, "organ": 1, "saeuredruese": 0} #Mengenangabe!!!

GEGNERTYPEN = {"kriecher":
                {
                "kurz": "Der Kriecher tritt fast ausschließlich in riesigen Schwärmen auf, um den Feind blitzschnell zu überrennen.", 
                "lang": "DER KRIECHER: \nDer Kriecher wurde vom der Brut zu einer perfektionierten Tötungsmaschine mutiert. Von der Größe eines großen Hundes, \ngreift er mit messerscharfen Sensenklauen und kraftvollen Beißwerkzeugen an. Ihre wahre Stärke liegt in ihrer Masse und \nihrer enormen Fortbewegungsgeschwindigkeit. Einzeln sind sie leicht zu eliminieren, doch im Kollektiv fluten sie die Schlachtfelder, \numgehen Verteidigungslinien und überrennen selbst stark befestigte Stellungen in Sekundenschnelle durch ihre schiere Überzahl.",
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
    "panzerbrut": "Panzerbrut", "speier": "Speier", "kriecher": "Kriecher"}

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

aktueller_sektor = "depot"


#---------------------------------------------------------------------------------------------------------
#FUNKTIONEN AUSGABE
def empty_magazine_msg():
    print("Das Magazin ist leer.")   

def no_more_ammo_msg():
    print("Wir haben keine Munition mehr.")

def reloaded_msg():
    print("Nachgeladen.")

def not_depot_msg():
    print("Gehe zum Depot. Hier gibt es keine Waren.")

def sector_not_exist():
    print("Diesen Sektor gibt es nicht.")  

def keine_ware_gewählt_msg():
    print("Keine Ware ausgewählt. Gebe --waren ein, um die Waren zu sehen.") 

def ware_nicht_verfügbar_msg():
    print("Diese Ware ist nicht verfügbar.")

def kein_vaporium_msg():
    print("Du besitzt nicht genügend Vaporium.")

def inventar_voll_msg():
    print("Dein Inventar ist voll.")

def ungueltige_eingabe_msg():
    print("Ungültige Eingabe.")

def gekauft_stapelbar_msg(anzahl, anzeigenamen, word2):
    print(f"{anzahl} {anzeigenamen.get(word2, word2)} erfolgreich gekauft.")

def kauf_menge_msg():
    print(f"Wieviele möchtest du kaufen?")

def gekauft_msg(anzeigenamen, word2):
    print(f"{anzeigenamen.get(word2, word2)} erfolgreich gekauft.")  

def upgrades_anzeigen_msg(freigeschaltet, anzeigenamen):
    for verbesserung in UPGRADES:
        if verbesserung not in freigeschaltet:
            print(f"{anzeigenamen.get(verbesserung, verbesserung)}: {UPGRADES[verbesserung]} Vaporium")
        else:
            print(f"{anzeigenamen.get(verbesserung, verbesserung)}: bereits erworben.") 

def nehmen_msg(anzeigenamen, word2):
    print(f"{anzeigenamen.get(word2, word2)} aufgenommen.")

def ablegen_msg(anzeigenamen, word2):
    print(f"{anzeigenamen.get(word2, word2)} abgelegt.")

def liegt_nicht():
    print("Das liegt hier nicht.") 

def umsehen_msg(aktueller_sektor, sectors, kern_integritaet):
    print(sectors[aktueller_sektor]["beschreibung"])               
    print(f"Nachbarsektoren: {sectors[aktueller_sektor]['nachbarn']}")
    if "integritaet" in aktueller_sektor:
        print(f"Integritaet: {sectors[aktueller_sektor]['integritaet']}")  
    else:
        print(f"Integritaet: {kern_integritaet}")



def besitze_nicht():
    print("Das besitze ich nicht.")

def nichts_ausgewaehlt():
    print("Nichts ausgewählt.")

def upgrade_erworben(word2):
    print(f"{word2} erworben.")   

def verkauft_msg(vorrat, anzeigenamen, verkaufswerte):
    print(f"{vorrat[verkauft]} {anzeigenamen.get(verkauft, verkauft)} für {(vorrat[verkauft] * verkaufswerte[verkauft])} Vaporium verkauft.")

def verkauft_abschluss_msg(bezahlung, vorrat):
    print()
    print(f"Du hast insgesamt {bezahlung} Vaporium erhalten.")
    print(f"Du besitzt jetzt {vorrat['vaporium']} Vaporium.")

def keine_richtung_msg():
    print("Keine Richtung ausgewählt. Nutze --umsehen, um Richtungen zu sehen.")

def inventar_msg(inventory, vorrat, anzeigenamen):
    print("Gegenstände und Vorrat:")
    for gegenstand in inventory:
        print(f"- {anzeigenamen.get(gegenstand, gegenstand)}")
    for gegenstand in vorrat:
        print(f"- {vorrat[gegenstand]} {anzeigenamen.get(gegenstand, gegenstand)}")



#-----------------------

def schaden_an_gegner(gegner_pos, spawnende_gegnertypen):
    del gegner_pos[i]
    del spawnende_gegnertypen[i]

def schaden_an_base():
    print()


#FUNKTIONEN RECHNUNGEN/ENTSCHEIDUNGEN
def feuern():
    if reload_necessary:
        empty_magazine()
    else:                
        schaden_an_gegner()
    if len(gegner_pos) > 0:
        closest_enemy = min(gegner_pos)
        i = gegner_pos.index(closest_enemy)                    
    geladen -= 1
    exp += 10
    loot.append(random.choice(loot_table))  
    round_nr += 1                    
    if geladen == 0:
        empty_magazine()
        reload_necessary = True                        
    for move in range(len(gegner_pos)):
        gegner_pos[move] -= 1                    
                                    
    if "schnellfeuer" in freigeschaltet and len(gegner_pos) > 0:                       
        if reload_necessary:
            empty_magazine()                      
        else:
            schaden_an_gegner(gegner_pos, spawnende_gegnertypen)
            exp += 10
            geladen -= 1
            loot.append(random.choice(loot_table))
            if geladen == 0:
                empty_magazine()
                reload_necessary = True
    kern_integritaet -= len(gegner_pos) * 2
    health -= len(gegner_pos) * 1    

def zeige_status(kern_integritaet, vorrat, health, stufe, gegner_pos, freigeschaltet):
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
    print(f"Ammo: {vorrat['munition']}")
    print(f"Gegner: {gegner_pos}")
    print(f"Stufe: {stufe}")
    print(f"Upgrades:{freigeschaltet}")
    
    """
    print("Kern      [" + ("#" * kern_balken) + ("·" * kern_rest) + "]")
    print("Health    [" + ("#" * health_balken) + ("·" * health_rest) + "]")
    print("Munition  [" + ("#" * ammo_balken) + ("·" * ammo_rest) + "]")"""


def nachladen(round_nr, reloaded, vorrat, geladen, reload_necessary, kern_integritaet):
    round_nr += 1
    reloaded = False
    while vorrat["munition"] > 0 and geladen < magazin_groesse:
        vorrat["munition"] -= 1
        geladen += 1
        reloaded = True
        reload_necessary = False
    if vorrat["munition"] == 0:
        no_more_ammo()        
    elif reloaded == True:
        reloaded_msg()

    kern_integritaet -= len(gegner_pos) * 2
    reload_necessary = False                  
    for move in range(len(gegner_pos)):
        gegner_pos[move] -= 1

def einkaufen(aktueller_sektor, vorrat, stapelbar, inventory):
    if aktueller_sektor != "depot":
        not_depot_msg()
    elif len(action) == 1:
        keine_ware_gewählt_msg()                           
    elif word2 not in waren:
        ware_nicht_verfügbar_msg()
    elif vorrat["vaporium"] < waren[word2]:
        kein_vaporium_msg()
    elif word2 not in stapelbar and len(inventory) >= max_inventory:
        inventar_voll_msg()
    else:
        if len(action) == 2:                       
            if word2 not in stapelbar:
                inventory.append(word2)
                vorrat["vaporium"] -= waren[word2]
                gekauft_msg(anzeigenamen, word2) 
            else:
                anzahl = int(input())
                if anzahl < 1:
                    ungueltige_eingabe_msg()           
                if vorrat["vaporium"] < (waren[word2] * anzahl):
                    kein_vaporium_msg()
                else:                                                       # aktuell NUR MUNITION ALS STAPELBAR!!!!!
                    vorrat["munition"] += (munitionskiste * anzahl)
                    vorrat["vaporium"] -= (waren[word2] * anzahl)
                    gekauft_stapelbar_msg(anzahl, anzeigenamen, word2)


def verkaufen(aktueller_sektor, verkaufswerte, vorrat, anzeigenamen):
    if aktueller_sektor != "depot":
        not_depot_msg()
    else:  
        bezahlung = 0             
        for verkauft in verkaufswerte:
            verkauft_msg(vorrat, anzeigenamen, verkaufswerte)
            bezahlung += (vorrat[verkauft] * verkaufswerte[verkauft])
            vorrat[verkauft] = 0                        
        vorrat["vaporium"] += bezahlung  
        return vorrat["vaporium"]
        verkauft_abschluss_msg(bezahlung, vorrat)  


def upgraden(vorrat, freigeschaltet):
    if aktueller_sektor != "depot":
        not_depot_msg()
    elif len(action) == 1 or word2 not in UPGRADES or word2 in freigeschaltet:
        ungueltige_eingabe_msg()                 
    elif vorrat["vaporium"] < UPGRADES[word2]:
        kein_vaporium_msg()
    else:      
        vorrat["vaporium"] -= UPGRADES[word2]    
        freigeschaltet.add(word2)
        upgrade_erworben()
        if "grossmagazin" in freigeschaltet:
            magazin_groesse = round(magazin_groesse * 1.5)   
            return magazin_groesse

def wechsel_sektor(sectors, aktueller_sektor, word2):
    if len(action) == 1:
        keine_richtung_msg()

    else:
        if len(action) == 2 and word2 in sectors[aktueller_sektor]["nachbarn"]:
            print(f"Ich gehe zum Sektor {word2}.")
            aktueller_sektor = word2 #vergeht eine Runde?
            return aktueller_sektor
        else:
            sector_not_exist()


def nehmen(loot, inventory, vorrat, word2):
    if len(action) == 1:
        ungueltige_eingabe_msg()
    else:
        if word2 in loot:
            if word2 not in stapelbar:
                if len(inventory) >= max_inventory:
                    inventar_voll_msg()
                else:
                    inventory.append(word2)
                    loot.remove(word2)
                    nehmen_msg(anzeigenamen, word2)
            else:
                vorrat[word2] += 1
                loot.remove(word2)
                nehmen_msg(anzeigenamen, word2)
        else:
            liegt_nicht()

def waren():                                                     #kein Logik, nur ausgabe
    if aktueller_sektor != "depot":
        print("Gehe zum Depot. Hier gibt es keine Waren.")
    else:
        for ware in waren:
            print(f"{anzeigenamen.get(ware, ware)}: {waren[ware]} Vaporium")
            print()
            print(f"Du besitzt {vorrat["vaporium"]}.")
                    #aufgabe 6 muss überarbeitet werden? Alle waren ohne Schleife angezeigt. Ware wird jetzt schon ohne Mehrarbeit ausgegeben?!?!?!?

def ablegen(inventory, loot, word2):
    if len(action) == 1:
        nichts_ausgewaehlt()
    else:
        if len(action) == 2 and word2 in inventory:
            inventory.remove(word2)
            loot.append(word2)
            ablegen_msg(anzeigenamen, word2)
        else:
            besitze_nicht()

def bestiarium():                                                #kein Logik, nur ausgabe
    if len(word2) == 0:
        for gegnerauflistung in bekannte_gegnertypen:
            print(f"{anzeigenamen.get(gegnerauflistung, gegnerauflistung)}: {GEGNERTYPEN[gegnerauflistung]["kurz"]}")
        print(f"Du hast {len(bekannte_gegnertypen)} von {len(GEGNERTYPEN)} entdeckt.")
    else:
        if word2 not in GEGNERTYPEN:
            print("Diesen Gegner gibt es nicht.")
        elif word2 not in bekannte_gegnertypen and word2 in GEGNERTYPEN:
            print("Zu diesem Gegner konnten unsere Marines noch keine Informationen sammeln.")
        elif word2 in bekannte_gegnertypen and word2 in GEGNERTYPEN:
            print(GEGNERTYPEN[word2]["lang"])  

def verarbeite_befehl():
    action = input("--")
    action = action.lower().split()
    if len(action) == 0:
        ungueltige_eingabe_msg()

    else:
        word1 = action[0]
        word2 = ""
        if len(action) > 1:
            word2 = action[1]


        if word1 == "feuer" or word1 == "feuern":
            feuern()

        elif word1 == "nachladen":
            nachladen()

        elif word1 == "inventar":
            inventar_msg(inventory, vorrat, anzeigenamen)

        elif word1 == "nimm":
            nehmen(loot, inventory, vorrat, word2)
        
        elif word1 == "lege":
            ablegen(inventory, loot, word2)

        elif word1 == "umsehen":
            umsehen_msg(aktueller_sektor, sectors, kern_integritaet)   

        elif word1 == "gehe":
            wechsel_sektor(sectors, aktueller_sektor, word2)
        
        elif word1 == "waren":
            waren()
        
        elif word1 == "kaufe":
            einkaufen(aktueller_sektor, vorrat, stapelbar, inventory)              
        
        elif word1 == "verkaufe" or word1 == "verkaufen":
            verkaufen(aktueller_sektor, verkaufswerte, vorrat, anzeigenamen)

        elif word1 == "upgrades":
            upgrades_anzeigen_msg(freigeschaltet, anzeigenamen)

        elif word1 == "upgrade":   
            upgraden()
                    
        elif word1 == "map":
            print(karte)
        
        elif word1 == "bestiarium":
            bestiarium()
                            
        elif word1 == "status":
            zeige_status()


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


#SPAWN    
    if wave >= 1:
        moegliche_gegnertypen.add("kriecher")
    if wave > 3:
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
        i = gegner_pos.index(closest_enemy)
        for anmarsch_pos in range(len(gegner_pos)):     
            if gegner_pos[anmarsch_pos] > 0:            
                anmarschbahn[-gegner_pos[anmarsch_pos]] = GEGNERTYPEN[spawnende_gegnertypen[anmarsch_pos]]["zeichen"]
        
        print("Das Loch @ " + "".join(anmarschbahn) + " /-\ Vorposten")

#EINE AKTION!
# --------------      
        print("Wähle eine der Aktionen:\n--beenden --feuer --status --nachladen --inventar --umsehen --gehe --waren --kaufe x --verkaufe --upgrades --upgrade x --map --bestiarium")

        print()
        verarbeite_befehl()  
#---------------

    if kern_integritaet <= 0:        
        print("Deine Basis wurde zerstört.")
        break
        
    elif health <= 0:
        print("Du bist gestorben.")
        break
        
        

