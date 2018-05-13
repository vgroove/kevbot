# kevbot
TBOA personal assistant

## Getting started

1. Install `docker` and `docker-compose` on your system.
1. Clone the repository `git clone https://github.com/vgroove/kevbot`.
1. Configure Kevbot by either generating or obtaining a config file.
  - Generate config file in python shell, which will output a basic `config.json` that must be populated:
    ```
    $ cd kevbot
    $ python
    >>> from config import generate_config
    >>> generate_config()
    >>> quit()
    ```
   - Obtain TBOA server config by contacting me, the place `config.json` alongside `config.py`.
1. If you'd like to start with data, run `mkdir data` from the root of the cloned repository, then contact me for testdb files.
1. Navigate to the root of the repository, then run `docker-compose up -d`.  This will start a Kevbot container running the most recent code alongside a MongoDB container using the database files in `./data`.
1. Go talk to Kevbot on your server!
