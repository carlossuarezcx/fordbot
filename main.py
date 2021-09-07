import os
from discord.ext import commands
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    texto = ""
    if lower == "double":
        texto = ""
    elif lower == "infernus2":
        texto=" "
    elif lower == "lavin":
        texto="Ese muchacho es gratis."    
    else:
        texto="Vehículo no encontrado"

    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])