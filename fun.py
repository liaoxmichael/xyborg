import os
import time
import random
import re
import csv
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["8ball"])
    async def answer(self, ctx):
        answer = random.randint(1, 10)
        responses = [
            "maybe so",
            "hmm... how about no",
            "... I GUESS",
            "maybe later, little man",
            "god, what kind of question is that? gross",
            "pepis",
            "fuck",
            "in time, kiddo",
            "According to all known laws of aviation,",
            "do i have to answer that"
        ]
        await ctx.send(responses[answer - 1])

    @commands.command()
    async def joke(self, ctx):
        with open('data/jokes.csv', newline='') as jokefile:
            jokereader = csv.reader(jokefile)
            jokelist = [row for row in jokereader][1:]  # skip header
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

async def setup(bot):
    await bot.add_cog(Fun(bot))