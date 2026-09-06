import time
import random

player_class = None
player_name = None

#equipment
medkit = None
tool = None
heavy_machinegun = None
machinegun = None


#stats
health = 100
damage = 10
armor = 5

#resouces
scrap = 0
ammo = 40
core = 100
ammo_max = 40
core_max = 100
exp = 0

inventory = []

balken_laenge = 10


wave_to_evacuation = 20
recruts = 0
enemy = []
reload_necessary = False
enemy_in_sight = None
radiomessage_transmitted = None
answere = None


last_message = "Kzzz... Brauchen dringend Verstärkung! kschhh... Wir werden überrannt! Kzzz... Beeilt euch! ...chhh"
lights = "Notbeleuchtung" # kürzere Sichtweite?


ascii_kopf = """
                                     VORPOSTEN              
  /---------------------------------------------------------------------------\ 
 / *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *\ 
/                                                                               \ 
"""

print(f"Health: {health} | Ammo: {ammo} | Schrott: {scrap} | Rekruten: {recruts} | Wellen bis zur Evakuierung: {wave_to_evacuation} ")

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
    medkit = True
elif player_class == "heavy":
    health = int(health * 1.4)
    damage = int(damage * 1.4)
    armor = int(armor * 2)
    heavy_machinegun = True
elif player_class == "engineer":
    health = int(health * 0.9)
    damage = int(damage * 0.7)
    armor = int(armor * 0.8)
    tool = True

health_max = health

print()
print(f"Klasse: {player_class}")
print(f"Health: {health}")
print(f"Damage: {damage}")
print(f"Armor: {armor}")

print()
time.sleep(1)
print()

print(f"Wir haben nur noch {ammo} Munition übrig.")
print(f"Die Kernintegrität unserer Einrichtung beträgt zwar noch {core}%,")
print(f"aber uns verbleiben nur noch {scrap} Schrott für Reparaturen.")

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
loot_table = ["schrott", "panzerplatte", "datenkern", "munitionskasten"]
loot = []


for wave in range(1, wave_to_evacuation + 1):
    print(f"--- Welle {wave} von {wave_to_evacuation} ---")
    
    round_nr = 1
    enemy = []


    for spawn in range(wave):
        enemy.append(5)
        
    print(f"{len(enemy)} Gegner befinden sich im Anmarsch.")
    

    while len(enemy) > 0 and (core > 0 and health > 0):
        print(f"Welle {wave} | Runde {round_nr}")

        pos_on_map = ["."] * 5
        closest_enemy = min(enemy)
        
        for enemy_pos in range(len(enemy)):
            if enemy[enemy_pos] > 0:
                pos_on_map[-enemy[enemy_pos]] = "k"
        print("Das Loch @ " + "".join(pos_on_map) + " /-\ Vorposten")
        

        action = input("Wähle eine Aktion: beenden/feuer/status/nachladen/inventar> ").lower().split()   #test,schaden sind entwicklerwerkzeuge
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
                    print("Keine Munition mehr.")
                else:
                    print("Feuer frei!")
                    ammo -= 1
                    enemy.remove(closest_enemy)
                    exp += 10
                    round_nr += 1
                    core -= len(enemy) * 2 
                    health -= len(enemy) * 1
                    loot.append(random.choice(loot_table))
                    if ammo == 0:
                        print("Munition ist jetzt leer!")
                        reload_necessary = True                        
                    for move in range(len(enemy)):
                        enemy[move] -= 1

            elif word1 == "nachladen" or (word1 == "lade" and word2 == "nach") :
                print("Lade nach!")
                round_nr += 1
                ammo = 40
                core -= len(enemy) * 2
                reload_necessary = False                  
                for move in range(len(enemy)):
                    enemy[move] -= 1

                
            elif word1 == "beenden" or (word1 == "welle" and word2 == "beenden"):
                print(f"Welle {wave} beendet")
                break

            elif word1 == "inventar" or (word1 == "inventar" and word2 == "anzeigen"):
                print(inventory)

            elif word1 == "nimm":
                if len(action) == 1:
                    print("Nichts ausgewählt.")
                else:
                    if word2 in loot and len(inventory) < 10:
                        inventory.append(word2)
                        loot.remove(word2)
                        print(f"{word2} aufgenommen.")
                    else:
                        print("Das liegt hier nicht.")
            
            elif word1 == "lege":
                if len(action) == 1:
                    print("Nichts ausgewählt.")
                else:
                    if word2 in inventory:
                        inventory.remove(word2)
                        loot.append(word2)
                        print(f"{word2} abgelegt.")
                    else:
                        print("Das besitze ich nicht.")
            
            elif word1 == "status" or (word1 == "status" and  word2 == "anzeigen"):
                
                kern_balken = round((core / core_max) * balken_laenge)      #Meine Balkenanzeigen rechnen alle Werte auf die Balkenlänge 10 um und übschreiten keine Grenzen.
                ammo_balken = round((ammo / ammo_max) * balken_laenge)
                health_balken = round((health / health_max) * balken_laenge)
                kern_rest = balken_laenge - kern_balken
                ammo_rest = balken_laenge - ammo_balken
                health_rest = balken_laenge - health_balken
                
                print(f"Kern: {core}")
                print(f"Health: {health}")
                print(f"Armor: {armor}")
                print(f"Schrott: {scrap}")
                print(f"Ammo: {ammo}")
                print(f"Schaden: {damage}")
                print(f"Rekruten: {recruts}")
                print(f"Gegner: {enemy}")
                print(f"Erfahrung: {exp}")
                print(f"Nachladen nötig: {reload_necessary}")
                print(f"Loot:{loot}")
                print(f"Inventar: {inventory}")
                print("Kern      [" + ("#" * kern_balken) + ("·" * kern_rest) + "]")
                print("Health    [" + ("#" * health_balken) + ("·" * health_rest) + "]")
                print("Munition  [" + ("#" * ammo_balken) + ("·" * ammo_rest) + "]")

            
    if core <= 0:        
        break
        print("Deine Basis wurde zerstört.")
    elif health <= 0:
        break
        print("Du bist gestorben.")
        

