import discord
from discord.ext import commands
import requests
import random
import os 
from config import TOKEN 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

ANNOUNCE_CHANNEL_ID = 1450582004730036456


def get_poke_image_url():
    poke_id = random.randint(1, 1025)
    url = f'https://pokeapi.co/api/v2/pokemon/{poke_id}'

    headers = {
        "User-Agent": "DiscordBot"
    }

    res = requests.get(url, headers=headers, timeout=10)

    if res.status_code != 200:
        return "Erro ao acessar a PokéAPI 😢"

    data = res.json()
    return data["sprites"]["front_default"]

@bot.command()
async def pokerandom(ctx):
    image_url = get_poke_image_url()

    if image_url is None:
        await ctx.send("Não consegui pegar um Pokémon 😢")
        return

    await ctx.send(image_url)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')
    channel = bot.get_channel(ANNOUNCE_CHANNEL_ID)
    if channel:
        await channel.send("Eu to online!")
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def hello2(ctx):
    pasta = "images"

    arquivos = os.listdir(pasta)
    imagem = "hello.gif"
    caminho = os.path.join(pasta, imagem)
    await ctx.send(file=discord.File(caminho))
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

@bot.command()
async def memes(ctx):
    pasta = "images"

    arquivos = os.listdir(pasta)
    imagens = [f for f in arquivos if f.endswith(("meme.png", "picturte.png", "images.jpg", "skeleton.gif"))]

    if not imagens:
        await ctx.send("Nenhuma imagem encontrada 😢")
        return

    imagem_escolhida = random.choice(imagens)
    caminho = os.path.join(pasta, imagem_escolhida)

    await ctx.send(file=discord.File(caminho))
bot.run(TOKEN)