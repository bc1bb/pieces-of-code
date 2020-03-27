fatal() {
        echo "$@"
        exit 1
}

getLastSource() {

        if [ ! "$(which jq)" ]; then
                fatal "Please install jq"
        fi
        if [ -z "$1" ] || [ -z "$2" ]; then
                fatal "Missing one argument (should be in the form getLastSource USER REPO)"
        fi

        user=$1
        repo=$2

        API="$(curl -s "https://api.github.com/repos/$user/$repo/releases/latest" || fatal "cannot connect to https://api.github.com/repos/$user/$repo/releases/latest")"
        LINK="$(echo $API | jq ".zipball_url" | tr -d \")"
}

#<example
getLastSource jusdepatate amtenael-linux
echo "$LINK"
getLastSource tbodt ish
echo "$LINK"
#</example>