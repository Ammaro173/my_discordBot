# MAKE A DISCORD BOT
import discord
import random
import datetime
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = discord.Client()

# create client and login to server
@client.event
async def on_ready():
    print("Bot {0.user} is ready!".format(client))


# client event for messages handling
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    userMessage = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {userMessage} {channel}")

    # to make sure the bot doesn't reply to itself
    if message.author == client.user:
        return

    # or
    # if userMessage.lower() == "hello":
    #     await message.channel.sendf(f"Hello!{username}")
    #     return

    ## for a specific channel
    # if message.channel.name == "general":
    #     await message.channel.send(f"{username} said: {userMessage}")
    #     return

    # if the message is "!hello"
    if message.content.startswith("!hello"):
        # send a message to the channel the message was sent in
        await message.channel.send(f"Hello! {username}")
        return

    # if the message is "!roll"
    if message.content.startswith("!roll"):
        # send a message to the channel the message was sent in
        await message.channel.send(random.randint(1, 6))
        return

    # if the message is "!ping"
    if message.content.startswith("!ping"):
        # send a message to the channel the message was sent in
        await message.channel.send("Pong!")
        return

    # if the message is "!help"
    if message.content.startswith("!help"):
        # send a message to the channel the message was sent in
        await message.channel.send(
            """
        !info -> get info about the bot
        !ping -> ping
        !hello -> hello
        !roll -> roll a dice
        !flip -> flips a coin
        !exit -> gracefully exits the bot
        !choose -> rock, paper, scissors
        !time -> get the current time
        """
        )
        return

    # if the message is "!flip"
    if message.content.startswith("!flip"):
        # send a message to the channel the message was sent in
        await message.channel.send(random.choice(["heads", "tails"]))
        return

    # if the message is "!choose"
    if message.content.startswith("!choose"):
        # send a message to the channel the message was sent in
        await message.channel.send(random.choice(["rock", "paper", "scissors"]))
        return

    # if the message is "!exit"
    if message.content.startswith("!exit"):
        # send a message to the channel the message was sent in
        await message.channel.send("Goodbye!")
        # logout the bot
        await client.logout()
        return

    # if the message is "!info"
    if message.content.startswith("!info"):
        # send a message to the channel the message was sent in
        await message.channel.send("This is a bot made by @Ammaro")
        return

    # if the message is "!time"
    if message.content.startswith("!time"):
        # send a message to the channel the message was sent in
        await message.channel.send(str(datetime.datetime.now()))
        return


# def create_bot():
#     bot = commands.Bot(command_prefix="!")
#     return bot


client.run(TOKEN)
