import discord
from discord.ext import commands
import os
from bmodules.exceptions import DiceError, ModError
from bmodules import DiceManager
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="~", help_command=None)


@client.event
async def on_ready():
    print(f"Hi, I'm {client.user}")


@bot.command()
async def roll(ctx, *args):
    try:
        r = DiceManager(args)
        await ctx.send(r.print_result())
    except DiceError:
        await ctx.send(
            "```fix\nOnly valid combinations of dice work (eg. 1d6, 1d20, 3d6, 2d100, etc..)```"
        )
    except ModError:
        await ctx.send(
            "```fix\nMust have a number or dice behind the mod (eg. 1d20+10, 2d4 + 2, etc..)```"
        )


@bot.command()
async def help(ctx, *args):
    await ctx.send("```WIP```")


bot.run(os.getenv("TOKEN"))
