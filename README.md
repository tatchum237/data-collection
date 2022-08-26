# programme sur les techniques de collection de données.

## Description

Salut les amis, je viens avec un programme sur un ensemble de techinque utilisée pour collecter les données. Nous avons exploré le scrapping, la collecte depuis des API, des fichiers (html, csv, json, sql...)



## Comment lancer le programme ?

He bien! vous devez ouvrir le dossier **MON-PROGRAMME** avec **VISUAL STUDIO CODE** ou **PYcharm** se trouvant dans le dossier **data_collection**
une fois vous êtes dans ce dossier, vous trouverez deux autres dossiers:
  - **DATABASES** qui contient les fichiers que nous allons explorer et la base de données **db**
  - **MODULE5** qui contient un dossier **libraries** avec des algorithmes que nous allons exploités dans d'autres fichiers
  

Pour lancer, vous pouvez lancer uniquement le fichier **main.py** qui appelle tous les autres fichiers ou vous pouvez lancer les differents fichiers independamment afin de mieux apprehender les diiferentes fonctions.

une fois le projet démaré, nous allons parler des fonctionnalités.


## Les fonctionnalités

1. Une class avec plusieurs fonctions qui scrappe les données du fichier **html** se trouvant dans **DATABASES**. le fichier **html_.py**  illustre cette hypothése.
2. Une class avec plusieurs fonction qui scrappe les données du site de la [bceao](https://www.bceao.int/fr/cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts). Le fichier **bceao.py** illustre cette hypothése.
3. Une concatenation des differentes sources de données. Le fichier **concatenation.py** illustre cette hypothése.
4. La collecte de pays (nom et drapeau) depuis une [api free](https://restcountries.com/v2/all) et sauvegarde dans une liste. Le fichier **country.py** illustre cette hypothése.
5. Une base de données **data.db** qui va stocker toute nos données collectées. Nous avons modelisé comme suite:
- un pays a une devise. Le fichier **prepasCountry.py** illustre cette hypothése.
- une personne reste dans un pays. Le fichier **prepasPersonne.py** illustre cette hypothése.
- En suite les tables ont été crée et les données sauvegardées. Le fichier **sql.py** illustre cette hypothése.

6. Enfin une fonction qui va éxecuter toutes les autes class et fonction. Le fichier **main.py** illustre cette hypothése.


# Votre machine doit sur tout être connécté sur internet et installer les modules