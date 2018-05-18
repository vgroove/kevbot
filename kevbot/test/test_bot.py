from unittest import TestCase
from unittest.mock import patch
import kevbot.bot

class TestTextGenWorker(TestCase):

    def fake_good_gen(self, text=""):
        return "This is some random text!"

    def fake_bad_gen(self, text=""):
        return 80085

    def fake_except_gen(self, text=""):
        raise Exception("Had some trouble generating text!")

    @patch.object(kevbot.text_gen.markov.MarkovMongo, '__init__', return_value=None)
    @patch.object(kevbot.text_gen.markov.MarkovMongo, 'generate', new=fake_good_gen)
    def test_good_input_good_gen(self, mock_MarkovMongo):
        # Generate some messages with good input
        long_message = kevbot.bot._generate_worker("This is some really good input right here.")
        medium_message = kevbot.bot._generate_worker("This is good input.")
        short_message = kevbot.bot._generate_worker("Good input.")
        no_message = kevbot.bot._generate_worker("")

        # Check the messages are some sort of string
        self.assertTrue(isinstance(long_message, str))
        self.assertTrue(isinstance(medium_message, str))
        self.assertTrue(isinstance(short_message, str))
        self.assertTrue(isinstance(no_message, str))

        # Check that messages actually contain something
        self.assertTrue(len(long_message) > 0)
        self.assertTrue(len(medium_message) > 0)
        self.assertTrue(len(short_message) > 0)
        self.assertTrue(len(no_message) > 0)

    @patch.object(kevbot.text_gen.markov.MarkovMongo, '__init__', return_value=None)
    @patch.object(kevbot.text_gen.markov.MarkovMongo, 'generate', new=fake_bad_gen)
    def test_good_input_bad_gen(self, mock_MarkovMongo):
        # Generate some messages with good input
        long_message = kevbot.bot._generate_worker("This is some really good input right here.")
        medium_message = kevbot.bot._generate_worker("This is good input.")
        short_message = kevbot.bot._generate_worker("Good input.")
        no_message = kevbot.bot._generate_worker("")

        # Check the messages are some sort of string
        self.assertTrue(isinstance(long_message, str))
        self.assertTrue(isinstance(medium_message, str))
        self.assertTrue(isinstance(short_message, str))
        self.assertTrue(isinstance(no_message, str))

        # Check that messages actually contain something
        self.assertTrue(len(long_message) > 0)
        self.assertTrue(len(medium_message) > 0)
        self.assertTrue(len(short_message) > 0)
        self.assertTrue(len(no_message) > 0)

    @patch.object(kevbot.text_gen.markov.MarkovMongo, '__init__', return_value=None)
    @patch.object(kevbot.text_gen.markov.MarkovMongo, 'generate', new=fake_except_gen)
    def test_bad_input(self, mock_MarkovMongo):
        # Attempt to generate a message with bad input
        bad_message = kevbot.bot._generate_worker(80085)

        # Check the message is some sort of string
        self.assertTrue(isinstance(bad_message, str))

        # Check that message actually contains something
        self.assertTrue(len(bad_message) > 0)
