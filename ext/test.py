from ext.util.context import CustomContext
from discord.ext import commands
import discord
import asyncio
import random

class TestCog(commands.Cog):
    """A cog for testing the help command and embed builder."""
    def __init__(self, client):
        self.client = client

    @commands.command(brief = "Says whatever you want the bot to say.")
    async def say(self, ctx, *, message):
        await ctx.embed(title = "Say", description = message)

    @commands.command(brief = "Starts a raffle.")
    async def raffle(self, ctx, amount: int):
        MINIMUM_PLAYERS = 2
        JOIN_TIMEFRAME = 15

        msg = await ctx.send(f"{ctx.author} has started a raffle for ${amount}. React to join!")
        await msg.add_reaction("✅")

        await asyncio.sleep(JOIN_TIMEFRAME)

        players = [ctx.author.id]

        for reaction in msg.reactions:
            if str(reaction) == "✅":
                for user in reaction.users:
                    if user not in players: players.append(user)

        if len(players) < MINIMUM_PLAYERS:
            await ctx.send("Not enough players to start the raffle.")
        else:
            await ctx.send(f"{random.choice(players)} won the raffle for ${amount}.")

def setup(client):
    client.add_cog(TestCog(client))
