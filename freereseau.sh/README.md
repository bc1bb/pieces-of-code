# `freereseau.sh`
[this script used to be hosted here](https://github.com/jusdepatate/freereseau.sh) <br>
Regardez l'état du réseau de DSLAMs Free avec ce script Bash grace au flux RSS de [free-reseau.fr](https://www.free-reseau.fr/free-reseau-rss.xml) et a l'API de `wttr.in` pour obtenir la météo locale).
<br>Le script n'est surement pas parfait et j'accepte les PRs.

```
jusdepatate@jusdepatate:~$ bash freereseau.sh

    \  /       Partiellement nuageux
  _ /"".-.     6..9 °C
    \_(   ).   ↑ 17 km/h
    /(___(__)  10 km
               0.0 mm

Liste des DSLAMs Free ne répondant pas : org93-3 org93-4 mtt83-1 muy83-1 muy83-2 muy83-3 tra83-1 ciu43-1 (8).

jusdepatate@jusdepatate:~$ bash freereseau.sh muy83-1

Ce DSLAM ne répond pas.

```
