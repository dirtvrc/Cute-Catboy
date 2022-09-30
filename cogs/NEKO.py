import random
import discord
import secrets
import asyncio
import aiohttp
import hmtai

from io import BytesIO
from discord.ext import commands
from utils import permissions, http, default


class Neko_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()

    @commands.command(aliases=["sauce"])
    async def hentai(self, ctx):
        """ Random hentai """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","hentai")
        await ctx.send(bio)

    @commands.command()
    async def wave(self, ctx):
        """ Greeting! Wave gifs! (●'◡'●) """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","wave")
        await ctx.send(bio)

    @commands.command()
    async def poke(self, ctx):
        """ Poke-poke :P """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","poke")
        await ctx.send(bio)

    @commands.command()
    async def pat(self, ctx):
        """ Let's pat some good guys (/ω＼) """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","pat")
        await ctx.send(bio)

    @commands.command()
    async def kiss(self, ctx):
        """ Kissu! :3 """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","kiss")
        await ctx.send(bio)

    @commands.command()
    async def feed(self, ctx):
        """ Who want eat? :P """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","feed")
        await ctx.send(bio)

    @commands.command()
    async def hug(self, ctx):
        """ I like hugs, do you? """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","hug")
        await ctx.send(bio)

    @commands.command()
    async def cuddle(self, ctx):
        """ Cuddle cuddle cuddle xD """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","cuddle")
        await ctx.send(bio)

    @commands.command()
    async def cry(self, ctx):
        """ Bite bite biting :3 """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","cry")
        await ctx.send(bio)

    @commands.command()
    async def slap(self, ctx):
        """ 	BAKA!! """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","slap")
        await ctx.send(bio)

    @commands.command()
    async def lick(self, ctx):
        """ Mmm hum hum, so tasty~ """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","lick")
        await ctx.send(bio)

    @commands.command()
    async def bite(self, ctx):
        """ Nyaaaaaa!! """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","bite")
        await ctx.send(bio)

    @commands.command()
    async def dance(self, ctx):
        """ Move like lady jagger ヾ(≧▽≦*)o """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","dance")
        await ctx.send(bio)

    @commands.command()
    async def boop(self, ctx):
        """ Boopyy """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","boop")
        await ctx.send(bio)

    @commands.command()
    async def sleep(self, ctx):
        """ Zzz 💤 """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","sleep")
        await ctx.send(bio)

    @commands.command()
    async def like(self, ctx):
        """ I like it, nice 👍"""
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","like")
        await ctx.send(bio)

    @commands.command()
    async def kill(self, ctx):
        """ Kill everyone, everybody! """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","kill")
        await ctx.send(bio)

    @commands.command()
    async def tickle(self, ctx):
        """ Tiiickle tickle tickle :3 """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","tickle")
        await ctx.send(bio)

    @commands.command()
    async def depression(self, ctx):
        """ SFW depression Gifs :c """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","depression")
        await ctx.send(bio)

    @commands.command()
    async def neko(self, ctx):
        """ NSFW Neko Nyaaa! """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","nsfwNeko")
        await ctx.send(bio)

    @commands.command()
    async def gif(self, ctx):
        """ NSFW gif """
        if not permissions.can_handle(ctx, "attach_files"):
            return await ctx.send("I cannot send images here ;-;")

        bio = hmtai.get("hmtai","gif")
        await ctx.send(bio)

async def setup(bot):
    await bot.add_cog(Neko_Commands(bot))
