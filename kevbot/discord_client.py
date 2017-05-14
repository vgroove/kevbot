import asyncio
from config import load_config
import discord
import logging

class DiscordClient(discord.Client):

    def __init__(self, bot):
        """Loads configuration for bot"""

        super(DiscordClient, self).__init__()
        self.bot = bot

    @asyncio.coroutine
    async def on_read(self):
        logging.info('Logged in as: {0}, {1}'.format(self.user.name, self.user.id))

    @asyncio.coroutine
    async def on_message(self, message):
        """Called when message is received on any channel on server"""

        # Respond to message if not in an ignored channel
        if self.bot.should_respond(message.content, message.server.name, message.channel.name):
            response = await self.loop.run_in_executor(self.bot.generate_exec, 
                    self.bot.generate, message.content)

            if response is not None:
                logging.info("Sending response...")
                await self.send_message(message.channel, response)
        
        # Record conversation anytime someone else speaks
        if message.author.name != self.config["name"]:
            await self.loop.run_in_executor(self.bot.update_exec, self.bot.update_db, message.content)

    @asyncio.coroutine
    async def on_reaction_add(self, reaction, user):
        """Called when a message has a reaction added to it"""

    @asyncio.coroutine
    async def on_channel_delete(self, channel):
        """Called when a channel is deleted"""

    @asyncio.coroutine
    async def on_channel_create(self, channel):
        """Called when a channel is created"""

    @asyncio.coroutine
    async def on_channel_update(self, before, after):
        """Called when channel name, permissions, etc. are changed"""

    @asyncio.coroutine
    async def on_member_join(self, member):
        """Called when a member joins the server"""

    @asyncio.coroutine
    async def on_member_remove(self, member):
        """Called when a member leaves the server"""

    @asyncio.coroutine
    async def on_member_update(self, before, after):
        """Called when member status, game playing, nickname, etc. are changed"""

    @asyncio.coroutine
    async def on_server_join(self, server):
        """Called when client joins a server"""
