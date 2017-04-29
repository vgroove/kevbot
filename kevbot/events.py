import asyncio
import discord
import logging
from markov import MarkovMongo
import random
import re

client = discord.Client()
mm = MarkovMongo()
is_url = re.compile("^(https?|ftp)://[^\s/$.?#].[^\s]*$@iS")

async def generate(seed=None):
    """Async task for generating a response"""
    return mm.generate(seed)

@client.event
async def on_read():
    logging.info('Logged in as: {0}, {1}'.format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    """Called when message is received on any channel on server"""
    if message.server.name == "Kevbot Test Server":
        words = message.content.split(' ')

        # Only respond configured amount of time or if spoken to
        if words[0].lower() == "kevbot" or random.random() < 0.05:
            logging.info("Responding to message: \"{0}\"".format(message.content))
            if len(words) > 6:
                index = random.randint(0, len(words)-2)
                response = await generate(seed=(words[index], words[index + 1]))
                logging.info("Generated \"{0}\" from seed \"({1}, {2})\"".format(
                    response, words[index], words[index + 1]))
            elif len(words) > 2:
                index = random.randint(0, len(words)-1)
                response = await generate(seed=words[index])
                logging.info("Generated \"{0}\" from seed \"{1}\"".format(
                    response, words[index]))
            else:
                response = await generate()
                logging.info("Generated \"{0}\" with no seed".format(response))
            if not is_url.match(response):
                logging.info("Sending response...")
                await client.send_message(message.channel, response)
            else:
                logging.info("Discarding response...")

    # Record conversation anytime someone else speaks
    if message.author.name != "Kevbot":
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

