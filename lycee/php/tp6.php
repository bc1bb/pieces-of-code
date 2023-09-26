<html>
  <head>
    <title>Machine à calculer</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h2>Calculatrice</h2>
    <form method="get">
      <input type="text" name="op">
      <input type="submit" name="validation" value="Calculer">
    </form><br>
    <?php
    if(isset($_GET["op"]) && isset($_GET["validation"])) { 
      $input = str_split($_GET["op"]);
      $n1 = "";
      $op = "";
      $n2 = "";
      $res = 0;

      if(sizeof($input) < 3) {
        $res="Erreur";
      } else {
        foreach($input as $i) {
          if($op == "") {
            if(is_numeric($i) || $i == ".") {
              $n1 = $n1.$i;
            } elseif ($i == ",") {
              $n1 = $n1.".";
            } else {
              $op = $i;
            }
          } else {
            if(is_numeric($i) || $i == ".") {
              $n2 = $n2.$i;
            } elseif ($i == ",") {
              $n2 = $n2.".";
            } else {
              $res = "Erreur";
              break;
            }
          }
        }

        if($op == "+") {
          $res=$n1+$n2;
        } elseif($op == "-") {
          $res=$n1-$n2;
        } elseif($op == "*") {
          $res=$n1*$n2;
        } elseif($op == "/") {
          $res=$n1/$n2;
        } else {
          $res="Erreur";
        }
      }

      echo "Le résultat est ".round($res, 2);
    }
    ?>
  </body>
</html>