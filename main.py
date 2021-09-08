import os
from discord.ext import commands
hierro = 50
plastico = 210
vidrio = 210
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    texto = ""
    if lower == "double":

        texto = " "
    elif lower == "infernus2":
        texto=" "
    elif lower == "lavin":
        texto="Ese muchacho es gratis."
    elif lower == "effy":
        texto="Ella es inalcazable, es imposible poner un precio :3"
    else:
        texto="Vehículo no encontrado"

    await ctx.send(texto)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\- Seasparrow 2**"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])