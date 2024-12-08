# rettibot aka retti's slave
> src of my overly aggressive bot

## commands
- prefix is $
- run help command too see all commands
- run `$help (command)` to obtain extra info about that specific command

if a command returns "uh oh" means it errored the fuck out.

## other stuff it can do

- nothing much else but has a message logger, can be toggled with `$togglelogger`
- also logs attachments now
- message logger is on by default, toggle with `$togglelogger`

- it can also log all commands now, in the console. might add a .log file later on.

## usage
1. clone the repo
2. create a new file called `super_secret_token.py` and add `TOKEN = <your bot token>` in there. obviously replace <your bot token> with your actual bot's token.
if you don't know how to make a bot i won't explain that to you
3. creating a virtual environment for all the dependencies is highly recommended (`python -m venv .env` - `source .env/bin/activate` (linux))
4. `python main.py`

## notes

- recipes command won't work because you have to add your own recipes. github doesn't like me adding my own.
- there's some user ids left in there. if it bothers you just delete them or replace them.

## credits
- chatgpt
- guest (guestsneezeplays) (kinda)

### feel free to pr tho idk if i will merge them because i couldn't care less about this bot