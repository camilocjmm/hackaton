import discord
from discord.ext import commands
import random
from model import get_class
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


recetas_saludables = [
    "ensalada de quinoa con aguacate y garbanzos",
    "salmón al horno con brócoli",
    "smoothie de espinaca, plátano y leche de almendras",
    "pollo a la plancha con verduras asadas"
]

informacion_clima = [
    "hace sol ☀️",
    "está nublado ☁️",
    "llueve ligeramente 🌧️",
    "tormenta eléctrica ⚡️"
]

ejercicios = [
    "haz 15 minutos de yoga",
    "corre 20 minutos",
    "realiza 3 series de 15 sentadillas",
    "haz 10 flexiones"
]

planeta = [
    "planta un árbol",
    "usa una bicicleta",
    "reduce el uso de plásticos",
    "recicla papel, vidrio y metales"
]

@bot.command()
async def clima(ctx, *, ciudad: str):
    info = obtener_clima(ciudad)
    await ctx.send(f"🌤️ El clima en {ciudad} es: {info}")
dq 


@bot.command(name="receta")
async def receta_saludable(ctx):
    receta = random.choice(recetas_saludable)
    await ctx.send(f"🍽️ Receta saludable: {receta}")


@bot.command(name="clima")
async def clima(ctx):
    clima = random.choice(informacion_clima)
    await ctx.send(f"🌤️ Clima actual: {clima}")


@bot.command(name="ejercicio")
async def ejercicio(ctx):
    ejercicio = random.choice(ejercicios)
    await ctx.send(f"🏋️ Sugerencia de ejercicio: {ejercicio}")


@bot.command(name="eco")
async def mejorar_clima(ctx):
    consejo = random.choice(planeta)
    await ctx.send(f"🌱 Consejo ecológico: {consejo}")


@bot.command(name="clasificar")
async def clasificar_mensaje(ctx, *, mensaje):
    categoria = get_class(mensaje)
    await ctx.send(f"📊 El mensaje fue clasificado como: {categoria}")


bot.run("TOKEN")
