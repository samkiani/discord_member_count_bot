#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Konstantin (k0nze) Lübeck"
__copyright__   = "Copyright 2021, Discord Member Count Bot"
__credits__     = ["Alex Ronquillo: https://realpython.com/how-to-make-a-discord-bot-python/"]

__license__     = "BSD 3-Clause License"
__version__     = "0.1"
__contact__     = {
                    "Twitch": "https://twitch.tv/k0nze",
                    "Youtube": "https://youtube.com/k0nze",
                    "Patreon": "https://www.patreon.com/k0nze",
                    "Twitter": "https://twitter.com/k0nze_gg",
                    "TikTok": "https://www.tiktok.com/@k0nze.gg",
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

# get path to data.json file
JSON_FILE = str(os.path.dirname(os.path.realpath(__file__))) + '/data.json'

# enable discord gateway intents
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """ Runs once the bot has established a connection with Discord """
    print(f'{bot.user.name} has connected to Discord')

    # check if bot has connected to guilds
    if len(bot.guilds) > 0:
        print('connected to the following guilds:')

        # list guilds
        for guild in bot.guilds:
            # display guild name, id and member count
            print(f'* {guild.name}#{guild.id}, member count: {len(guild.members)}')
            # update the member count
            await update_member_count_channel_name(guild)


@bot.event
async def on_member_join(member):
    """ gets triggered when a new member joins a guild """
    print(f"* {member} joined {member.guild}")
    await update_member_count_channel_name(member.guild)


@bot.event
async def on_member_remove(member):
    """ gets triggered when a new member leaves or gets removed from a guild """
    print(f"* {member} left {member.guild}")
    await update_member_count_channel_name(member.guild)


async def update_member_count_channel_name(guild):
    """ updates the name of the member count channel """
    member_count_channel_id = get_guild_member_count_channel_id(guild)
    member_count_suffix = get_guild_member_count_suffix(guild)

    if member_count_channel_id != None and member_count_suffix != None:
        member_count_channel = discord.utils.get(guild.channels, id=member_count_channel_id)
        new_name = f"{get_guild_member_count(guild)} {member_count_suffix}"
        await member_count_channel.edit(name=new_name)

    else:
        print(f"* could not update member count channel for {guild}, id not found in {JSON_FILE}") 


def get_guild_member_count(guild):
    """ returns the member count of a guild """
    return len(guild.members)


def get_guild_member_count_channel_id(guild):
    """ returns the channel id for the channel that should display the member count """
    with open(JSON_FILE) as json_file:
        # open JSON file
        data = json.load(json_file)
        for data_guild in data['guilds']:
            if int(data_guild['id']) == guild.id:
                return data_guild['channel_id']

            return None


def get_guild_member_count_suffix(guild):
    """ returns the the suffix that should be displayed after the member count """
    with open(JSON_FILE) as json_file:
        # open JSON file
        data = json.load(json_file)
        for data_guild in data['guilds']:
            if int(data_guild['id']) == guild.id:
                return data_guild['suffix']

            return None


if __name__ == "__main__":
    # launch bot
    bot.run(DISCORD_TOKEN)