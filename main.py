import os

import discord
from discord import Embed
from discord.ext import commands
hierro = 50
plastico = 250
vidrio = 250
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        texto = "Hola, gracias por preferirnos. \nTodo parece indicar que aún no contamos con __" + nombre + "__."
        for row in datos:
            if lower in row:
                x = row.split(",")
                if(x[0]==lower):
                    salida = "** Vehículo: " + x[0].capitalize() + "**\n\t- Tipo: "+ x[1]+ "\n\t- Precio Total: **${:,}.** "
                    salida2 = "\n\t**${:,}.**"
                    papeles = int(x[2])
                    h=int(x[3])
                    p=int(x[4])
                    v=int(x[5])
                    pu=int(x[6])
                    ll=int(x[7])
                    texto = salida.format(papeles+ (h* hierro) + (p*plastico) + (v* vidrio) + pu+ll)
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/"+lower+".png"
                    if img:
                        texto += img
                    embed = discord.Embed(title="**"+nombre.capitalize()+"**",  description="\tTipo: " +x[1], colour=0x13D8)
                    embed.add_field(name="\tPrecio Total", value = salida2.format(papeles + (h * hierro) + (p*plastico) + (v * vidrio) + pu+ll), inline = False)
                    embed.set_image(url=img)


    if lower == "effy":
        texto = "Hola, ella no tiene precio, por más dinero que tengas nunca te alcanzará c:"
    elif lower == "lavin":
        texto = "Hola, esa muchacha es gratis. Cualquiera puede tenerla."
    #await ctx.send(texto)
    await ctx.send(embed=embed)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.**_\n- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\n- Seasparrow 2_"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])