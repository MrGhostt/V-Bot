import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot
from playsound import playsound

import tkinter as tk
import ttk
import urllib
import json

LARGE_FONT = ("Verdana", 12)
bot = commands.Bot(command_prefix='a.')
TOKEN = 'NDgyNzAzODQzNDM2NjU4Njk4.DsYUdA.kOt1_Z6MBPD4cfJReWBZHYLMVvQ'
from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))


load_opus_lib()


@bot.event
async def on_ready():
    print("hi")
opts = {
    'default_search': 'auto',
    'quiet': True,
}


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)


players = {}


@bot.command(pass_context=True)
async def play(ctx, *, url):
    global play_server
    play_server = ctx.message.server
    voice = bot.voice_client_in(play_server)
    global player
    player = await voice.create_ytdl_player(url, ytdl_options=opts)
    players[play_server.id] = player
    if player.is_live == True:
        await bot.say("Can not play live audio yet.")
    elif player.is_live == False:
        player.start()


async def pause(ctx):
    player.pause()


@bot.command(pass_context=True)
async def resume(ctx):
    player.resume()


@bot.command(pass_context=True)
async def volume(ctx, vol):
    vol = float(vol)
    vol = player.volume = vol
    ä


@bot.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()


@bot.command(pass_context=True)
async def gui(ctx):
    controller.show_frame(PageOne)

############################ GUI ############################################


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):  # This is a method

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # weight is like kinda priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Use at your own risk", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree",
                             command=quit)
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dota2 Chatwheel Sounds", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="TI 18",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Basic Sounds",
                             command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text="CyKa BLyaT Sounds",
                             command=lambda: controller.show_frame(PageFour))
        button4.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="TI 18!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Easiest Money",
                             command=lambda: playsound("https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/1/13/Chat_wheel_2018_easiest_money.mp3"))
        button1.pack()
        button2 = ttk.Button(self, text="Echo Slam",
                             command=lambda: playsound("https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/7/73/Chat_wheel_2018_echo_slama_jama.mp3"))
        button2.pack()
        button3 = ttk.Button(self, text="Oy Oy Oy",
                             command=lambda: playsound("https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/4/4c/Chat_wheel_2018_oy_oy_oy.mp3"))
        button3.pack()
        button4 = ttk.Button(self, text="Next Level",
                             command=lambda: playsound("https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/6/60/Chat_wheel_2018_next_level.mp3"))
        button4.pack()
        button5 = ttk.Button(self, text="Ta daa",
                             command=lambda: playsound("https://d1u5p3l4wpay3k.cloudfront.net/dota2_gamepedia/b/bb/Chat_wheel_2018_ta_daaaa.mp3"))
        button5.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Basic Sounds!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Sounds",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CyKa BLyaT", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Sounds",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()


app = SeaofBTCapp()


async def open_window()
    app.mainloop()

bot.loop.create_task(open_window())
bot.run(TOKEN)
