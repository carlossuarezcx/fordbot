import os
from discord.ext import commands
hierro = 50
plastico = 250
vidrio = 250
bot = commands.Bot(command_prefix ='/')
@bot.command(name='precio')
async def consulta_precio(ctx, nombre):
    lower = nombre.lower()
    texto=""

    ''''# = ===============================================================================================
    if lower == "infernus3":
        texto="**"+nombre+"**\n     -Tipo = SportClasico \n     -Precio Total = **$ "+str(110000+3500*hierro+1167*plastico+875*vidrio+20000+20000)+".**"

    elif lower == "infernus2":
        salida = "**" + nombre + "**\n\t- Tipo=SportClasico\n\t- Precio Total = **${:,}.** "
        texto = salida.format(110000 + 3500 * hierro + 1167 * plastico + 875 * vidrio + 20000 + 20000)

    elif lower == "baller6":
        salida = "**" + nombre + "**\n\t- Tipo=SUV\n\t- Precio Total = **${:,}.** "
        texto = salida.format(92000 + 6500 * hierro + 2167 * plastico + 1625 * vidrio + 20000 + 20000)

    elif lower == "blazer3":
        salida = "**" + nombre + "**\n\t- Tipo=MOTO\n\t- Precio Total = **${:,}.** "
        texto = salida.format(12000 + 4500 * hierro + 1500 * plastico + 1125 * vidrio + 0 + 20000)

    elif lower == "chimera":
        salida = "**" + nombre + "**\n\t- Tipo=MOTO\n\t- Precio Total = **${:,}.** "
        texto = salida.format(25000 + 417 * hierro + 313 * plastico + 208 * vidrio + 0 + 20000)

    elif lower == "dukes3":
        salida = "**" + nombre + "**\n\t- Tipo=CLASICO\n\t- Precio Total = **${:,}.** "
        texto = salida.format(50000 + 2750 * hierro + 2750 * plastico + 2750 * vidrio + 20000 + 20000)

    elif lower == "issi7":
        salida = "**" + nombre + "**\n\t- Tipo=COMPACTO\n\t- Precio Total = **${:,}.** "
        texto = salida.format(15000 + 292 * hierro + 100 * plastico + 70 * vidrio + 20000 + 20000)

    elif lower == "novak":
        salida = "**" + nombre + "**\n\t- Tipo=SUV\n\t- Precio Total = **${:,}.** "
        texto = salida.format(45000 + 7000 * hierro + 2333 * plastico + 1750 * vidrio + 20000 + 20000)

    elif lower == "seasparrow2":
        salida = "**" + nombre + "**\n\t- Tipo=HELICOPTERO\n\t- Precio Total = **${:,}.** "
        texto = salida.format(800000 + 11000 * hierro + 3667 * plastico + 2750 * vidrio + 20000 + 0)

    # = ===============================================================================================
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
    '''
    with open('autoscsvtxt.txt', newline='') as File:
        for row in File:
            x = row.split(",")
            if (x[0]==lower):
                salida = "**" + x[0] + "**\n\t- Tipo= "+ x[1]+ "\n\t- Precio Total = **${:,}.** "
                papeles = int(x[2])
                h=int(x[3])
                p=int(x[4])
                v=int(x[5])
                pu=int(x[6])
                ll=int(x[7])
                texto = salida.format(papeles+ (h* hierro) + (p*plastico) + (v* vidrio) + pu+ll)
            else:
                texto="Vehículo no encontrado."
    await ctx.send(texto)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.**_\n- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\n- Seasparrow 2_"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])