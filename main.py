import os
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
        for row in datos:
            if lower in row:
                x = row.split(",")
                if(x[0]==lower):
                    salida = "**" + x[0] + "**\n\t- Tipo: "+ x[1]+ "\n\t- Precio Total: **${:,}.** "
                    papeles = int(x[2])
                    h=int(x[3])
                    p=int(x[4])
                    v=int(x[5])
                    pu=int(x[6])
                    ll=int(x[7])
                    texto = salida.format(papeles+ (h* hierro) + (p*plastico) + (v* vidrio) + pu+ll)
            else:
                texto = "Hola, gracias por preferirnos. \nTodo parece indicar que aún no contamos con " + nombre + "."

    await ctx.send(texto)
@bot.command(name='exclusivos')
async def consulta_ex(ctx):
    texto = "**Vehículos exclusivos de la semana.**_\n- Baller 6 \n- Blazer 3\n- Chimera\n- Dukes 3\n- Issi 7\n- Novak\n- Seasparrow 2_"
    await ctx.send(texto)
bot.run(os.environ['tokendiscord'])