import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(926355378298572902)
    await channel.send(F'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(927102810816933969)
    await channel.send(F'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)} {ms}')

bot.run('OTI2MzUyNTI3MzEyNjk1MzM2.Yc6bBQ.bjx8LHfyLXlhnBkOU3tCNGlqpBU')

