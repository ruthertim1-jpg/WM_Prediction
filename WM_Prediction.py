import numpy as np
from itertools import combinations

import WM_structure
from WM_structure import Gruppen




# wer speilt gegen wen
gesamt_spielplan = []

for Gruppe , Teams in Gruppen.items():
    paarungen = list(combinations(Teams,2)) #´combinations# verhindet doppelte paarungen

    spiele_pro_gruppe = [] 
    
    
    for team1, team2 in paarungen:
        spiele_pro_gruppe.append(f"{team1} gegen {team2}") # append fügt zu bereits bestehenden liste hinten das hinzu, wass in seiner Klammer kommt
        #print(f"{team1} gegen {team2}")
    
    gruppen_spielplan = {
        "Gruppe": Gruppe,
        "Spiele": spiele_pro_gruppe,
         "":print()
    }
    gesamt_spielplan.append(gruppen_spielplan)


print(gesamt_spielplan)
