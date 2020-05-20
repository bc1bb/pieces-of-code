fatal() {
        echo "$@" >&2
        exit 1
}

getLastSource() {

        if [ ! "$(which jq)" ]; then
                fatal "getLastSource: Please install jq"
        fi
        if [ -z "$1" ] || [ -z "$2" ]; then
                fatal "getLastSource: Missing one argument (should be in the form getLastSource USER REPO)"
        fi

        user=$1
        repo=$2

        API="$(curl -s "https://api.github.com/repos/$user/$repo/releases/latest" || fatal "getLastSource: cannot connect to https://api.github.com/repos/$user/$repo/releases/latest")"
        LINK="$(echo $API | jq ".zipball_url" | tr -d \")"

        echo "$LINK"
}

#<example>
getLastSource jusdepatate amtenael-linux
getLastSource ish-app ish
# direct output

x="$(getLastSource jusdepatate amtenael-linux)"
echo "$x"
#wget "$x" -O "amtenael-linux.zip"
# put output in variable and use it
#</example>