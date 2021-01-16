import discord
import asyncio
import random
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='$')
bot.remove_command("help")

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
    url = "https://media.giphy.com/media/l0G17mKNa6XJHYN5m/giphy.gif"
    emb = discord.Embed(title="Choking " + username, color=0x42cf29)
    emb.set_image(url=url)
    await ctx.send(embed=emb)

@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title="No.", color=0x0e4780))

@bot.command()
async def embed(ctx):
    msgs = []
    sender = ctx.author
    senderavatar = str(sender.avatar_url)
    sendername = str(sender.display_name)
    msg0 = await ctx.send(embed=discord.Embed(title="Where do you want to send the embed?", color=0xff0000))

    def check(msg):
        return msg.channel == ctx.channel and msg.author == sender

    msg1 = await bot.wait_for("message", check=check)
    msgs.append(msg1)
    channel = discord.utils.get(ctx.guild.channels, mention=msg1.content, type=discord.ChannelType.text)
    if channel is None:
        await ctx.send(embed=discord.Embed(title="Error!", color=0xff0000, description="You need to mention a channel!"))
        return
    await msg1.delete()
    await msg0.edit(embed=discord.Embed(title="What title do you want?", color=0xff0000, description="Type cancel to cancel."))
    msg2 = await bot.wait_for("message", check=check)
    msgs.append(msg2)
    title = msg2.content

    if(title == "cancel"):
        await ctx.send(embed=discord.Embed(title="Canceled!", color=0xff0000))
        return

    await msg2.delete()
    await msg0.edit(embed=discord.Embed(title="What description do you want?", color=0xff0000, description="Type cancel to cancel."))
    msg3 = await bot.wait_for("message", check=check)
    msgs.append(msg3)
    description = msg3.content
    if (description == "cancel"):
        await ctx.send(embed=discord.Embed(title="Canceled!", color=0xff0000))
        return
    await msg3.delete()
    emb = discord.Embed(title=title, description=description, color=0xff0000)
    emb.set_footer(text="Sent by " + sendername, icon_url=senderavatar)
    await msg0.edit(embed=discord.Embed(title="Sending...", color=0xff0000))
    await channel.send(embed=emb)
    await msg0.edit(embed=discord.Embed(title="Successful!", description="Embed sent in " + str(channel.mention), color=0xff0000))



@bot.command()
async def clear(ctx, arg):
    try:
        limit = int(arg)
    except ValueError:
        await ctx.send(embed=discord.Embed(title="Error!", color=0xff0000, description="You need to specify a number!"))
        return
    messages = await ctx.channel.history(limit=limit + 1).flatten()


bot.run('Nzk5Njc4MDY0NTg5MTQ0MTQ0.YAHEOw.sMZKBiTl-AesLgimX7ajwXWJdOk')
