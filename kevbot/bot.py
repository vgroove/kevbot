from concurrent.futures import ProcessPoolExecutor
import logging
from markov import MarkovMongo
import random

def _generate_worker(text):
    """Generate a response given any text"""
    words = text.split(' ')
    response = None

    if len(words) > 6:
        index = random.randint(0, len(words)-2)
        response = MarkovMongo().generate((words[index], words[index + 1]))
        logging.info("Generated \"{0}\" from seed \"({1}, {2})\"".format(
            response, words[index], words[index + 1]))
    elif len(words) > 2:
        index = random.randint(0, len(words)-1)
        response = MarkovMongo().generate(words[index])
        logging.info("Generated \"{0}\" from seed \"{1}\"".format(
            response, words[index]))
    else:
        response = MarkovMongo().generate()
        logging.info("Generated \"{0}\" with no seed".format(response))

    return response

def _update_db_worker(text):
    """Log words into chat engine data structure"""
    logging.info("Updating database with \"{0}\"...".format(text))
    MarkovMongo().insert_words(text)
    logging.info("Finished updating database with \"{0}\"...".format(text))
    return True

class Bot():
    """Does stuff"""

    def __init__(self, config):
        self.config = config
        if "core_limit" in self.config:
            self.update_exec = ProcessPoolExecutor(int(self.config["core_limit"]/2))
        else:
            self.update_exec = ProcessPoolExecutor()
        self.generate_exec = ProcessPoolExecutor()

    @property
    def name(self):
        """Gets current name of bot"""
        return self.config["name"]

    def should_respond(self, text, author, server, channel=None):
        """Determines if bot should respond based on configuration and command words"""
        if ((server in self.config["servers"] and
            channel not in self.config["servers"][server]["ignore"]) and
            (text.split(' ', 1)[0].lower() == self.config["name"].lower() or
            random.random() < self.config["servers"][server]["responsiveness"]) and
            author != self.name):
                return True
        return False

    def generate(self, text, loop=None):
        """Generate response given text. If given event loop run in separate process."""
        if loop is not None:
            return loop.run_in_executor(self.generate_exec, _generate_worker, text)
        return _generate_worker(text)


    def update_db(self, text, loop=None):
        """Updates database with given text. If given event loop run in separate process."""
        if loop is not None:
            return loop.run_in_executor(self.update_exec, _update_db_worker, text)
        return _update_db_worker(text)

