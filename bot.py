#!/bin/python
import sys
import discord
import logging

from discord.ext import commands
from command import MaestroCommand

import config

logging.basicConfig(level=logging.DEBUG,
                    format=config.logging_format)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(config.logging_format))
logger.addHandler(handler)

bot = commands.Bot(command_prefix=config.command_prefix)
bot.add_command(MaestroCommand)

@bot.event
async def on_ready():
    logging.info(f'{bot.user.name} has connected to Discord!')

def main():
    try:
        bot.run(config.token)
    except discord.errors.LoginFailure as e:
        logging.error('LoginFailure:', e)
        sys.exit(1)
    except Exception as e:
        logging.error('Error:', e)
        sys.exit(1)

if __name__ == "__main__":
    main()
