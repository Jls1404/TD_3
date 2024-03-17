# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:20:48 2024

@author: julco
"""
"""

"""        
import matplotlib.pyplot as plt
import glob
import json

def lire_json(chemin):
    with open(chemin, "r", encoding="UTF-8") as f:
        chaine = json.load(f)
    return chaine

# Initialise des listes vides pour les remplir par la suite afin d'y stocker des informations pour le graphique
cluster_lengths = []
centroids = []

# Parcourt le dossier pour lire les fichiers JSON
for chemin in glob.glob("../fichiers_clusters/cluster_pour_graphique/*"):
    nom_fichier = chemin.split("\\")[-1]
    print(nom_fichier)
    fichier = lire_json(chemin)

    # Permet de calculer la longueur des clusters et de les ajouter à une liste
    for cluster in fichier:
        cluster_length = len(fichier[cluster]["Termes"])
        cluster_lengths.append(cluster_length)
        centroids.append(fichier[cluster]["Centroïde"])

# Création d'un graphique qui représente la longueur des différents clusters sous forme de cercles plus ou moins important
plt.figure(figsize=(20, 14))# gère la taille du graphique
for i, (length, centroid) in enumerate(zip(cluster_lengths, centroids)):
    plt.scatter(i, length, s = length * 10, alpha =  0.7, label = f"Cluster {i}")# personnalisation des cercles du graphique
    plt.annotate(centroid, (i, length), textcoords = "offset points", xytext = (0,6), ha = "center", fontsize = "8")# permet de personnaliser le titre des cercles 

# Personnalisation du graphique et enregsitrement de ce-dernier
plt.xlabel("Cluster Index")
plt.ylabel("Longueur des cluster")
plt.title("Longueur de cluster selon les centroides")
plt.grid(True)
plt.savefig("Graphique_cluster.png")
# plt.legend()
plt.show()
       


# créer un depot TD3-Cluster: y mettre le code, les graphiques, le rapport pdf
# ajouter comme collaborateur "These-SCAI2023"