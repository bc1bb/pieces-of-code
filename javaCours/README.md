# Les variables et les types de données

Exercice 1

Créer un tableau de dix chaînes de caractères puis remplir ce tableau avec des adresses e-mail. Calculer ensuite, à partir des informations présentes dans le tableau, la part de marché de chacun des fournisseurs.

Indice : dans une adresse e-mail, le nom du fournisseur est la partie située après le caractère @.

Exercice 2

Générer trois nombres aléatoires compris entre 0 et 1000, puis vérifier si vous avez deux nombres pairs suivis par un nombre impair. Si ce n’est pas le cas, recommencer jusqu’à ce que vous ayez la combinaison pair, pair, impair. Afficher ensuite le nombre d’essais nécessaires pour obtenir cette combinaison.

Indice : la classe Random propose un ensemble de méthodes permettant d’obtenir un nombre aléatoire. Concentrez-vous sur la méthode suivante en lisant la javadoc :

```java
public int nextInt(int bound)
```

Pour utiliser cette méthode, il est nécessaire d’avoir un objet de type Random :

```java
Random rd = new Random();
rd.nextInt(...);
```

Excercice 3

Générer un nombre aléatoire compris entre 0 et 1000. Demander ensuite à l’utilisateur de deviner le nombre choisi par l’ordinateur. Il doit saisir un nombre compris entre 0 et 1000 lui aussi. Comparer le nombre saisi avec celui choisi par l’ordinateur et afficher sur la console « c’est plus » ou « c’est moins » selon le cas. Recommencer jusqu’à ce que l’utilisateur trouve le bon nombre. Afficher alors le nombre d’essais nécessaires pour trouver la bonne réponse.

Indice : pour récupérer les caractères saisis au clavier, nous avons à notre disposition le flux System.in. Malheureusement, celui-ci ne propose que des fonctions rudimentaires pour la récupération des saisies de l’utilisateur (lecture caractère par caractère). Pour une utilisation plus confortable, il vaut mieux utiliser un objet de type Scanner. Nous aurons ainsi à notre disposition une série de fonctions permettant la récupération d’entiers, de décimaux, de chaînes de caractères... Ces fonctions sont nommées nextXxx où Xxx doit être remplacé par le type de données que l’on souhaite obtenir, par exemple la méthode nextInt pour un entier, nextLine pour une chaîne de caractères, etc.

```java
String chaine;
Scanner sc;
sc = new Scanner(System.in);
chaine = sc.nextLine();
```

Exercice 4

Ajouter au jeu de l’exercice 3 l’affichage du temps mis par l’utilisateur pour obtenir la bonne réponse.

Indice : intéressez-vous aux classes OffsetTime et Duration.

# Programmation Objet

Exercice 1

Créer une classe représentant un article d’un magasin de vente par correspondance. Un article est caractérisé par sa référence, sa désignation, son prix. Créer ensuite une méthode main permettant de tester le bon fonctionnement de la classe précédente.

Exercice 2

Ajouter les deux classes Livre et Dvd héritant de la classe Article.

Un livre possède un numéro ISBN, contient un certain nombre de pages et a été écrit par un auteur, un DVD a une certaine durée et a été produit par un réalisateur.

Ajouter les attributs nécessaires aux classes Livre et Dvd pour avoir le nom de l’auteur ou du réalisateur. Tester ensuite le fonctionnement de ces deux nouvelles classes.

Exercice 3

Modifier les classes Livre et Dvd pour avoir disponibles les informations suivantes concernant l’auteur ou le réalisateur :

- son nom
- son prénom
- sa date de naissance

Indice : les auteurs et les réalisateurs sont des personnes.

Exercice 4

Modifier le code précédent pour pouvoir obtenir rapidement la liste des articles concernant un auteur ou un réalisateur.