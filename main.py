import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import youtube_dl

# Get the API token from the .env file
TOKEN = "MzkwOTc5OTkzMzE4MDY0MTQ4.GSNQEG.RTSUZa9hxEh-cl9p1JftBOU11q6nyR7cAHeTkE"

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
