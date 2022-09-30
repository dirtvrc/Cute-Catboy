import time
import discord
import psutil
import os

from discord.ext import commands
from utils import default, http


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self.process = psutil.Process(os.getpid())


    @commands.command()
    async def embed(self, ctx):
        """ Rules will go here I guess... """
        embed=discord.Embed(title="Rules", url="https://youtu.be/dQw4w9WgXcQ", description="**1.** Respect everyone here. Take the drama elsewhere.\n**2.** No NSFW outside of designated NSFW channels.\n**3.** No talking of illegal activities. This includes doxxing.\n**4.** No racism or gore.\n**5.** No spam.\n\nPlease react with the :white_check_mark: to accept these rules. ", color=0xff00e1) 
        await ctx.send(embed=embed)
  
    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=["joinme", "join", "botinvite"])
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(self.bot.user.id)}>")

    @commands.command()
    async def covid(self, ctx, *, country: str):
        """Covid-19 Statistics for any countries"""
        async with ctx.channel.typing():
            r = await http.get(f"https://disease.sh/v3/covid-19/countries/{country.lower()}", res_method="json")

            if "message" in r:
                return await ctx.send(f"The API returned an error:\n{r['message']}")

            json_data = [
                ("Total Cases", r["cases"]), ("Total Deaths", r["deaths"]),
                ("Total Recover", r["recovered"]), ("Total Active Cases", r["active"]),
                ("Total Critical Condition", r["critical"]), ("New Cases Today", r["todayCases"]),
                ("New Deaths Today", r["todayDeaths"]), ("New Recovery Today", r["todayRecovered"])
            ]

            embed = discord.Embed(
                description=f"The information provided was last updated <t:{int(r['updated'] / 1000)}:R>"
            )

            for name, value in json_data:
                embed.add_field(
                    name=name, value=f"{value:,}" if isinstance(value, int) else value
                )

            await ctx.send(
                f"**COVID-19** statistics in :flag_{r['countryInfo']['iso2'].lower()}: "
                f"**{country.capitalize()}** *({r['countryInfo']['iso3']})*",
                embed=embed
            )

    @commands.command(aliases=["info", "stats", "status"])
    async def about(self, ctx):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = sum(g.member_count for g in self.bot.guilds) / len(self.bot.guilds)

        embedColour = None
        if hasattr(ctx, "guild") and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.set_thumbnail(url=ctx.bot.user.avatar)
        embed.add_field(name="Last boot", value=default.date(self.bot.uptime, ago=True))
        embed.add_field(
            name=f"Developer{'' if len(self.config['owners']) == 1 else 's'}",
            value=", ".join([str(self.bot.get_user(x)) for x in self.config["owners"]])
        )
        embed.add_field(name="Library", value="discord.py")
        embed.add_field(name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers:,.2f} users/server )")
        embed.add_field(name="Commands loaded", value=len([x.name for x in self.bot.commands]))
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB")

        await ctx.send(content=f"ℹ About **{ctx.bot.user}**", embed=embed)


async def setup(bot):
    await bot.add_cog(Information(bot))
