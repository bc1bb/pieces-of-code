#!/usr/bin/env bash
# very tiny and basic shell script to check if you are shadow banned by twitter
# Jus de Patate - 2020
fatal() {
        echo "$@" >&2
        exit 1
}

if [ ! "$(which jq)" ]; then
  fatal "Please install jq"
fi

if [ "$(which curl)" ]; then
  REQ="curl -s"
elif [ "$(which wget)" ]; then
  REQ="wget -qO-"
else
  fatal "Please install wget or cURL"
fi

if [ -z "$1" ]; then
  fatal "Missing one argument (should be in the form shadowban @user)"
fi

screenName="$1"

API="$($REQ "https://shadowban.eu/.api/$screenName" || fatal "Couldn't connect to https://shadowban.eu/.api/$screenName")"
isBanned="$(echo "$API" | jq ".tests.ghost.ban")"

if [ "$isBanned" == "true" ]; then
  echo "$screenName is shadow banned"
else
  echo "$screenName isn't shadow banned"
fi
