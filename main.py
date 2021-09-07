import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('discord_token')
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    texto = ""
    if lower == "double":
        texto = ""
    elif lower == "infernus2":
        texto=" "
    else:
        texto="Vehículo no encontrado"

    await ctx.send(texto)
bot.run(token)