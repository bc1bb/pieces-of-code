#!/usr/bin/env bash
# freereseau.sh - JdP_
version="1.4"

if [ -w /tmp/ ]; then
  curl -s https://www.free-reseau.fr/free-reseau-rss.xml > /tmp/freerezo.xml
else
  echo "freereseau.sh ne peut pas écrire dans /tmp/, s'il vous plait changez les permissions"
  exit 1
fi

if [ "$(which tput 2>/dev/null)" ]; then
  BOLD=$(tput bold)
  NORMAL=$(tput sgr0)
else
  BOLD="\e[1m"
  NORMAL="\e[0m"
fi

if [ ! "$(which curl 2>/dev/null)" ]; then
  echo "Install curl please"
  exit 1
fi

wttr() {
  CITY=$(curl -s ipinfo.io/city)
  REGION=$(curl -s ipinfo.io/region)

  if [ "$CITY" = "" ]; then
    CITY=$REGION
  fi

  curl -s "wttr.in/$CITY?Q0&lang=fr"
}

echo ""
# saut de ligne au début

if [ ! "$@" ]; then
# si il n'y a pas d'arguments
  # récuperation du nom du/des DSLAMs HS depuis le fichier XML precedemment téléchargé
  ee="$(grep "description" /tmp/freerezo.xml | awk 'NR==2' | sed -e 's/<description>/ /g' | sed -e 's/<\/description>/ /g')"

  # nombre de DSLAM qui ne répondent pas
  nmbr="$(echo $ee | awk '{print $1;}')"
  # -1 parce qu'il a l'air de toujours trouver 1 DSLAM HS de trop
  nmbr="$(( $nmbr - 1 ))"

  wttr
  echo ""

  echo "Liste des DSLAMs Free ne répondant pas : ${BOLD}$(echo $ee | cut -d" "  -f10-)${NORMAL} ($nmbr)${NORMAL}."

  rm /tmp/freerezo.xml
  # ne pas oublier de supprimer le fichier apres l'avoir manipulé

elif [[ $1 = "--help" || $1 = "-h" ]]; then
# argument help, qui indique toutes les fonctionnalitées
  echo "freereseau.sh - $version"
  echo "Un script qui permet de voir quel DSLAMs Free ne répondent pas"
  echo "En cas d'argument présent, le script va vous dire si ce DSLAM est détecté comme HS"
  echo "En cas d'argument absent, le script va vous dire tous les DSLAM détectés comme HS"

else
# en cas d'argument présent mais qui n'est pas reconnaissable par le script
  if [[ "$(grep $1 /tmp/freerezo.xml)" ]]; then
    echo "${BOLD}Ce DSLAM ne répond pas.${NORMAL}"
  else
    echo "${BOLD}Ce DSLAM répond ou n'existe pas.${NORMAL}"
  fi

fi

echo ""
# saut de ligne a la fin
