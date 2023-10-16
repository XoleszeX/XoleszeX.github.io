import discord
from discord import *

bot = discord.Bot()

@bot.event
async def on_ready():
    print("Uruchomiono bota")

#Przykładowa komenda embed
@bot.command(description="Przykładowa komenda embed")
async def embed(ctx, title, description):
    embed = discord.Embed(title=title, description=description)
    await ctx.respond(embed=embed)

bot.run("token bota")