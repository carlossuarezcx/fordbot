import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
hierro = 35
plastico = 145
vidrio = 145
bot = commands.Bot(command_prefix ='/')
slash = SlashCommand(bot, sync_commands=True)

def regla(material, porcentaje):
    total = (porcentaje*material) / 100
    return material - int(total)

@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    if " " in lower:
        lower= lower.replace(" ","")
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**", description="Todo parece indicar que aún no contamos con "+nombre.capitalize()+".\nPremium Deluxe Motorsport agradece tu preferencia.", colour=0x13D8)
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
    elif lower == "calleja":
       # img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha no es para cualquiera, vale mucho <3. \n(No hay foto para que no te enamores)", colour=0x13D8)
        #embed.set_image(url=img)
    await ctx.send(embed=embed)
@bot.command(name='cotizar')
async def consulta_ensamble(ctx, nombre):
    lower = nombre.lower()
    if " " in lower:
        lower= lower.replace(" ","")
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**",
                              description="Todo parece indicar que aún no contamos con " + nombre.capitalize() + ".\nPremium Deluxe Motorsport agradece tu preferencia.",
                              colour=0x13D8)
        for row in datos:
            if lower in row:
                x = row.split(",")
                if (x[0] == lower):
                    salida2 = "${:,}"
                    papeles = int(x[2])
                    h = int(x[3])
                    p = int(x[4])
                    v = int(x[5])
                    pu = int(x[6])
                    ll = int(x[7])
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/" + lower + ".png"
                    embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="\tTipo: " + x[1],
                                          colour=0x13D8)
                    embed.add_field(name="Costo papeles:",
                                    value=salida2.format(papeles), inline=False)
                    embed.add_field(name="Hierro: ",
                                    value="\t"+str(h), inline=False)
                    embed.add_field(name="Plástico: ",
                                    value="\t"+str(p), inline=False)
                    embed.add_field(name="Vidrio: ",
                                    value="\t"+str(v), inline=False)
                    embed.set_image(url=img)

    await ctx.send(embed=embed)
@bot.command(name='precioconmaterial')
async def consulta_preciomaterial(ctx, nombre, porcentaje):
    lower = nombre.lower()
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**", description="Todo parece indicar que aún no contamos con "+nombre.capitalize()+".\nPremium Deluxe Motorsport agradece tu preferencia.", colour=0x13D8)

        for row in datos:
            if lower in row:
                x = row.split(",")
                if(x[0]==lower):
                    porcentaje = int(porcentaje)
                    salida = "** Vehículo: " + x[0].capitalize() + "**\n\t- Tipo: "+ x[1]+ "\n\t- Precio Total: **${:,}.** "
                    salida2 = "\n\tPrecio aportando materiales: **${:,}.**"
                    papeles = int(x[2])
                    h=int(x[3])
                    p=int(x[4])
                    v=int(x[5])
                    pu=int(x[6])
                    ll=int(x[7])
                    totalh = regla(h,int(porcentaje))
                    totalp = regla(p,int(porcentaje))
                    totalv = regla(v,int(porcentaje))
                    texto = salida.format(papeles + (totalh* hierro) + ( totalp  * plastico) + (totalv * vidrio) + pu+ll)
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/"+lower+".png"
                    if img:
                        texto += img
                    embed = discord.Embed(title="**"+nombre.capitalize()+"**",  description="\tTipo: " +x[1], colour=0x13D8)
                    embed.add_field(name="*Incluye costos de logística*", value = salida2.format(papeles + (totalh* hierro) + ( totalp  * plastico) + (totalv * vidrio) + pu+ll), inline = False)
                    embed.set_image(url=img)

                    if (porcentaje > 80):
                        embed = discord.Embed(title="**Hola.**",
                                              description="La cantidad máxima de materiales es 80%.\nFord Motor Company agradece tu preferencia.",
                                              colour=0x13D8)
                    if (porcentaje <=0):
                        embed = discord.Embed(title="**Hola.**",
                                              description="La cantidad no es válida. Utliza **/precio _nombrevehículo_**\nPremium Deluxe Motorsport agradece tu preferencia.",
                                              colour=0x13D8)

    if lower == "effy":
        img="https://cdn.discordapp.com/avatars/439245514060464128/484c45c34c3db6232de8b1151d6071e3.png?size=512"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Hola, ella no tiene precio, por más dinero que tengas nunca te alcanzará c:", colour=0x13D8)
        embed.set_image(url=img)
    elif lower == "lavin":
        img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha es gratis, cualquiera puede tenerla.", colour=0x13D8)
        embed.set_image(url=img)
    elif lower == "calleja":
       # img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha no es para cualquiera, vale mucho <3. \n(No hay foto para que no te enamores)", colour=0x13D8)
        #embed.set_image(url=img)
    await ctx.send(embed=embed)

@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.\n(15 / 11 / 2021)**_\n- Blazer 3\n- Karin Calico GTF\n- GP 1\n- Luxor\n- Prototipo\n- Voltic\n- Xa2 1_"
    await ctx.send(texto)
@slash.slash(name='exclusivos',  description="Muestra los vehículos exclusivos")
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.\n(15 / 11 / 2021)**_\n- Blazer 3\n- Karin Calico GTF\n- GP 1\n- Luxor\n- Prototipo\n- Voltic\n- Xa2 1_"
    await ctx.send(texto)
@slash.slash(name='precio',  description="Muestra el precio total del vehículo")
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    if " " in lower:
        lower= lower.replace(" ","")
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**", description="Todo parece indicar que aún no contamos con "+nombre.capitalize()+".\nPremium Deluxe Motorsport agradece tu preferencia.", colour=0x13D8)
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
    elif lower == "calleja":
       # img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha no es para cualquiera, vale mucho <3. \n(No hay foto para que no te enamores)", colour=0x13D8)
        #embed.set_image(url=img)
    await ctx.send(embed=embed)
@slash.slash(name='precioconmaterial',  description="Muestra el precio total del vehículo proporcionando material.")
async def consulta_preciomaterial(ctx, nombre, porcentaje):
    lower = nombre.lower()
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**", description="Todo parece indicar que aún no contamos con "+nombre.capitalize()+".\nPremium Deluxe Motorsport agradece tu preferencia.", colour=0x13D8)
        for row in datos:
            if lower in row:
                x = row.split(",")
                if(x[0]==lower):
                    porcentaje = int(porcentaje)
                    salida = "** Vehículo: " + x[0].capitalize() + "**\n\t- Tipo: "+ x[1]+ "\n\t- Precio Total: **${:,}.** "
                    salida2 = "\n\tPrecio aportando materiales: **${:,}.**"
                    papeles = int(x[2])
                    h=int(x[3])
                    p=int(x[4])
                    v=int(x[5])
                    pu=int(x[6])
                    ll=int(x[7])
                    totalh = regla(h,int(porcentaje))
                    totalp = regla(p,int(porcentaje))
                    totalv = regla(v,int(porcentaje))

                    texto = salida.format(papeles + (totalh* hierro) + ( totalp  * plastico) + (totalv * vidrio) + pu+ll)
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/"+lower+".png"
                    if img:
                        texto += img
                    embed = discord.Embed(title="**"+nombre.capitalize()+"**",  description="\tTipo: " +x[1], colour=0x13D8)
                    embed.add_field(name="*Incluye costos de logística*", value = salida2.format(papeles + (totalh* hierro) + ( totalp  * plastico) + (totalv * vidrio) + pu+ll), inline = False)
                    embed.set_image(url=img)

                    if (porcentaje > 80):
                        embed = discord.Embed(title="**Hola.**",
                                              description="La cantidad máxima de materiales es 80%.\nPremium Deluxe Motorsport agradece tu preferencia.",
                                              colour=0x13D8)
                    if (porcentaje <=0):
                        embed = discord.Embed(title="**Hola.**",
                                              description="La cantidad no es válida. Utliza **/precio _nombrevehículo_**\nPremium Deluxe Motorsport agradece tu preferencia.",
                                              colour=0x13D8)

    if lower == "effy":
        img="https://cdn.discordapp.com/avatars/439245514060464128/484c45c34c3db6232de8b1151d6071e3.png?size=512"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Hola, ella no tiene precio, por más dinero que tengas nunca te alcanzará c:", colour=0x13D8)
        embed.set_image(url=img)
    elif lower == "lavin":
        img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha es gratis, cualquiera puede tenerla.", colour=0x13D8)
        embed.set_image(url=img)
    elif lower == "calleja":
       # img = "https://site-static.up-cdn.com/f/7e65ffa29ed72bf6902b2068f13931ebf0148d415e03cc6e42af521165ac72ec04e91cd5488cbd45/960x960"
        embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="Esa muchacha no es para cualquiera, vale mucho <3. \n(No hay foto para que no te enamores)", colour=0x13D8)
        #embed.set_image(url=img)
    await ctx.send(embed=embed)
@slash.slash(name='cotizar',  description="Muestra la cantidad de materiales del vehículo")
async def consulta_ensamble(ctx, nombre):
    lower = nombre.lower()
    if " " in lower:
        lower= lower.replace(" ","")
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**",
                              description="Todo parece indicar que aún no contamos con " + nombre.capitalize() + ".\nPremium Deluxe Motorsport agradece tu preferencia.",
                              colour=0x13D8)
        for row in datos:
            if lower in row:
                x = row.split(",")
                if (x[0] == lower):
                    salida2 = "${:,}"
                    papeles = int(x[2])
                    h = int(x[3])
                    p = int(x[4])
                    v = int(x[5])
                    pu = int(x[6])
                    ll = int(x[7])
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/" + lower + ".png"
                    embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="\tTipo: " + x[1],
                                          colour=0x13D8)
                    embed.add_field(name="Costo papeles:",
                                    value=salida2.format(papeles), inline=False)
                    embed.add_field(name="Hierro: ",
                                    value="\t"+str(h), inline=False)
                    embed.add_field(name="Plástico: ",
                                    value="\t"+str(p), inline=False)
                    embed.add_field(name="Vidrio: ",
                                    value="\t"+str(v), inline=False)
                    embed.set_image(url=img)
    await ctx.send(embed=embed)  
@slash.slash(name='desguazar',  description="Muestra la cantidad de materiales restantes al desguazar")
async def consulta_desguace(ctx, nombre, kilometros):
    lower = nombre.lower()
    if " " in lower:
        lower= lower.replace(" ","")
    with open('autoscsvtxt.txt', newline='') as File:
        datos = File.readlines()
        embed = discord.Embed(title="**Hola.**",
                              description="Todo parece indicar que aún no tenemos información para: " + nombre.capitalize() + ".\nPremium Deluxe Motorsport agradece tu preferencia.",
                              colour=0x13D8)
        for row in datos:
            if lower in row:
                x = row.split(",")
                if (x[0] == lower):
                    kilometros = int(kilometros)
                    h = int(x[3]-kilometros)
                    p = int(x[4]-kilometros)
                    v = int(x[5]-kilometros)
                    img = "\nhttps://site-static.up-cdn.com/modules/gtav/vehiculos/res/vehicles/" + lower + ".png"
                    embed = discord.Embed(title="**" + nombre.capitalize() + "**", description="\tTipo: " + x[1],
                                          colour=0x13D8)
                    embed.add_field(name="Hierro: ",
                                    value="\t"+str(h), inline=False)
                    embed.add_field(name="Plástico: ",
                                    value="\t"+str(p), inline=False)
                    embed.add_field(name="Vidrio: ",
                                    value="\t"+str(v), inline=False)
                    embed.add_field(name="(Función en etapa experimental, no se garantiza el resultado))",
                                    value=":)", inline=False)
                    embed.set_image(url=img)

    await ctx.send(embed=embed)  
@bot.event
async def on_ready():
    activity = discord.Game(name="RAGE Multiplayer", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")
bot.run(os.environ['tokendiscord'])
