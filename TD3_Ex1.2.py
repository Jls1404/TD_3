# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:40:14 2024

@author: Etudiants-d220
"""

import json
import glob
import pandas as pd


## permet de lire un fichier au format json
def lire_json(chemin):
    with open(chemin, "r", encoding = "utf-8") as f:
        fichier = json.load(f)
    return fichier

## permet de lire un fichier et de le retourner sous forme de chaine de carcatères
def lire_fichier(chemin):
    with open(chemin, "r", encoding = "utf-8") as f:
        chaine = f.read()
    return chaine

## permet de lire un fichier csv avec la librairie pandas
def lire_csv(chemin):
    fichier = pd.read_csv(chemin, sep = " ", quotechar = "\n", engine = "python", on_bad_lines = "skip")
    return fichier

## fonction reprise du programme de cluster et permet de récupérer le nom du fichier à partir du chemin de ce fichier        
def nomfichier(chemin):
    nomfich = chemin.split("\\")[-1]
    nomfich = nomfich.split(".")
    nomfich = ("_").join([nomfich[0], nomfich[1]])
    return nomfich

## programme principal
for chemin in glob.glob("../DATA/*/*/*.bio"):
    entité_json = set()# initialisation d'un set pour le stockage des données
    nom_fichier = nomfichier(chemin)# utilisation de la fonction nomfichier
    # print(nom_fichier)
    df = lire_csv(chemin)
    df.columns = ["Entité", "BIO", "?"]# donne un nom au différentes colonnes afin de pouvoir les manipuler par la suite
    # print(df.head(50))
    df_propre = df[df["BIO"].isin(["I-ORG", "B-ORG", "I-MISC", "B-MISC", "I-LOC", "B-LOC", "I-PER", "B-PER"])]# stocke uniquement les entités pertinentes 
    # print(df_propre.head(50))
    for entité in df["Entité"]:# parcourt la colonne Entité...
        entité_json.add(entité)# ...et récupère chaque entité pour les ajouter au set entités_json initialisé au début du programme
        
    ## stocke les entités récupérées au format json pour les réutiliser par la suite
    with open(f"entité_{nom_fichier}.json", "w", encoding="utf-8") as w:
        w.write(json.dumps(list(entité_json), indent = 2, ensure_ascii = False))
        
        
            
            
            
   
 
    
    