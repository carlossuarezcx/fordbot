import os
from discord.ext import commands
hierro = 50
plastico = 210
vidrio = 210
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    if lower == "infernus2":
        texto="- Tipo = SportClasico \n- Precio Total = *"+str(110000+3500*hierro+1167*plastico+875*vidrio+20000+20000)+"*"
    elif lower == "":
        texto=" "
    elif lower == "calleja":
        texto="Esa muchacha es una interesada, te sale carísima."
    elif lower == "lavin":
        texto="Ese muchacho es gratis."
    elif lower == "effy":
        texto="Ella es inalcazable, es imposible poner un precio :3"
    else:
        texto="Vehículo no encontrado"

    await ctx.send(texto)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.**_\n- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\n- Seasparrow 2_"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])