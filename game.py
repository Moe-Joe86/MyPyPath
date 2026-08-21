import time

player_class = None
player_name = None

#equipment
medkit = None
werkzeug = None
heavy_machinegun = None
machinegun = None


#stats
health = 100
damage = 10
armor = 5

#resouces
schrott = 0
ammo = 40
kern = 100
ammo_max = 40
kern_max = 100

inventar = []

balken_laenge = 10


wellen_bis_evakuierung = 20
rekruten_anzahl = 0
gegner_anzahl = 1
nachladen_noetig = False
ziel_in_sicht = None
funkspruch_abgesetzt = None
antwort = None


letzte_meldung = "Kzzz... Brauchen dringend Verstärkung! kschhh... Wir werden überrannt! Kzzz... Beeilt euch! ...chhh"
beleuchtung = "Notbeleuchtung" # kürzere Sichtweite?


ascii_kopf = """
                                     VORPOSTEN              
  /---------------------------------------------------------------------------\ 
 / *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\ 
/                                                                               \ 
"""

print(f"Health: {health} | Ammo: {ammo} | Schrott: {schrott} | Rekruten: {rekruten_anzahl} | Wellen bis zur Evakuierung: {wellen_bis_evakuierung} ")

"""
print(f"Aufgezeichnete Durchsage: {letzte_meldung}")
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
print("-Soldat")
print("-Medic")
print("-Heavy")
print("-Engineer")
print()
player_class = input("Wähle eine Klasse und gebe den Namen ein:  ")
player_class = player_class.lower().strip()

if player_class != "soldat" and player_class != "medic" and player_class != "heavy" and player_class != "engineer": # hiermit möchte ich Auftrag 3 ohne else erfüllen. Diese Bedingung kann ich auch mit == und einem else erfüllen, ist aber kostspieliger. bewusste entscheidung gegen die Aufgabe!
    player_class = input("Falsche Eingabe. Gib Soldat, Medic, Heavy oder Engineer ein: ")
    player_class = player_class.lower().strip()

if player_class == "soldat":
    health = 100
    damage = 10
    armor = 5
    machinegun = True
elif player_class == "medic":
    health *=  0.8
    damage *= 0.6
    armor *= 0.6
    medkit = True
elif player_class == "heavy":
    health *= 1.4
    damage *= 1.4
    armor *= 2
    heavy_machinegun = True
elif player_class == "engineer":
    health *= 0.9
    damage *= 0.7
    armor *= 0.8
    werkzeug = True

print()
print(f"Klasse: {player_class}")
print(f"Health: {health}")
print(f"Damage: {damage}")
print(f"Armor: {armor}")

print()
time.sleep(1)
print()

print(f"Wir haben nur noch {ammo} Munition übrig.")
print(f"Die Kernintegrität unserer Einrichtung beträgt zwar noch {health}%,")
print(f"aber uns verbleiben nur noch {schrott} Schrott für Reparaturen.")

print()
time.sleep(1)

print(f"Aufgezeichnete Durchsage: {letzte_meldung}")

print()
time.sleep(1)
print()
"""
print("Feinde nähern sich. Du siehst etwas ungewöhnliches. Setzt du einen Funkspruch ab?")
antwort = input("Ja oder Nein > ")
antwort = antwort.lower().strip()

repeat = True
while repeat:
    if antwort == "ja":
        funkspruch_abgesetzt = True
        print("Ein Funkspruch wurde abgesetzt.")
        repeat = False
    elif antwort == "nein":
        funkspruch_abgesetzt = False
        print("Du hast keinen Funkspruch abgesetzt.")
        repeat = False
    else:
        antwort = input("Falsche Eingabe. Schreibe Ja oder Nein: ")

"""
ziel_in_sicht = True
print()

print(ascii_kopf)


for welle in range(1, wellen_bis_evakuierung + 1):
    print(f"--- Welle {welle} von {wellen_bis_evakuierung} ---")
    
    runde = 1
    gegner_anzahl = welle              # Auftrag 14 maximal primitiv erledigt

    while gegner_anzahl > 0 and kern > 0:
        print(f"Welle {welle} | Runde {runde}")
        eingabe = input("Wähle eine Aktion: beenden/test/schaden/feuer/status/nachladen> ").lower().strip()   #test,schaden sind entwicklerwerkzeuge

        if eingabe == "test":
            gegner_anzahl -= 1
            print(f"Noch {gegner_anzahl} Gegner übrig.")
        elif eingabe == "schaden":
            kern -= 32
            print(f"{kern} Kern")
        elif eingabe == "feuer" and ammo > 0:
            print("Feuer frei!")
            ammo -=1
            gegner_anzahl -= 1
            runde += 1
            kern -= gegner_anzahl * 2
            if ammo == 0:
                print("Munition ist jetzt leer!")
                nachladen_noetig = True
        elif eingabe == "feuer" and nachladen_noetig:
            print("Keine Munition mehr")
        elif eingabe == "nachladen":
            print("Lade nach!")
            runde += 1
            ammo = 40
            kern -= gegner_anzahl * 2
            nachladen_noetig = False
            
        elif eingabe == "beenden":
            print(f"Welle {welle} beendet")
            break
        elif eingabe == "status":
            
            kern_balken = round((kern / kern_max) * balken_laenge)      #Meine Balkenanzeigen rechnen alle Werte auf die Balkenlänge 10 um und übschreiten keine Grenzen.
            ammo_balken = round((ammo / ammo_max) * balken_laenge)
            kern_rest = balken_laenge - kern_balken
            ammo_rest = balken_laenge - ammo_balken
            
            print(f"Kern: {kern}")
            print(f"Health: {health}")
            print(f"Armor: {armor}")
            print(f"Schrott: {schrott}")
            print(f"Ammo: {ammo}")
            print(f"Schaden: {damage}")
            print(f"Rekruten: {rekruten_anzahl}")
            print(f"Gegner: {gegner_anzahl}")
            print(f"Nachladen nötig: {nachladen_noetig}")
            print("Kern      [" + ("#" * kern_balken) + ("·" * kern_rest) + "]")
            print("Munition  [" + ("#" * ammo_balken) + ("·" * ammo_rest) + "]")
        
    if kern <= 0:
            break
        

