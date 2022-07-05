import discord
import os
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$sched'):
    await message.channel.send('Here\'s today\'s schedule')

client.run(os.getenv('key'))