# rettibot aka retti's slave
> src of my overly aggressive bot

## commands
- prefix is $
- run `$help` command too see all commands
- run `$help (command)` to obtain extra info about that specific command

if a command returns "uh oh" means it errored the fuck out.

## other stuff it can do

- nothing much else but has a message logger, can be toggled with `$togglelogger`
- also logs attachments now (kinda broken)
- message logger is off by default, toggle with `$togglelogger`

- it can also log all commands now, in the console. might add a .log file later on.

- it also has a separate self checkout bot because waldo asked me to make one. the balances are synced.

to make this one work, add `CHECKOUT_TOKEN = <your other bot token here>` to the `super_secret_token.py` file, and add your items into a dict in a `items.py` file.

the dict should look like `ITEMS = {"name of item": <price of item>, ...}`

## usage
1. clone the repo
2. create a new file called `super_secret_token.py` and add `TOKEN = <your bot token>` in there. obviously replace <your bot token> with your actual bot's token.
if you don't know how to make a bot i won't explain that to you
3. creating a virtual environment for all the dependencies is highly recommended (`python -m venv .env` - `source .env/bin/activate` (linux))
4. install dependencies: `pip install -r requirements.txt`
4. `python main.py`

### and for the checkout bot
same thing, but `python checkout.py`

## notes

- recipes command won't work because you have to add your own recipes. github doesn't like me adding my own.
- to make recipes work you need to create `recipes.py` and add `recipes = {}` and then add your recipes in there.
- in case you don't know how to just google "how to make python dictionary entries"

## credits
- chatgpt
- guest (guestsneezeplays) (kinda)

### feel free to pr tho idk if i will merge them because i couldn't care less about this bot