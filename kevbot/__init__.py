import logging
from kevbot.bot import Bot
from kevbot.config import load_config
from kevbot.clients.discord_client import DiscordClient
from kevbot.text_gen.markov import MarkovMongo

def main():
    """Run Kevbot"""
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Read file from default location
    bot_config = "config.json"
    config = load_config(bot_config)

    # Creating bot and attaching to chat client
    bot = Bot(bot_config)
    client = DiscordClient(bot)

    # Running chat client
    logging.info("Connecting to Discord...")
    client.run(config["discord_key"])

if __name__ == "__main__":
    main()

