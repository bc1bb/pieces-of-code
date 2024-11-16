<html>
  <head>
    <title>Premier pas en PHP</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h2>Variables et affichage d'un texte différent suivant la variable</h2>
    <p>
    <?php
      $moy=0;
      for($i=1; $i<=100; $i++) {
        $j=rand(0, 10);
        $moy=($moy+$j)/2;  
      }
      echo "La moyenne des 100 nombres est: ".round($moy, 2);  
      ?>
    </p>
  </body>
</html>