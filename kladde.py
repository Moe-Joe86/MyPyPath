auto = "auto"
fahrrad = "fahhrad"
traktor = "traktor"



inventar = [auto, fahrrad, traktor]
print(inventar)

inventar.append("schiff")
print(inventar)

inventar = inventar.append("bohrer") 
print(inventar)

"""
eingabe = input("Wähle feuer oder feuer machen").lower().split()
if eingabe[0] == "feuer" and len(eingabe) == 1:
    print("feuer")
if eingabe[0] == "feuer" and eingabe[1] == "machen" and len(eingabe) == 2:
    print("feuer machen")
"""

eingabe = input("Wähle feuer oder feuer machen").lower().split()
if len(eingabe) == 1:
    if eingabe[0] == 'feuer':
        print("feuer")

if len(eingabe) == 2:
    if eingabe[0] == "feuer" and eingabe[1] == 'machen':
        print("feuer machen")
