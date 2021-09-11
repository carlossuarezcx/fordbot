import os

import discord
from discord import Embed
from discord.ext import commands
hierro = 40
plastico = 210
vidrio = 210
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**", description="Todo parece indicar que aún no contamos con "+nombre.capitalize()+".\nFord Motor Company agradece tu preferencia.", colour=0x13D8)
        #texto = "Hola, gracias por preferirnos. \nTodo parece indicar que aún no contamos con __" + nombre + "__."
        for row in datos:
            if lower in row:
                x = row.split(",")
                if(x[0]==lower):
                    salida = "** Vehículo: " + x[0].capitalize() + "**\n\t- Tipo: "+ x[1]+ "\n\t- Precio Total: **${:,}.** "
                    salida2 = "\n\tPrecio total: **${:,}.**"
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
                    embed.add_field(name="*Incluye costos de logística*", value = salida2.format(papeles + (h * hierro) + (p*plastico) + (v * vidrio) + pu+ll), inline = False)
                    embed.set_image(url=img)

    if lower == "effy":
        img="https://cdn.discordapp.com/avatars/439245514060464128/484c45c34c3db6232de8b1151d6071e3.png?size=512"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Hola, ella no tiene precio, por más dinero que tengas nunca te alcanzará c:", colour=0x13D8)
        embed.set_image(url=img)
    elif lower == "lavin":
        img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha es gratis, cualquiera puede tenerla.", colour=0x13D8)
        embed.set_image(url=img)
    await ctx.send(embed=embed)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.**_\n- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\n- Seasparrow 2_"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])