import discord
import asyncio
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.command()
async def degr(ctx):
    await ctx.send(
        embed=discord.Embed(title="Do not talk to Degr", color=0x32a852, description="Do not talk to Degr! You may "
                                                                                     "get sexually assaulted!"))

@bot.command()
async def whois(ctx, person: discord.User):
    sender = ctx.author
    useravatar = str(person.avatar_url)
    username = str(person.display_name)
    userping = str(person.mention)
    senderavatar = str(sender.avatar_url)
    sendername = str(sender.display_name)
    embedx = discord.Embed(title=username, description=userping, color=0x02e0ca)
    embedx.set_author(name="Requested by " + sendername, icon_url=senderavatar)
    embedx.set_image(url=useravatar)
    await ctx.send(embed=embedx)

@bot.command()
async def choke(ctx, person: discord.User):
    username = str(person.display_name)
    url = "https://tenor.com/9JNv.gif"
    emb = discord.Embed(title="Choking " + username, color=0x42cf29)
    emb.set_image(url=url)
    await ctx.send(embed=emb)


bot.run('Nzk5Njc4MDY0NTg5MTQ0MTQ0.YAHEOw.sMZKBiTl-AesLgimX7ajwXWJdOk')
