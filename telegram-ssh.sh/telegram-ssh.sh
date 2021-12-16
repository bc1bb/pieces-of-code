#!/usr/bin/env bash
# Jus de Patate_ - Telegram Monitoring Bot (github:jusdepatate/telegram-monitoring-bot) - 2020
# Get a Telegram notification everytime someone SSH in your account
# requires grepcidr

fatal() {
  touch "$HOME"/.ssh/telegram_ssh_log
  echo "$(date) | $*"  > "$HOME"/.ssh/telegram_ssh_log
  exit 0
  # so we don't warn the hacker if there's one
}

BOT_KEY=""
# Your API KEY from BotFather

CHAT_ID=""
# Where to send notification

LOCAL_IP="10.0.0.0/8 172.16.0.0/12 192.168.0.0/16"
# Local IPs

TRUSTED_IP=""
# IPs that will do a notification by default but won't check any informations online

if [ -z "$BOT_KEY" ]; then
  fatal "No bot API key"
elif [ -z "$CHAT_ID" ]; then
  fatal "No Chat ID, I don't know where to send my message m8"
fi

if [ -z "$SSH_CLIENT" ]; then
  IP="$(echo "$SSH_CONNECTION" | awk '{ print $1}')"
else
  IP="$(echo "$SSH_CLIENT" | awk '{ print $1}')"
fi
# Get IP

send() {
  if [ -n "$1" ]; then
    if [ "$1" = "local" ]; then
      MESSAGE="Connection to $(whoami) from local ($IP) on $(tty) ($(hostname))"
    elif [ "$1" = "nossh" ]; then
      MESSAGE="Login to $(whoami) from local on $(tty) ($(hostname))"
    elif [ "$1" = "trusted" ]; then
      MESSAGE="Login to $(whoami) from a trusted IP ($IP) on $(tty) ($(hostname))"
    fi
  # nossh, local & trusted arguments (look above)
  # comment this part if you don't want notification from local login (w/o SSH) or login from trusted IP
  else
    INFOREQ="$(curl -s "http://ip-api.com/line/$IP?fields=status,message,continent,country,regionName,city,zip,isp,as,mobile,proxy,hosting,query")"
    STATUS="$(echo "$INFOREQ" | sed "1q;d")"

    if [ ! "$STATUS" = "succes" ]; then
      CONTINENT="$(echo "$INFOREQ" | sed "2q;d")"
      COUNTRY="$(echo "$INFOREQ" | sed "3q;d")"
      REGION="$(echo "$INFOREQ" | sed "4q;d")"
      CITY="$(echo "$INFOREQ" | sed "5q;d")"
      CITY_ZIP="$(echo "$INFOREQ" | sed "6q;d")"
      ISP="$(echo "$INFOREQ" | sed "7q;d")"
      AS="$(echo "$INFOREQ" | sed "8q;d" | sed 's/ .*//')"
      MOBILE="$(echo "$INFOREQ" | sed "9q;d")"
      PROXY="$(echo "$INFOREQ" | sed "10q;d")"
      HOSTING="$(echo "$INFOREQ" | sed "11q;d")"
      TTY="$SSH_TTY"

      if [ "$MOBILE" = "true" ]; then
        SPECIAL=" - Mobile ISP)"
      elif [ "$PROXY" = "true" ]; then
        SPECIAL=" - VPN/TOR/Proxy)"
      elif [ "$HOSTING" = "true" ]; then
        SPECIAL=" - Hosting company)"
      else
        SPECIAL=")"
      fi

      MESSAGE="Connection to $(whoami) on $TTY ($(hostname)) from $CITY, $REGION ($CITY_ZIP), $COUNTRY ($CONTINENT) using IP $IP ($AS - $ISP$SPECIAL"
    else
      ERR_MESSAGE="$(echo "$INFOREQ" | sed "2q;d")"
      fatal "ip-api.com returned an error $ERR_MESSAGE"
    # here we get as much information from IP as possible using ip-api.com (ratelimit is at 45 reqs/minutes)
    fi
  fi

  REQUEST="$(curl -X POST -s -H 'Content-Type: application/json' --data "$(cat <<EOF
  {
    "chat_id": "$CHAT_ID",
    "text": "$MESSAGE"
  }
EOF
  )" "https://api.telegram.org/bot$BOT_KEY/sendMessage" || fatal "Unable to send request")"

  # shellcheck disable=SC2143
  # I love too much if [ $(echo | grep)] to use anything else :p
  if [ "$(echo "$REQUEST" | grep '"ok":false')" ]; then
        fatal "$REQUEST"
        # this means that we were not able to send a notification
  fi
}


if [ -z "$IP" ]; then
  # if no ssh
  send nossh
elif [ "$(echo "$IP" | grepcidr "$LOCAL_IP")" ]; then
  # if ssh from local
  send local
elif [ "$(echo "$IP" | grepcidr "$TRUSTED_IP")" ]; then
  # if ssh from trusted IP
  send trusted
else
  # if ssh from external IP
  send
fi