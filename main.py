import nextcord
from nextcord.ext.commands import Bot

import logging
import os

intents = nextcord.Intents.all()
bot = Bot(command_prefix=".", intents=intents)

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.CRITICAL)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    logging.info("Ready to use!")


@bot.event
async def on_connect():
    bot.add_all_application_commands()
    await bot.sync_all_application_commands()
    logging.info("Connecting to Discord...")


async def loadAllExtensions():
    for folder in os.listdir("./cogs"):
        for filename in os.listdir(f"./cogs/{folder}"):
            if (filename.endswith(".py")):
                bot.load_extension(f"cogs.{folder}.{filename[:-3]}")

# Set up cogs
if __name__ == "__main__":
    await loadAllExtensions()
    bot.start("MTAyNzI1NTE5OTE1ODUyMTk0OA.GFehQ6.vfWz8by8hrcI8AGG0FWW5zheDrcFD9HaVb46_Q")
