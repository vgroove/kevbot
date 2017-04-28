import logging
from markov import MarkovMongo
from events import client

if __name__ == "__main__":
    """Run Kevbot"""
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Run Discord client
    logging.info("Connecting to Discord...")
    client.run("MzA0NDQ2NzQwOTkwNTI1NDQw.C9mz2A.mMIaMFN86TCEtJTQiTCDxEZs9Bo")

