import asyncio
from concurrent.futures import ProcessPoolExecutor
import discord
import logging
from markov import MarkovMongo
import random
import re

client = discord.Client()
#chat_engine = MarkovMongo()
is_url = re.compile("^(https?|ftp)://[^\s/$.?#].[^\s]*$@iS")
generate_exec = ProcessPoolExecutor(1)
update_exec = ProcessPoolExecutor(2)

def generate(seed=None):
    """Generate a response given a seed"""
    return MarkovMongo().generate(seed)

def update_db(text):
    """Log words into chat engine data structure"""
    logging.info("Updating database with \"{0}\"...".format(text))
    MarkovMongo().insert_words(text)
    logging.info("Finished updating database with \"{0}\"...".format(text))

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
                response = await client.loop.run_in_executor(generate_exec, 
                        generate, (words[index], words[index + 1]))
                logging.info("Generated \"{0}\" from seed \"({1}, {2})\"".format(
                    response, words[index], words[index + 1]))
            elif len(words) > 2:
                index = random.randint(0, len(words)-1)
                response = await client.loop.run_in_executor(generate_exec,
                        generate, words[index])
                logging.info("Generated \"{0}\" from seed \"{1}\"".format(
                    response, words[index]))
            else:
                response = await client.loop.run_in_executor(generate_exec, generate)
                logging.info("Generated \"{0}\" with no seed".format(response))
            if not is_url.match(response):
                logging.info("Sending response...")
                await client.send_message(message.channel, response)
            else:
                logging.info("Discarding response...")

    # Record conversation anytime someone else speaks
    if message.author.name != "Kevbot":
        await client.loop.run_in_executor(update_exec, update_db, message.content)

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

