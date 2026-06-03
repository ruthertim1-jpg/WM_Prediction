import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from itertools import combinations

import WM_structure
from WM_structure import Gruppen

df_Elo = pd.read_csv("ELO_Ratings.csv", sep=";")
df_Wert = pd.read_csv("Nationalmannschaften_Wert.csv", sep=";")
df_results = pd.read_csv("results.csv")
df_resultswm = df_results[
    df_results["home_team"].isin(Gruppen) & 
    df_results["away_team"].isin(Gruppen)
]
#print(df_resultswm.head())
#print(df_resultswm)


# wer speilt gegen wen
gesamt_spielplan = []
for Gruppe , Teams in Gruppen.items():
    paarungen = list(combinations(Teams,2)) #´combinations# verhindet doppelte paarungen
    spiele_pro_gruppe = [] 

    for team1, team2 in paarungen:
        spiele_pro_gruppe.append(f"{team1}|{team2}") # append fügt zu bereits bestehenden liste hinten das hinzu, wass in seiner Klammer kommt
        #print(f"{team1} gegen {team2}")
    
    gruppen_spielplan = {
        "Gruppe": Gruppe,
        "Spiele": spiele_pro_gruppe,
    }
    gesamt_spielplan.append(gruppen_spielplan)
#print(gesamt_spielplan)


#Daten
df_zusammen = df_Elo.merge(df_Wert, on="Land")

wm_länderliste=[]
for Land in Gruppen.values():
    wm_länderliste.extend(Land)
    df_zusammen[df_zusammen.Land.isin(wm_länderliste)]
#print(wm_länderliste)


#ML Model
df_features = df_zusammen.set_index("Land")

features = [
    "ø-Alter", "Marktwert","Rank", "Losses","Wins","Draws","Matches_Total",
    "Goals_For", "Goals_Against","Rating",
]
