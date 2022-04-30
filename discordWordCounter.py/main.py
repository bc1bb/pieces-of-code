#!/usr/bin/env python
import matplotlib.pyplot as plt
import discord
import json


def get_credits(line):
    return open("credits").readlines()[line - 1].split("\n")[0]


async def chart():
    json_data = json.load(open("who.json", "r"))
    labels = []
    sizes = []

    for i in json_data:
        userid = int(i)
        user = client.get_user(userid)
        labels.append(user.name)
        sizes.append(json_data[i])

    plt.pie(sizes, labels=labels)
    plt.savefig("graph.png")


def edit_data(userid, nb):
    userid = str(userid)
    json_data = json.load(open("who.json", "r"))

    if userid in json_data.keys():
        json_data[userid] = json_data[userid] + nb
    else:
        json_data[userid] = nb

    json.dump(json_data, open("who.json", "w"))


triggerWord = get_credits(1)
botToken = get_credits(2)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if triggerWord in message.content:
        nb = message.content.count(triggerWord)
        edit_data(str(message.author.id), nb)
        await chart()
        await message.reply("Another one!", file=discord.File("graph.png"))


client.run(botToken)
