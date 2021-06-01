import discord
from discord.ext import commands
import praw
import time
import random
import requests
from bs4 import BeautifulSoup
import json
import os

#Zachary Keffaber, 5/31/2021, BananaBot

reddit = praw.Reddit(client_id='redditclientid', client_secret='clientsecret', user_agent='BannanaBot7829103')

client = commands.Bot(command_prefix="$b ")
os.chdir(r'/Users/zachary7829/BannanaBot/xp')

@client.event
async def on_ready():
 await client.change_presence(status=discord.Status.idle, activity=discord.Game('$b info for info'))
 print("Bot is ready")

@client.command()
async def hello(ctx):
 await ctx.send("Hi")

@client.command()
async def greentext(ctx):
 posts = reddit.subreddit('greentext').hot(limit=25)
 random_post_number = random.randint(0,24)
 for i,post in enumerate(posts):
  if i == random_post_number:
   await ctx.send(post.url)

@client.command()
async def secretmegumintestcommand(ctx):
 await ctx.send("https://hg1.funnyjunk.com/large/pictures/04/a5/04a5ea_6343222.jpg")

@client.command()
@commands.has_any_role("Administrators", "Moderators")
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member} has been kicked!")

@client.command()
@commands.has_any_role("Administrators", "Moderators")
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention} has been banned!")
 
@client.command(name="meme")
async def meme(ctx):
 posts = reddit.subreddit('memes').hot(limit=50)
 random_post_number = random.randint(0,49)
 for i,post in enumerate(posts):
  if i == random_post_number:
   await ctx.send(post.url)

@client.command()
async def waifu(ctx):
 waifu_id = "https://github.com/zachary7829/BananaBot/raw/main/waifu/" + str(random.randint(1,11)) + ".jpg"
 await ctx.send(waifu_id)

@client.command()
@commands.has_any_role("Administrators", "Moderators")
async def unban(ctx, user: discord.User):
 guild = ctx.guild
 if ctx.author.guild_permissions.ban_members:
  await ctx.send(f"{user} has been successfully unbanned.")
  await guild.unban(user=user)
   
@client.command()
async def apphookup(ctx):
 posts = reddit.subreddit('apphookup').hot(limit=1)
 for i,post in enumerate(posts):
  await ctx.send("The latest deal I could find is: " + post.url)

@client.command()
async def info(ctx):
 await ctx.send('**Commands:**\n\n$b kick {member} - kicks member\n$b ban {member} - bans member\n$b unban {member} - unbans member\n$b balance - shows your balance\n$b beg - beg for money\n$b waifu - sends a pic of a waifu\n$b meme - sends a meme\n$b greentext - sends a 4chan post\n$b appdeal - sends a deal on apps/games\n$b hello - say hello to the bot\n\n\n**Source Code: **https://github.com/zachary7829/BananaBot')

@client.command()
async def balance(ctx):
 await open_account(ctx.author)
 user = ctx.author
 users = await get_bank_data()

 wallet_amt = users[str(user.id)]["wallet"]
 bank_amt = users[str(user.id)]["bank"]

 em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.blue())
 em.add_field(name = "Wallet",value = wallet_amt)
 em.add_field(name = "Bank balance",value = bank_amt)
 await ctx.send(embed = em)

@client.command()
async def beg(ctx):
 await open_account(ctx.author)
 users = await get_bank_data()
 user = ctx.author
 earnings = random.randrange(101)
 await ctx.send(f"Someone gave you {earnings} coins!")
 users[str(user.id)]["wallet"] += earnings
 with open("mainbank.json","w") as f:
  json.dump(users,f)
 

async def open_account(user):

 users = await get_bank_data()

 if str(user.id) in users:
  return False
 else:
  users[str(user.id)] = {}
  users[str(user.id)]["wallet"] = 0
  users[str(user.id)]["bank"] = 0

 with open("mainbank.json","w") as f:
  json.dump(users,f)
 return True

async def get_bank_data():
 with open("mainbank.json","r") as f:
  users = json.load(f)

 return users

client.run()
