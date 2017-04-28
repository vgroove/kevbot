import asyncio
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord
import logging

logging.basicConfig(level=logging.INFO)
client = discord.Client()
bot = ChatBot(
        'Default Response Bot',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch'
        ],
        filters=[
            'chatterbot.filters.RepetitiveResponseFilter'
        ],
        database='chatterbot-database'
    )


@client.event
async def on_read():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    """Called when message is received on any channel on server"""
    if message.author.name != "Kevbot":
        response = bot.get_response(message.content)
        await client.send_message(message.channel, response)

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

if __name__ == "__main__":

    # Run Discord client
    client.run("MzA0NDQ2NzQwOTkwNTI1NDQw.C9mz2A.mMIaMFN86TCEtJTQiTCDxEZs9Bo")


    #bot.set_trainer(ChatterBotCorpusTrainer)
    #bot.train('chatterbot.corpus.english')

    # print("Type something to begin...")
    # while True:
    #     try:
    #         bot_input = bot.get_response(None)
    #     except (KeyboardInterrupt, EOFError, SystemExit):
    #         break
