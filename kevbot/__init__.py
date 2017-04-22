from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
client = discord.Client()
bot = ChatBot(
        'Default Response Bot',
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
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
    if message.author.name != "Kevbot":
        response = bot.get_response(message.content)
        await client.send_message(message.channel, response)

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
