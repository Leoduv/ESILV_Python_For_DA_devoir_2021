# Python For Data Analysis : Facebook Comment Volume

## Contexte

Le but de ce projet d'explorer un dataset et d'essayer de répondre à un problème à l'aide de machine learning en utilisant les différentes possibilités offertes en Python. 

## Le Dataset

Le dataset est composé d'informations sur un post Facebook et le nombre de commentaires qu'il a recu pendan tplusieurs plages horaires. Il contient 54 variables dont:
  - 4 variables sur la page: décrivant l'intérêt de l’utilisateur pour cette page
  - 25 variables dérivées: ce sont des calculs de minimum, maximum,
moyenne, médiane et écart type des variables essentielles
  - 5 variables "essentielles": décrivent le pattern des commentaires sur un
poste ou sur la page
  - 5 autres variables: décrivant le post ( sa taille, son nombre de partage…)
  - 14 Variables du jour de la semaine: décrivant le jour où la publication est
faite et celle de la publication à prévoir

Et la variable cible qui correspond donc au nombre de
commentaires que le post a reçu.

# Objectif : prédiction du nombre de commentaires 

## Contenu du projet

Le projet se compose de :
  - dataset complet zippé
  - un extrait du dataset pour pouvoir tester l'API (api_test.csv)
  - un model RandomForest entrainé utilisé par l'API
  - un notebook contenant l'exploration des données et l'entrainement des modèles de machine learning
  - l'app.py, à éxécuter pour tester l'API
  - un notebook contenant le code permettant de tester l'API

## Modèle utilisé pour l'API

Nous avons décidé d'utiliser un RandomForest car c'est celui qui nous a permis d'obtenir les meilleurs résultats.
Il a été entrainé avec un dataset contenant ces colonnes :

**AJOUTER LE NOM DES COLONNES ICI**

Et dont les 1% des valeurs les plus grandes ont été coupé, car elles étaient tellement plus élévés que les valeurs moyenne que les résulats étaient faussés.

# Résultats

BLABLABLA
