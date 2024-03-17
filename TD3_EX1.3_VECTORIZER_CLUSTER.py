#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:16:20 2022

@author: antonomaz
"""


import numpy as np
from sklearn.cluster import AffinityPropagation
# from sklearn.metrics import DistanceMetric 
from sklearn.feature_extraction.text import CountVectorizer
import sklearn
import json
import glob
import re
from collections import OrderedDict

## création d'une fonction pour lire un fichier json à partir d'un chemin
def lire_fichier (chemin):
    with open(chemin) as json_data: 
        texte = json.load(json_data)
    return texte

## création d'une fonction pour attribué un nom de fichier au fichier à partir de son chemin
def nomfichier(chemin):
    nomfich = chemin.split("/")[-1]
    # nomfich = nomfich.split(".")
    # nomfich = ("_").join([nomfich[0], nomfich[1]])
    return nomfich
    
 

chemin_entree = "../Json/AIMARD_les-trappeurs_TesseractFra-PNG.txt_SEM_WiNER.ann_SEM.json-concat.json"



## 
# for subcorpus in glob.glob("../Json/*"):# parcourt chaque fichier du dossier du chemin path_copora
#    print("SUBCORPUS***",subcorpus)
liste_nom_fichier = []# initialisation d'une liste qui permettra d'y ajouter des éléments et de les stocker au cours du programme
for path in glob.glob(chemin_entree):# parcourt chaque fichier du dossier du chemin 
#        print("PATH*****",path)
    nom_fichier = nomfichier(path)# avec la fonction nomfichier créée avant, on ressort le nom du fichier à partir du chemin
#        print(nom_fichier)
    liste = lire_fichier(path)# on créé une variable liste à laquelle on attribue les différents fichiers du chemin, en les lisant via la fonction lire_fichier, sous forme de chaine de carcatères
    # set_initial = set(liste)
    
######## FREQUENCE ########
    
    dic_mots = {}# initialisation d'un dictionnaire (structure qui comprend une assocation clé et différentes valeurs; un dictionnaire peut avoir plusieurs clés)
    i = 0# initilisation d'un compteur que l'on incrémentera de 1 à la fin de la boucle ci-dessus

    ## permet de connaitre les fréquences de chaque mot de la liste, sous forme de dictionnaire
    for mot in liste:# parcourt chaque élément (ici on explicite par le nom de la variable que ce sont des mots) de la liste au sein de laquelle on y a ajouté, au-dessus, les différents textes 
        mot = str(mot)
        if mot not in dic_mots:# ici une condition est mise en place, si les mots ne sont pas deja integrés au dictionnaire dic_mots
            dic_mots[mot] = 1# ..alors on associe la valeur 1 au dictionnaire avec comme clé le mot de la liste correpsondant
        else:# sinon, si le mot fait deja partie du dictionnaire...
            dic_mots[mot] += 1# ...on incrémente la valeur de la clé du mot par 1
    
    i += 1# à chaque fin de boucle on incrémente la variable i de 1
    print(dic_mots)
    new_d = OrderedDict(sorted(dic_mots.items(), key=lambda t: t[0]))
    # print(new_d)
    
    # freq = len(dic_mots.keys())# on utilise la fonction len() pour connaitre une longueur, ici on veut savoir le nombre de clés du dictionnaire dic_mots
    

    Set_00 = set(liste)# transforme la liste créée au début en set 
    print("set_00", Set_00)
    Liste_00 = list(Set_00)# transforme le Set_00 de la ligne du dessus en liste
    dic_output = {}# initialisation d'un dictionnaire
    liste_words = []# initialisation d'une liste
    matrice = []# initialisation d'une liste
    
    for l in Liste_00:
        # print(l)
        if len(l)!= 1:
            liste_words.append(l)
    

    try:# va tester le bloc ci-dessous jusqu'au bloc "except"
        words = np.asarray(liste_words)# np.asarray va transformer la "liste_words" en un tableau à laquelle on attribuera la variable "words"
        for w in words:# parcourt chaque ligne du tableau "words" créé à la ligne du dessus
            liste_vecteur = []# initialise une liste "liste_vecteur"
        
                
            for w2 in words:# parcourt chaque élément de la ligne du taleau
                    V = CountVectorizer(ngram_range=(2,3), analyzer='char')
                    X = V.fit_transform([w,w2]).toarray()
                    distance_tab1 = sklearn.metrics.pairwise.cosine_distances(X)            
                    liste_vecteur.append(distance_tab1[0][1])
                
            matrice.append(liste_vecteur)# ajoute à la liste"matrice" (créée plus huat) la "liste_vecteur" dans laquelle se trouve les distances cosinus 
        matrice_def = -1*np.array(matrice)
        print(matrice_def)
       
              
        affprop = AffinityPropagation(affinity="precomputed", damping= 0.6, random_state = None) 

        affprop.fit(matrice_def)
        for cluster_id in np.unique(affprop.labels_):
            exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
            cluster = np.unique(words[np.nonzero(affprop.labels_ == cluster_id)])
            cluster_str = ", ".join(cluster)
            cluster_list = cluster_str.split(", ")
                        
            Id = "ID" + str(i)
            for cle, dic in new_d.items(): 
                if cle == exemplar:
                    dic_output[Id] = {}
                    dic_output[Id]["Centroïde"] = exemplar
                    dic_output[Id]["Freq. centroide"] = dic
                    dic_output[Id]["Termes"] = cluster_list
            
            i=i+1
        #    print(dic_output)
        

    except:# si une errur est trouvée dans le bloc "try" alors plutot que d'arrêter le programme, on affichera...       
        print("**********Non OK***********", path)#...ce qui est écrit dans le "print" ci-contre 
        liste_nom_fichier.append(path)
        
        
        continue 



