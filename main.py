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

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GUILD = '258351915551817729'
ANNOUNCE_CHANNEL0 = '316340414732959746'
ANNOUNCE_CHANNEL1 = '725118344767995968'

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
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "xyborg" in message.content.casefold() or client.user.mentioned_in(message):
        if "play despacito" in message.content.casefold():
            await message.channel.send("https://www.youtube.com/watch?v=W3GrSMYbkBE you're welcome")
        if "laugh for me" in message.content.casefold():
            await message.channel.send("ha. ha. ha.")

    if "vore" in message.content.casefold() or "xycest" in message.content.casefold() or "daxy" in message.content.casefold():
        await message.add_reaction(u"\U0001F61F")  # worried
    if "loss" in message.content.casefold():
        await message.add_reaction(u"\u261D")  # pointing up
        await message.add_reaction(u"\U0001F64C")  # hands raised
        await message.add_reaction(u"\u270C")  # v
        await message.add_reaction(u"\U0001F919")  # call me
    # if "crab" in message.content.casefold():
    #     await message.channel.send("did you mean :crab: :cl::ab: :crab:")
    # if "scorpion" in message.content.casefold():
    #     await message.channel.send("Lobster Identified,")

    if ("69" in message.content) and not re.search(r"<(?:a?:[^:]+:|@!?|#|@&)?(\d*69\d*)>", message.content):
        await message.add_reaction(u"\U0001F629")  # weary
    if ("420" in message.content) and not re.search(r"<(?:a?:[^:]+:|@!?|#|@&)?(\d*420\d*)>", message.content):
        await message.add_reaction(u"\U0001F343")  # leaf falling
        await message.add_reaction(u"\U0001F525")  # fire
    if ("413" in message.content) and not re.search(r"<(?:a?:[^:]+:|@!?|#|@&)?(\d*413\d*)>", message.content):
        await message.add_reaction(u"\U0001F631")  # scream
        zodiac = random.randint(1, 13)
        if zodiac == 1:
            await message.add_reaction(u"\u2648")  # aries
        elif zodiac == 2:
            await message.add_reaction(u"\u2649")  # taurus
        elif zodiac == 3:
            await message.add_reaction(u"\u264A")  # gemini
        elif zodiac == 4:
            await message.add_reaction(u"\u264B")  # cancer
        elif zodiac == 5:
            await message.add_reaction(u"\u264C")  # leo
        elif zodiac == 6:
            await message.add_reaction(u"\u264D")  # virgo
        elif zodiac == 7:
            await message.add_reaction(u"\u264E")  # libra
        elif zodiac == 8:
            await message.add_reaction(u"\u264F")  # scorpius
        elif zodiac == 9:
            await message.add_reaction(u"\u2650")  # sagittarius
        elif zodiac == 10:
            await message.add_reaction(u"\u2651")  # capricorn
        elif zodiac == 11:
            await message.add_reaction(u"\u2652")  # aquarius
        elif zodiac == 12:
            await message.add_reaction(u"\u2653")  # pisces
        elif zodiac == 13:
            await message.add_reaction(u"\u26CE")  # ophiuchus
    # if "bored" in message.content.casefold():
    #     await message.channel.send("cw nsfw language meme: ||https://imgur.com/MZrOSFl.png||")
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
        await message.channel.send("PEPIS! *crashes into a car*")
    if "trance" in message.content.casefold() or "trans" in message.content.casefold():
        await message.add_reaction(u"\U0001F3F3\U0000FE0F\U0000200D\U000026A7\U0000FE0F")  # trans flag?
        # await message.channel.send("trance rite's!")
    if "final pam" in message.content.casefold():
        with open('data/final_pam.txt', 'r') as file:
            await message.channel.send(file.read())
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


@client.command(aliases=["r"])
async def roll(ctx, *, arg):
    result = u"\U0001F3B2" + " "  # game die
    try:
        if (arg.find("adv") != -1):
            arg = arg.replace("adv", "")
            result += str(d20.roll(arg, advantage=1))
        elif (arg.find("dis") != -1):
            arg = arg.replace("dis", "")
            result += str(d20.roll(arg, advantage=-1))
        else:
            result += str(d20.roll(arg))
        await ctx.reply(result)
    except Exception as e:
        await ctx.send(f"Unknown roll formatting. Error: `{str(e)}`")


@client.command(aliases=["8ball"])
async def answer(ctx):
    answer = random.randint(1, 10)
    if answer == 1:
        await ctx.send("maybe so")
    elif answer == 2:
        await ctx.send("hmm... how about no")
    elif answer == 3:
        await ctx.send("... I GUESS")
    elif answer == 4:
        await ctx.send("maybe later, little man")
    elif answer == 5:
        await ctx.send("god, what kind of question is that? gross")
    elif answer == 6:
        await ctx.send("pepis")
    elif answer == 7:
        await ctx.send("fuck")
    elif answer == 8:
        await ctx.send("in time, kiddo")
    elif answer == 9:
        await ctx.send("According to all known laws of aviation,")
    elif answer == 10:
        await ctx.send("do i have to answer that")


@client.command()
async def joke(ctx):
    with open('data/jokes.csv', newline='') as jokefile:
        jokereader = csv.reader(jokefile)
        jokelist = []
        for row in jokereader:
            # if lines == 0:
            #     # print("Headers are " + ", ".join(row))
            # else:
            #     # print(row[0] + "\n" + row[1] + "\n" + row[2] + "\n\n")
            jokelist.append(row)
        # print(lines)

    jokelist = jokelist[1:]  # remove the header

    joke = random.randint(0, len(jokelist))
    if joke == len(jokelist):
        await ctx.send("Have you ever heard of the legend of the Greek hero Bouphades? He was a lesser-mentioned sailor who traveled alongside Jason and the Argonauts, and his tale (written by Hesiod) takes place after their many escapades.")
        time.sleep(5)
        await ctx.send("He's settled down in Corinth and had a family, but his son Enteron mysteriously disappears one day and so he has to set off and try to find him. Hera favors him as a hero, so she grants him a gift to keep him safe: sacred Macedonian nuts.")
        time.sleep(5)
        await ctx.send("She also warns him that if he does go on this quest, he is doomed to die. However, brave-hearted Bouphades refuses to let his son go missing, so he accepts his death as a sacrifice - he's lived a long life, after all, and young Enteron has yet to experience the wide world and the Achaean seas.")
        time.sleep(5)
        await ctx.send("So Hera returns to Mount Olympus cloaked in her husband's clouds, and Bouphades sets out with nothing but his staff (for he is old now, and needs a walking support) and Hera's gift. He travels for forty days and forty nights, living off the land and being invited to kind kings' halls in exchange for his retelling of the Argonauts' tales.")
        time.sleep(5)
        await ctx.send("Brave-hearted Bouphades searches all this while, having been gifted golden armor (crafted by Hephaestus' son) and a golden blade (named Yore) by the kings of Argos and Phthia respectively, and slays many a beast, despite his age. However, he finds no trace of his son, having wandered all over the Pelopponese and even abroad to some islands.")
        time.sleep(5)
        await ctx.send("After this arduous journey, he is despairing, nearly mourning his son and accepting poor Enteron's death. That night, he scrapes together a fire, eats the last of his food, and curls up in an abandoned bear's cave to weather the night before giving up and going home. And that night, he has a prophetic dream, sent to him by Hera in her love and pity for the brave man.")
        time.sleep(5)
        await ctx.send("In his dreams, she reveals to him that the bear that lived in this cave has swallowed Enteron whole. He has found him, but he must go deeper into the cave and slay the beast, cut open its stomach, and save his boy. She tells him of the monstruous bear that lives in this cave, earning the cave the name Mouth of Death, for all who enter are doomed to be consumed.")
        time.sleep(5)
        await ctx.send("So when brave-hearted Bouphades awakes, he grips Yore and suits up again in his golden armor and goes deeper into the Mouth. There he confronts the bear, a ghoulish creature. He asks it: \"What is your name, so I might slay you and send your eternal soul to Hades, and free my son young Enteron, whom by swallowing you have brought doom upon your head!\"")
        time.sleep(5)
        await ctx.send("The bear responds: \"I am named the same as the very ground upon which you stand, for anyone who enters is lost! I am the Mouth of Doom, and by entering my lair foolishly as you have, you have already forfeited your life!\" And with that, the Mouth charges at him, bloody death in its eyes, intent on devouring brave-hearted Bouphades.")
        time.sleep(5)
        await ctx.send("Brave-hearted Bouphades remembered his sacrifice and stood his ground, Yore's blade angled up as the beast hurled itself at him. As its sharp claws tore through his armor and dealt him a fatal blow, so too did his blade strike true and tear the beast's stomach wide open, spilling young Enteron onto the ground. The boy was able to clutch his father's hand as the strength drained from it and his life flew down to Hades.")
        time.sleep(5)
        await ctx.send("His father smiled his son through the pain, but said nothing more as his breath escaped him. In order to remember his father's bravery, young Enteron salvaged what he could from the bloody ordeal, promising to bring the corpse of the Mouth home so everyone in Corinth would know his bravery and remember his legacy. And Hera's gift managed to sustain the boy enough so that he could reach home, using his father's gifted blade to great effect and to gain undying glory. Though young Enteron was a boy when he disappeared, he returned home a man.")
        time.sleep(5)
        await ctx.send("So, in total, only four things exited the cave, famous forever in Corinthian history as historic artifacts and heroes. And they are as follows:")
        time.sleep(3)
        await ctx.send("Bouphades' nuts, Enteron, Yore, Mouth.")
        time.sleep(3)
        await ctx.send("Gottem.")
    else:
        curr_joke = jokelist[joke]
        await ctx.send("Okay, how about this:")
        time.sleep(1)
        await ctx.send(curr_joke[0])
        time.sleep(3)
        await ctx.send(curr_joke[1])
        if curr_joke[2] != "0":
            time.sleep(3)
            await ctx.send(f"`This joke was suggested by Discord user {curr_joke[2]}. You could be next!`")


def csv_to_list(file):
    with open(file, newline='') as file:
        reader = csv.reader(file)
        result = list(reader)[1:]  # skip the header row
    return result


@client.command()
async def tip(ctx):
    tips = csv_to_list('data/dnd_tips.csv')
    tip = random.choice(tips)
    await ctx.send(f":bulb: {tip[0]}")
    if tip[1] != "0":
        await ctx.send(f"`Sourced from {tip[1]}.`")


@client.command()
async def quirk(ctx, *args):
    quirks = csv_to_list('data/dnd_npc_quirks.csv')
    quirk = random.choice(quirks)
    if args:
        await ctx.send(f"{' '.join(args)} {quirk[0]}!")
    else:
        await ctx.send(f'This NPC {quirk[0]}!')

client.run(os.environ.get("TOKEN"))
