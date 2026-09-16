
def erster_langer_name(namen):
    for name in namen:
        if len(name) > 5:
            return name          # hier ist Schluss — der Rest läuft nicht
    return "keiner gefunden"


namensliste = {"adol", "maxi", "hubertus", "anne"}
name = erster_langer_name(namensliste)
print(name)