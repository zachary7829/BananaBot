import discord
from discord.ext import commands
import praw
import time
import random
import requests

reddit = praw.Reddit(client_id='redditclientid', client_secret='clientsecret', user_agent='BannanaBot7829103')

client = commands.Bot(command_prefix="$b ")

@client.event
async def on_ready():
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
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member} has been kicked!")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member} has been banned!")


client.run()
