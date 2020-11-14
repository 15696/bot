from discord.ext.commands import HelpCommand, Cog, command
from ext.util.context import CustomContext
import discord

class CustomHelpCommand(HelpCommand):
	async def send_bot_help(self, mapping):
		prefix = await self.context.bot.get_prefix(self.context.message)
		embed = discord.Embed(
			title = "Help",
			description = f"You can use {prefix}help to get more info on a command or category.",
			color = discord.Color.blue()
		)

		cogs = "\n".join([c if c not in ["Jishaku", "ErrorHandler"] else "" for c in self.context.bot.cogs.keys()])
		embed.add_field(name = "Categories", value = cogs)

		INVITE = "https://discord.com/api/oauth2/authorize?client_id=765998687423299585&permissions=8&scope=bot"
		embed.add_field(name = "Bot", value = f"[Invite]({INVITE})\n")

		embed.set_footer(text = "Press the reactions to scroll through categories.")
		await self.context.send(embed = embed)

	async def send_cog_help(self, cog: Cog):
		embed = discord.Embed(
			title = cog.qualified_name,
			description = cog.description,
			color = discord.Color.blue()
		)

		for cmd in cog.walk_commands():
			embed.add_field(name = await self.context.bot.get_prefix(self.context.message) + cmd.name, value = cmd.brief)

		if len(embed.fields) == 0:
			embed.add_field(name = "Error", value = "This category does not have any commands.")
		await self.context.send(embed = embed)

	async def send_group_help(self, group):
		await ctx.send("send subcommand help")

	async def send_command_help(self, command: command):
		embed = discord.Embed(
			title = "Help",
			description = f"Showing help on the command `{command.name}`.",
			color = discord.Color.blue()
		)
		embed.add_field(name = "Usage", value = "insert usage here")

		if len(command.aliases) == 0:
			aliases = "None"
		else:
			aliases = ", ".join(command.aliases)

		embed.add_field(name = "Aliases", value = aliases, inline = False)
		await self.context.send(embed = embed)
