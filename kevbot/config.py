import json

def generate_config():
    bot_config = {}
    bot_config["name"] = "Kevbot"
    bot_config["core_limit"] = 4
    bot_config["log_path"] = "."
    bot_config["servers"] = {
            "Example 1": {
                "ignore": ["channel 1", "channel 2"],
                "responsiveness": 0.05 },
            "Example 2": {
                "ignore": ["channel 1", "channel 2"],
                "responsiveness": 1 }
            }
    with open("config.json", "w") as f:
        json.dump(bot_config, f)

def load_config(filename):
    bot_config = None
    with open(filename, "r") as f:
        try:
            bot_config = json.load(f)
        except ValueError:
            print("Invalid configuration JSON file!")
    return bot_config
