// very tiny and basic node script to check if you are shadow banned by twitter
// untested on windows, works on linux

const process = require("process")
const request = require("request")

const username = process.argv[2]
// arg 0 = path to node
// arg 1 = path to script
// arg 2 = first argument

const url = "https://shadowban.eu/.api/" + username
const options = {
    json: true,
    headers: {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }
}

if (username === undefined) {
    console.log("Missing username argument.")
} else {
    request(url, options, (error, res, body) => {
        if (error) {
            console.log(error)
        } else if (res.statusCode != 200) {
            console.log("statusCode: " + res.statusCode)
        } else {
            var banned = body.tests.ghost.ban

            if (banned) {
                console.log(username + " is shadow banned")
            } else {
                console.log(username + " isnt shadow banned")
            }
        }
    })
}