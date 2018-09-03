import discord 
import youtube_dl   
from discord.ext import commands


TOKEN= 'NDgyNzAzODQzNDM2NjU4Njk4.DmI67A.gjaikYAi2v0IAjQI_8RsDPlTkU8'
players = {}

client = commands.Bot(command_prefix = '#')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    print('Bot joined')


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    print('Bot left')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel,limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

client.run(TOKEN)
