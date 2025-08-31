import random
import csv
from discord.ext import commands

def csv_to_list(file):
    with open(file, newline='') as file:
        reader = csv.reader(file)
        result = list(reader)[1:]  # skip the header row
    return result

class DnD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tip(self, ctx):
        tips = csv_to_list('data/dnd_tips.csv')
        tip = random.choice(tips)
        await ctx.send(f":bulb: {tip[0]}")
        if tip[1] != "0":
            await ctx.send(f"`Sourced from {tip[1]}.`")

    @commands.command()
    async def quirk(self, ctx, *args):
        quirks = csv_to_list('data/dnd_npc_quirks.csv')
        quirk = random.choice(quirks)
        if args:
            await ctx.send(f"{' '.join(args)} {quirk[0]}!")
        else:
            await ctx.send(f'This NPC {quirk[0]}!')

async def setup(bot):
    await bot.add_cog(DnD(bot))