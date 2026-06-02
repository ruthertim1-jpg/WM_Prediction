import numpy as np
from itertools import combinations

import WM_structure
from WM_structure import Gruppen

print(Gruppen["Gruppe A"])

# wer speilt gegen wen
gesamt_spielplan = []

for Gruppe , Teams in Gruppen.items():
    paarungen = list(combinations(Teams,2))

    spiele_pro_gruppe = []
    
    
    for team1, team2 in paarungen:
        spiele_pro_gruppe.append(f"{team1} gegen {team2}")
        #print(f"{team1} gegen {team2}")
    
    gruppen_spielplan = {
        "Gruppe": Gruppe,
        "Spiele": spiele_pro_gruppe,
        }
    gesamt_spielplan.append(gruppen_spielplan)


print(gesamt_spielplan[0])
