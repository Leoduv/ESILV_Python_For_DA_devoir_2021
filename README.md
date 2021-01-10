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
  - un [extrait du dataset](api_test.csv) permettant d'essayer l'API (api_test.csv)
  - un [model RandomForest entrainé](random_forest.sav) utilisé par l'API
  - un [notebook](ProjetPython.ipynb) contenant l'exploration des données, feature engineering et l'entrainement des modèles de machine learning
  - le [script python d'API](app.py) à éxécuter pour tester l'API
  - un notebook contenant le code permettant de [tester l'API](api_test.ipynb)
  - les [performances des modèles](Resultats_Selection1.csv) issus de nos [deux](Resultats_Selection2.csv) datasets d'entrainement

## Modèle utilisé pour l'API

Nous avons décidé d'utiliser un RandomForest car c'est celui qui nous a permis d'obtenir les meilleurs résultats.
Il a été entrainé avec un dataset contenant ces colonnes :

|Number|Features|
| :-: | :- |
|30|CC1|
|31|CC2|
|32|CC3|
|33|CC4|
|34|CC5|
|3|Page_talking_about|
|37|Post_share_count|
|4|Page_category|
|35|Base_time|
|40à46|Post_published_day_num|
|47à53|Base_DateTime_day_num|
|54|Target_variable|

Et dont les 1% des valeurs les plus grandes ont été coupé, car elles étaient tellement plus élévés que les valeurs moyenne que les résulats étaient faussés.

# Résultats

En terme de précision et de viabilité d’industrialisation, nos résultats sont loin d’être excellents, nos meilleurs modèles font toujours beaucoup d’erreurs quand on sait que le nombre de commentaires du 3ème quartile est de 3, et que 65% des lignes avaient 0 commentaires. Mais nous avons vu une nette amélioration quand nous avons ignoré les lignes avec un nombre de commentaires > 100 (1.7 % des données). Nous sommes passés d’une erreur moyenne absolue de 20 à 7. 

Pour nous cela témoigne de l’impact de la distribution très peu homogène des données. Ce qui rendait d’ailleurs certaines visualisations comme la distribution de l’erreur impossible à cause des écarts. 

Mais le problème initial était de savoir s’il est possible d’estimer la quantité de commentaire à partir des caractéristiques d’une publication Facebook. 

Et pour nous, nos résultats montrent que c’est un objectif qui peut être atteignable avec surement plus de feature engineering, et peut-être du fine-tuning de models avec une cross-validation peut-être, que nous n’avons pas pu réaliser par manque de temps et ressources de calculs. 

## Pistes d'améliorations / réflexion 

Au vu de la distribution des données dans le dataset, nous nous sommes posés la question de comment contourner le problème de la surreprésentation des posts avec 0 commentaires. 

Une solution potentiel que nous n’avons pas pu tester serait de faire 2 modèles au lieu d’un seul : 
un premier modèle de classification dont le rôle serait de prédire si un post va recevoir des commentaires ou s’il y aura 0 commentaires.
puis, un autre modèle de régression, qui prédira le nombre de commentaire uniquement sur les posts étant identifiés comme “pouvant avoir des commentaires”. 
C’est une solution que nous avons vu fonctionner dans différents concours Kaggle !

Nous avons vu que l’auteur était plutôt parti sur la voie des réseaux de neurones, mais dans tous les cas nous avons vu le potentiel de ce jeu de données. 
Et peut-être un jour verrons-nous une fonctionnalité d’estimation automatique du nombre de likes ou de commentaires au moment de l’écriture d’un post sur FB ? 