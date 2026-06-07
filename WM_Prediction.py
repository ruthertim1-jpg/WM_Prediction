import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from itertools import combinations
import WM_structure
from WM_structure import Gruppen

import unicodedata


df_Elo = pd.read_csv("ELO_Ratings.csv", encoding= "latin-1", sep=";")
df_Wert = pd.read_csv("Nationalmannschaften_Wert.csv", sep=";")
df_results = pd.read_csv("results.csv")

wm_länderliste = []
for Land in Gruppen.values():
    wm_länderliste.extend(Land)

df_resultswm = df_results[
    df_results["home_team"].isin(wm_länderliste) & 
    df_results["away_team"].isin(wm_länderliste)
]
#beide Tabellen zusammengeführt
df_zusammen = df_Elo.merge(df_Wert, on="Land")
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



#Daten vorbereitung
X=[]
y=[]

df_features = df_zusammen.set_index("Land")
features = ["durchschnitts-Alter", "Marktwert","Rank","Rating","Average_Rank","Kadergröße","Matches_Total","Goals_For","Goals_Against"]

def normalisierte_Ergebnis(Tore):
    if Tore["home_score"] > Tore["away_score"]:
        return 1 # 1= heim siegt
    elif Tore["home_score"] < Tore["away_score"]:
        return 2 # 2= gast siegt
    else:
        return 0 # Untentschieden
    
df_results["Ergebnis"] = df_results.apply(normalisierte_Ergebnis,axis=1) # einfügen von 1,2,0 in die Tabellen
df_resultswm = df_results[
    df_results["home_team"].isin(wm_länderliste) & 
    df_results["away_team"].isin(wm_länderliste)].copy() ######## Gemini###### 
df_resultswm["Ergebnis"] = df_resultswm.apply(normalisierte_Ergebnis,axis=1)



for zeilennummer, Zeileninfo in df_resultswm.iterrows():
    heim_Team = Zeileninfo["home_team"]
    gast_Team = Zeileninfo["away_team"]

    if heim_Team in df_features.index and gast_Team in df_features.index:   ###########Geminis code ############### dient zur absicherung, dass nur Spiele betrachtet werden, zu denen ich auch Daten habe
        features_heim = df_features.loc[heim_Team, features].values
        features_gast = df_features.loc[gast_Team, features].values
        Trainingsparameter = features_heim - features_gast
        X.append(Trainingsparameter)
        y.append(Zeileninfo["Ergebnis"])

X = np.array(X)
y = np.array(y)


#Random Forest Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=200,random_state=42, max_depth= 3,min_samples_split=5)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
#print(y_pred)
genauigkeit = accuracy_score(y_test,y_pred)
print (f"Genauigkeit:",genauigkeit)


#echte Vorhersage


print ("-----Vorhersage------")
for Gruppenname in gesamt_spielplan:
    gruppen_punkte = {}
    aktuelle_teams = Gruppen[Gruppenname["Gruppe"]]

    for team in aktuelle_teams:
        gruppen_punkte[team] = 0
    print(f"\n {Gruppenname["Gruppe"]}")

    for Spiele in Gruppenname["Spiele"]:
        team1, team2 = Spiele.split("|")
        features_t1 = df_features.loc[team1, features].values
        features_t2 = df_features.loc[team2, features].values
        differents = features_t1 - features_t2
        TippdesModles = model.predict(differents.reshape(1,-1))[0]
        if TippdesModles == 1:
            gruppen_punkte[team1] += 3  # Team 1 bekommt 3 Punkte
        elif TippdesModles == 2:
            gruppen_punkte[team2] += 3  # Team 2 bekommt 3 Punkte
        else:
            gruppen_punkte[team1] += 1  # Beide bekommen 1 Punkt
            gruppen_punkte[team2] += 1


    #Tabelle erstellen
    df_Tabelle = pd.DataFrame(list(gruppen_punkte.items()), columns= ["Land", "Punkte"])
    df_Tabelle = df_Tabelle.sort_values(by="Punkte",ascending=False).reset_index(drop=True)
    df_Tabelle.index= df_Tabelle.index +1

    print(df_Tabelle)
    