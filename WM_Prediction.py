import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from itertools import combinations

import WM_structure
from WM_structure import Gruppen

df_Elo = pd.read_csv("Elo_Ratings.csv")
df_Wert = pd.read_clipboard("Nationalmannschaften_Wert.csv")

print(df_Elo.head())


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
    }
    gesamt_spielplan.append(gruppen_spielplan)

print(gesamt_spielplan)


#Daten

df_zusammen = df_Elo.merge(df_Wert, on="Land")
print(df_zusammen.head())

#ML Model

