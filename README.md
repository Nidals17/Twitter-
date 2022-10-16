# Twitter

programming projet APE

-------------------------------
## Plan

 -  *PRESENTATION*
 -  *CONDITION D'UTILISATION*
 -  *DEVELOPPEMENT*

-------------------------------
## Présentation

Dans le cadre du projet de python programming, nous avons travaillé sur un programme capable de scrapper les tweets et de lancer automatiquement une analyses textuelles (« Words Network », « Wordcloud », les n_grams ainsi que les « common words ») tout en nettoyant les tweets également
Pour ce faire nous avons utiliser le module tweepy de python qui permet de d’obtenir les tweets via un login qu’on obtient sur twitter developper, ensuite nous avons developper des fonctions qui nettoient les tweets obtenus en utlisant notamment la librairie « re ». Après le nettoyage nous appliquons quelques filtres pour obtenir les common word que nous affichons à l’aide de Matplotlib. Après, nous continuons notre exploitation avec les wordcloud et les words networks. Et pour finir nous avons developper à l’aide du module « tkinter » un interface où l’utilisateur tape un « hashtag » qui permet l’automatisation de tout le processus

-------------------------------

## CONDITIONS D'UTILISATION

Pour faire fonctionner le programme il faut tout d’abord créer un compte developpeur chez twitter, ce qui vous permettra d’obtenir un login que vous aller utiliser dans le fichier « twitterplot » en remplissant les champs vides (api_key,..). Ensuite il faut installer toutes les modules qui font fonctionner le programme si ce n’est pas déjà fait et c’est tout comme prérequis

-------------------------------
## DEVELOPPEMENT
Cette application résulte de la collaboration entre Koubikani Loubota Jacques Verlaine & Souk Nidal dans le cadre d'un projet en Architectures, modèles et language de données (Octobre 2022) en Master 2 Data Science (APE). Rédigée sur Jupyter 6.4.5, elle fait appel aux principaux packages et modules suivants :
 - tweepy
 - wordcloud
 - matplotplib.pyplot
 - pandas 
 - tkinter 
-------------------------------
