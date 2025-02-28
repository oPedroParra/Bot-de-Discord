# Importações
import discord
from discord.ext import commands
import asyncio

# Permições do Bot
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

# Eventos do Bot
@client.event
async def on_connect():
    print(f'O bot está conectado ao discord!')

@client.event
async def on_disconnect():
    print(f'O bot está desconectado ou tentando conexão com o discord!')

@client.event
async def on_ready():
    print(f'O bot {client.user} está online!')

@client.event
async def on_member_join(member:discord.Member):
    channel = client.get_channel(1333857306844074078)
    if channel:
        welcome_embed = discord.Embed(title=f"Bem-vindo, {member.name}!", description="Aproveite o servidor!")
        welcome_embed.set_thumbnail(url=member.avatar.url)
        await channel.send(embed=welcome_embed)
    else:
        print("Canal não encontrado.")

# Comandos do Bot
@client.command()
async def bebaAgua(ctx:commands.Context):
    user = client.get_user(649395730192269312)
    if user: 
        while True:
            await ctx.send(f"Vai beber agua, {user.mention}")
            await asyncio.sleep(300)
    else:
        print("User não encontrado.")

@client.command()
async def oi(ctx:commands.Context):
    await ctx.reply(f"Olá, {ctx.author.display_name}")

@client.command()
async def ping(ctx:commands.Context):
    await ctx.send("Pong!")

# Token
client.run("token aqui")