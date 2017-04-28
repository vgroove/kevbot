import asyncio
import discord
import logging
from markov import MarkovMongo

client = discord.Client()
mm = MarkovMongo()

@client.event
async def on_read():
    logging.info('Logged in as: {0}, {1}'.format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    """Called when message is received on any channel on server"""
    if message.author.name != "Kevbot":
        logging.info("Responding to message: \"{0}\"".format(message.content))
        response = mm.generate()
        await client.send_message(message.channel, response)
        logging.info("Updating database...")
        mm.insert_words(message.content)

@client.event
async def on_reaction_add(reaction, user):
    """Called when a message has a reaction added to it"""

@client.event
async def on_channel_delete(channel):
    """Called when a channel is deleted"""

@client.event
async def on_channel_create(channel):
    """Called when a channel is created"""

@client.event
async def on_channel_update(before, after):
    """Called when channel name, permissions, etc. are changed"""

@client.event
async def on_member_join(member):
    """Called when a member joins the server"""

@client.event
async def on_member_remove(member):
    """Called when a member leaves the server"""

@client.event
async def on_member_update(before, after):
    """Called when member status, game playing, nickname, etc. are changed"""

@client.event
async def on_server_join(server):
    """Called when client joins a server"""

