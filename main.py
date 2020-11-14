from ext.util.help.help import CustomHelpCommand
from ext.util.context import CustomContext
from discord.ext import commands
import discord
import re, os

intents = discord.Intents.default()
intents.members = True
intents.presences = True

class Bot(commands.Bot):
	"""Subclassed for more functionality."""

	async def get_prefix(self, message):
		"""Determine the prefix for a specific guild."""
		return "-"

	async def get_context(self, message, *, cls = CustomContext):
		"""Return the custom context to use in our commands."""
		return await super().get_context(message, cls = cls)

	def add_cog(self, cog: commands.Cog):
		"""Override the original function to add a log message."""
		super().add_cog(cog)
		name = cog.__class__.__name__.upper()
		print(f"[{name}] Loaded.")

	def __init__(self):
		"""Initialize the super class."""
		super().__init__(
			command_prefix = self.get_prefix,
			case_insensitive = True,
			intents = intents,
			help_command = CustomHelpCommand(),
		)

	def load(self, path : str, unload = False):
		"""Provide a better way to load extensions."""
		for root, dirs, files in os.walk(path):
			dirs.remove("util") if "util" in dirs else None
			for name in files:
				if name.endswith(".py"):
					ext = ".".join(re.split("[^a-zA-Z]", root))[2:]
					if unload:
						self.unload_extension(ext + "." + name[:-3])
					else:
						self.load_extension(ext + "." + name[:-3])

client = Bot()

@client.command()
@commands.is_owner()
async def reload(ctx):
	client.load("./ext", unload = True)
	client.load("./ext")
	await ctx.result("Reloaded all extensions.")

client.load("./ext")
client.load_extension("jishaku")

with open("token.txt", "r") as token:
	client.run(token.read())
