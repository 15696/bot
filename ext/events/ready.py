from discord.ext import commands
import discord

class Ready(commands.Cog):
	"""Logs the on_ready event of the bot."""
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("[READY] Ready.")
		status = discord.Status.dnd
		name = "over " + str(len(self.client.users)) + " members"
		activity = discord.Activity(type = discord.ActivityType.watching, name = name)
		await self.client.change_presence(status = status, activity = activity)

def setup(client):
	client.add_cog(Ready(client))
