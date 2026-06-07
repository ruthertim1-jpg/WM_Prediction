import numpy as np
import pandas as pd


df_Elo = pd.read_csv("ELO_Ratings.csv", encoding= "latin-1", sep=";")
df_Wert = pd.read_csv("Nationalmannschaften_Wert.csv", sep=";")

#Gruppen Dictionary:
Gruppen = {
    "Gruppe A": ["Mexiko", "Südafrika", "Republik Korea", "Tschechien"],
    "Gruppe B": ["Kanada", "Bosnien und Herzegowina", "Katar", "Schweiz"],
    "Gruppe C": ["Brasilien", "Marokko", "Haiti", "Schottland"],
    "Gruppe D": ["USA", "Paraguay", "Australien", "Türkei"],
    "Gruppe E": ["Deutschland", "Curaçao", "Elfenbeinküste", "Ecuador"],
    "Gruppe F": ["Niederlande", "Japan", "Schweden", "Tunesien"],
    "Gruppe G": ["Belgien", "Ägypten", "IR Iran", "Neuseeland"],
    "Gruppe H": ["Spanien", "Kap Verde", "Saudi-Arabien", "Uruguay"],
    "Gruppe I": ["Frankreich", "Senegal", "Irak", "Norwegen"],
    "Gruppe J": ["Argentinien", "Algerien", "Österreich", "Jordanien"],
    "Gruppe K": ["Portugal", "DR Kongo", "Usbekistan", "Kolumbien"],
    "Gruppe L": ["England", "Kroatien", "Ghana", "Panama"],
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

