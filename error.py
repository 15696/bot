from discord.ext import commands

class ErrorHandler(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			left = round(error.retry_after, 2)
			if error.cooldown.type == commands.BucketType.user:
				await ctx.error(f"You have {left} seconds left until you can use this command again.")
			elif error.cooldown.type == commands.BucketType.guild:
				await ctx.error(f"{left} seconds left until this server can use this command again.")
			elif error.cooldown.type == commands.BucketType.member:
				await ctx.error(f"You have {left} seconds left until you can use this command in this server again.")
			elif error.cooldown.type == commands.BucketType.channel:
				await ctx.error(f"{left} seconds left until this channel can use this command again.")
			else:
				await ctx.error(f"There is no cooldown message set for this cooldown type.")

		elif isinstance(error, commands.NoPrivateMessage):
			await ctx.error("You cannot use this command in direct messages!")
		elif isinstance(error, commands.MissingPermissions):
			await ctx.error("You don't have permission to do this!")
		elif isinstance(error, commands.BotMissingPermissions):
			await ctx.error("I don't have permission to do this!")
		elif isinstance(error, commands.CommandNotFound):
			await ctx.error("That command doesn't exist!")
		else:
			raise error
			await ctx.error(f"The bot owner can see more in the bot logs.\n```{error}```")

def setup(client):
	client.add_cog(ErrorHandler(client))
