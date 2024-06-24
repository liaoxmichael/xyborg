#like to call it: Thursday
import datetime
import asyncio
from discord.ext import commands, tasks
import discord
from random import randint

class Asuka(commands.Cog):
    def __init__(self, bot, AnnounceChannel0, AnnounceChannel1):
        self.bot = bot
        self.channelPlaceList = [AnnounceChannel0, AnnounceChannel1] #AnnounceChannel passed as an int
        self.wednesday = False
        self.LikeToCall.start()

    def cog_unload(self):
        self.LikeToCall.cancel()

    @tasks.loop(minutes = 1)
    async def LikeToCall(self):
        t = datetime.datetime.now()
        wkd = datetime.datetime.weekday(t)
        r = randint(1,7)
        # print("Running loop: rolled a " + str(r))
        if(r != 1):
            return
        if(wkd == 6):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/54137f2061164b9b61b5838ab3aa388b/tumblr_pb2ia3WNBj1ro4h8wo1_1280.jpg")
        if(wkd == 0):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/67b523d14b2df6308d2748fdaf76b6e1/tumblr_pb2ia3WNBj1ro4h8wo2_1280.jpg")
        if(wkd == 1):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/f7cac09cc4912c21e81a5f0f21428455/tumblr_pb2ia3WNBj1ro4h8wo3_1280.jpg")
        if(wkd == 2):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/b237e91fde1182d39733fe222b297ccf/tumblr_pb2ia3WNBj1ro4h8wo4_1280.png")
        if(wkd == 3):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/f7fedcf43ff00b6f761fdfd663b84650/tumblr_pb2ia3WNBj1ro4h8wo5_540.png")
        if(wkd == 4):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/aabff0f84f61bea125c6dbbbf44cd289/tumblr_pb2ia3WNBj1ro4h8wo6_1280.jpg")
        if(wkd == 5):
            if(t.hour == 3 and t.minute == 0):
                await self.bot.get_channel(self.channelPlaceList[1]).send("https://64.media.tumblr.com/bb25e517c640e7f1f71cbfae02a75268/tumblr_pb2ia3WNBj1ro4h8wo7_1280.jpg")
