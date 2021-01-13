#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2020, Discord Bot Template"
__credits__     = ["Alex Ronquillo: https://realpython.com/how-to-make-a-discord-bot-python/"]

__license__     = "BSD 3-Clause License"
__version__     = "0.1"
__contact__     = {
                    "Twitch": "https://twitch.tv/k0nze",
                    "Youtube": "https://youtube.com/k0nze",
                    "Twitter": "https://twitter.com/k0nze_gg",
                    "Instagram": "https://instagram.com/k0nze.gg",
                    "Discord": "https://discord.k0nze.gg",
                }

import os
import json
import discord
import random

from os.path import join, dirname
from dotenv import load_dotenv
from discord.utils import get
from discord.ext import commands

# load .env file
dir_path = os.path.dirname(os.path.realpath(__file__))

dotenv_path = join(dir_path, '.env')
load_dotenv(dotenv_path)

DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    """ Runs once the bot has established a connection with Discord """

    print(f'{bot.user.name} version has connected to Discord')

    # check if bot has connected to guilds
    if len(bot.guilds) > 0:
        print('connected to the following guilds:')

        for guild in bot.guilds:
            print(f'* {guild.name}#{guild.id}')


@bot.command(name="gif")
async def on_gif(ctx):
    """
    Runs when the !gif command was issued in a Discord text channel and posts a 
    random GIF from the JSON file
    """
    guild = ctx.guild
    channel = ctx.channel
    author = ctx.author
    command = ctx.message.content

    # log event on command line
    print(f'* "{author.name}" issued "{command}" in "{channel}" of "{guild}"')

    # post random GIF from the JSON file
    await channel.send(get_random_gif_link())


def get_random_gif_link():
    """ Returns a random gif link from the JSON file """
    with open(JSON_FILE) as json_file:
        # open JSON file
        data = json.load(json_file)
        # get all gifs
        gifs = data['gifs']
        # randomly select a gif
        gif = random.choice(gifs)

        # return the link of the gif to the caller
        return gif['link']


if __name__ == "__main__":
    # launch bot
    bot.run(DISCORD_TOKEN)
