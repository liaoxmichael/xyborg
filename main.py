"""
This is a Discord bot module.
"""

import os
import time
import random
import re
import csv
import d20
import discord
from oraseye import Asuka
from discord.ext import commands
from dotenv import load_dotenv
from gradio_client import Client

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GUILD = '258351915551817729'  # unknown?
ANNOUNCE_CHANNEL0 = '316340414732959746'  # unknown?
ANNOUNCE_CHANNEL1 = '725118344767995968'  # announcements (roll models)

# Define the intents
intents = discord.Intents.default()
intents.message_content = True  # Make sure you enable the required intents

# Define the activity
activity = discord.Activity(
    name='paint dry', type=discord.ActivityType.watching)

# Create the bot instance with the activity and intents
client = commands.Bot(command_prefix='xy!', activity=activity, intents=intents)


@client.event
async def on_ready():
    await client.add_cog(Asuka(client, int(ANNOUNCE_CHANNEL0), int(ANNOUNCE_CHANNEL1)))
    await client.load_extension("dnd")
    await client.load_extension("fun")
    
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    
    if client.user.mentioned_in(message):
        user_input = message.content.replace(f"<@!{client.user.id}>", "").strip()
        print(f"User input: {user_input}")
        
        async with message.channel.typing():
            try:
                print("Sending request to Hugging Face Space...")
                gradio_client = Client("liaoxmichael/xyborg")
                reply = gradio_client.predict(
		            user_input=user_input,
		            api_name="/predict"
                )
                print(f"Model reply: {reply}")
            except Exception as e:
                reply = f"Error: {str(e)}"
    
        return await message.reply(reply, mention_author=False)
    
    if "xyborg" in message.content.casefold():
        if "play despacito" in message.content.casefold():
            await message.reply("https://www.youtube.com/watch?v=W3GrSMYbkBE you're welcome")
        if "laugh for me" in message.content.casefold():
            await message.reply("ha. ha. ha.")

    if "vore" in message.content.casefold() or "xycest" in message.content.casefold() or "daxy" in message.content.casefold():
        await message.add_reaction(u"\U0001F61F")  # worried
    if "loss" in message.content.casefold():
        await message.add_reaction(u"\u261D")  # pointing up
        await message.add_reaction(u"\U0001F64C")  # hands raised
        await message.add_reaction(u"\u270C")  # v
        await message.add_reaction(u"\U0001F919")  # call me

    if ("69" in message.content) and not re.search(r'\<[^>]*\>', message.content):
        await message.add_reaction(u"\U0001F629")  # weary
    if ("420" in message.content) and not re.search(r'\<[^>]*\>', message.content):
        await message.add_reaction(u"\U0001F343")  # leaf falling
        await message.add_reaction(u"\U0001F525")  # fire
    if ("413" in message.content) and not re.search(r'\<[^>]*\>', message.content):
        await message.add_reaction(u"\U0001F631")  # scream
        zodiac = random.randint(1, 13)
        emojis = [
            u"\u2648", u"\u2649", u"\u264A", u"\u264B", u"\u264C", u"\u264D", u"\u264E",
            u"\u264F", u"\u2650", u"\u2651", u"\u2652", u"\u2653", u"\u26CE"
        ]
        await message.add_reaction(emojis[zodiac - 1])
    if "like this post" in message.content.casefold():
        await message.add_reaction(u"\U0001F44D")  # thumbs up
    if "good joke" in message.content.casefold():
        await message.add_reaction(u"\U0001F499")  # blue heart
    if "thanks xyborg" in message.content.casefold():
        await message.add_reaction(u"\U0001F499")  # blue heart
    if "bad joke" in message.content.casefold():
        await message.add_reaction(u"\U0001F614")  # pensive
    if "poll:" in message.content.casefold():
        await message.add_reaction(u"\U0001F44D")  # thumbs up
        await message.add_reaction(u"\U0001F44E")  # thumbs down
    if "what's the scoop" in message.content.casefold():
        await message.reply("PEPIS! *crashes into a car*")
    if "trance" in message.content.casefold() or "trans" in message.content.casefold():
        await message.add_reaction(u"\U0001F3F3\U0000FE0F\U0000200D\U000026A7\U0000FE0F")  # trans flag
    if "final pam" in message.content.casefold():
        with open('data/final_pam.txt', 'r') as file:
            await message.reply(file.read())

    await client.process_commands(message)


@client.command()
async def ping(ctx):
    # simple command so that when you use ping command the bot will respond with "pong!"
    await ctx.send(f"pong! 🏓 \nlatency: **{round(client.latency * 1000)}ms**")

# @client.command()
# 	async def kick(ctx, member : discord.Member):
# 	try:
# 		await member.kick(reason=None)
# 		await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
# 	except:
# 		await ctx.send("bot does not have the kick members permission!")

client.remove_command('help')  # before your own "help" command


@client.command()
async def help(ctx):
    with open('data/help.txt', 'r') as file:
        await ctx.send(file.read())


@client.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)


client.run(os.environ.get("TOKEN"))
