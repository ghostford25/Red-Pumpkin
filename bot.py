import discord
from discord.ext import commands
import requests
import random
import os 
from config import TOKEN 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

quizzes_verdes = [
    {
        "pergunta": "Qual desses materiais demora mais para se decompor?",
        "opcoes": {
            "A": "Papel",
            "B": "Casca de banana",
            "C": "Garrafa plástica"
        },
        "resposta": "C"
    },
    {
        "pergunta": "Qual ação ajuda MAIS a reduzir a poluição?",
        "opcoes": {
            "A": "Jogar lixo no chão",
            "B": "Reciclar materiais",
            "C": "Queimar lixo"
        },
        "resposta": "B"
    },
    {
        "pergunta": "O que NÃO é reciclável?",
        "opcoes": {
            "A": "Vidro",
            "B": "Papel",
            "C": "Papel higiênico usado"
        },
        "resposta": "C"
    }
]

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
@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}👋!')

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
    await ctx.send('pong🏓!')

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

@bot.command()
async def polution(ctx):
    await ctx.send(
        "🌍 **Poluição** é a contaminação do meio ambiente por resíduos, fumaça, químicos e lixo.\n"
        "Ela afeta a saúde humana, os animais e o clima.\n\n"
        "Pequenas ações do dia a dia já ajudam muito!"
    )
@bot.command()
async def reciclagem(ctx):
    await ctx.send(
        "♻️ **Reciclagem** é o processo de transformar materiais usados em novos produtos.\n"
        "Isso ajuda a reduzir o lixo, economizar recursos naturais e proteger o meio ambiente.\n\n"
        "Separe seu lixo e recicle sempre que puder!"
    )

@bot.command()
async def reciGuia(ctx):
    await ctx.send(
        "♻️ **Guia rápido de reciclagem:**\n"
        "🟦 Papel → jornais, caixas\n"
        "🟥 Plástico → garrafas PET\n"
        "🟩 Vidro → garrafas, potes\n"
        "🟨 Metal → latinhas\n\n"
        "Sempre limpe os materiais antes de reciclar!"
    )
@bot.command()
async def ajudarplaneta(ctx):
    await ctx.send(
        "🌱 **Como ajudar a combater a poluição:**\n"
        "♻️ Recicle sempre que possível\n"
        "🚯 Não jogue lixo na rua\n"
        "🛍️ Evite plástico descartável\n"
        "🚲 Use transporte sustentável\n"
        "💧 Economize água"
    )
@bot.command()
async def impacto(ctx):
    await ctx.send(
        "⚠️ **Impactos da poluição:**\n"
        "🐟 Morte de animais aquáticos\n"
        "🌫️ Doenças respiratórias\n"
        "🌡️ Aquecimento global\n"
        "🏭 Contaminação do solo e da água"
    )
@bot.command()
async def quizverde(ctx):
    quiz = random.choice(quizzes_verdes)

    mensagem = (
        "🌱 **Quiz Verde** 🌱\n\n"
        f"❓ {quiz['pergunta']}\n\n"
        f"A) {quiz['opcoes']['A']}\n"
        f"B) {quiz['opcoes']['B']}\n"
        f"C) {quiz['opcoes']['C']}\n\n"
        "✏️ Responda com **A**, **B** ou **C**"
    )

    await ctx.send(mensagem)

    def check(m):
        return (
            m.author == ctx.author and
            m.channel == ctx.channel and
            m.content.upper() in ["A", "B", "C"]
        )

    try:
        resposta = await bot.wait_for("message", timeout=20.0, check=check)
        if resposta.content.upper() == quiz["resposta"]:
            await ctx.send("✅ **Correto!** Você ajudou o planeta 🌍💚")
        else:
            correta = quiz["resposta"]
            await ctx.send(
                f"❌ **Errado!**\n"
                f"A resposta correta era **{correta}) {quiz['opcoes'][correta]}**"
            )
    except:
        await ctx.send("⏰ Tempo esgotado! Tente novamente com `!quizverde`")

bot.run(TOKEN)
