import discord
import pymongo

class Member:
	def __init__(self, member: discord.Member):
		"""Initialize the discord.Member database helper."""
		self.client = pymongo.MongoClient("localhost", 27017)
		self.collection = self.client.discord.members
		self.query = self.collection.find_one({"id": member.id})

		if self.query is None:
			defaults = {
				"id": member.id,
				"balance": 200
			}

			self.collection.insert_one(defaults)

		self.member = member
		self.balance = self.query["balance"]

	def set_balance(self, value):
		document = self.collection.find_one({"id": self.member.id})
		self.collection.update_one({"id": self.member.id}, {"$set": {"balance": value}}, upsert = True)

	def add_balance(self, amount):
		self.set_balance(self.balance + amount)

	def subtract_balance(self, amount):
		self.set_balance(self.balance - amount)