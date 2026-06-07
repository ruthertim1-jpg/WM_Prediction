import numpy as np
import pandas as pd


df_Elo = pd.read_csv("ELO_Ratings.csv", encoding= "latin-1", sep=";")
df_Wert = pd.read_csv("Nationalmannschaften_Wert.csv", sep=";")

#Gruppen Dictionary:
Gruppen = {
    "Group A": ["Mexico", "South Africa", "South Korea", "Czech Republic"],
    "Group B": ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
    "Group C": ["Brazil", "Morocco", "Haiti", "Scotland"],
    "Group D": ["United States", "Paraguay", "Australia", "Turkey"],
    "Group E": ["Germany", "Curaçao", "Ivory Coast", "Ecuador"],
    "Group F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "Group G": ["Belgium", "Egypt", "Iran", "New Zealand"],
    "Group H": ["Spain", "Cape Verde", "Saudi Arabia", "Uruguay"],
    "Group I": ["France", "Senegal", "Iraq", "Norway"],
    "Group J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "Group K": ["Portugal", "Democratic Republic of the Congo", "Uzbekistan", "Colombia"],
    "Group L": ["England", "Croatia", "Ghana", "Panama"],
}

# sechtzentelfinale
Sechzehntel= {

}
#Achtelfinale
Achtelfinale = {
    "Spiel A": [" A1","B2"],
    "Spiel B": [],
    "Spiel C": [],
    "Spiel D": [], 
    "Spiel E": [],
    "Spiel F": [],
    "Spiel G": [],
    "Spiel H": [],
}

#1Viertelfinale

#1 Halbfinale

#Finale

# Datenstruktur

