# $help (command)
info = {
    "help": "what do you think this does moron \n`$help (command)`",
    "sex": "sexes people.\n `$sex <user pings separated by spaces>`. you can also sex someone by replying `$sex` to their message.",
    "balance": "shows your current balance in retdollars (R$ ARE NOT ROBUX), or another user's one \n `$balance|$bal (user ping)`",
    "coinflip": "50-50 chance of winning or losing your bet. gambling is awesome. \n`$coinflip|$cf <amount>`",
    "gift": "transfers the desired amount of R$ to the desired user \n`$gift <user ping> <amount|all>`",
    "bless": "summons money and gifts it to the desired person, instead of transferring it, kinda like a /give. requires admin. supports negative numbers. \n`$bless <user ping> <amount>`",
    "ship": "returns a random percentage of \"love\" between two people. percentages are persistent (stored). \n`$ship <user1> <user2>` or `$ship <user>` to ship yourself with that user.",
    "togglelogger": "toggles the message logger. requires admin. \n`$togglelogger (on|off|1|0|query|get)`",
    "recipe": "shows recipes for \"stuff\", if available. \n`$recipe <name|list>`",
    "rape": "DOES NOT RAPE A PERSON. it uses the dlink 9.8 vuln thing on an ip address, added it because i'm bored. to use it on fr*nch fucks, search for some on fofa. \n`$rape http://<ip>`",
    "afk": "sets you as afk, and lets other people know you are if they ping you. \n`$afk (amount of time in minutes) (reason / cause)`",
    "spam": "totally does not spam. \n`$spam (amount of messages)`",
    "purge": "mass deletes messages, for moderation purposes. also has a filter option, it can delete only messages that have that specific keyword. \n`$purge <amount of messages> (filter)`",
    "roulette": "GAMBLEING!!1!1!!1!!! \n`$roulette <red|black|low|high|1-36|0|00> <amount>` (e.g.: `$roulette red 50`). RUSSIAN IS NOT A BET TYPE WALDO",
    "sexquery": "returns the sex stats of a person, or yours if there's no mention. \n`$sexquery  (user)`",
    "amidildo": "are you a dildo?",
    "avatar": "returns the avatar of a user, or yours if there's no mention. \n`$avatar (user)`",
    "checkout_help": "commands for slef checkout bot. \n`$checkout_help`",
    "setbal": "sets the balance of a user. requires admin. also supports negatives and basic math expressions. \n`$setbal <user ping> <amount|math expression>`",
}


# $help text
text = """
very epick commands (prefix is $):
doing $help (command) will show you the help text for that command. though aliases (such as bal for balance) are not supported, because i am a fucking asshole and i have decided not to without any actual reason.
- help: what do you think this does moron. use `$help (command)` for more info.
- sex: sexes people
- recipe: sends recipes for "stuff"
- rape: uses the dlink 9.8 critical score thingy on an ip address.
- ship: ships 2 people and returns a random percentage. the generated percentages are persistent.
- togglelogger: toggles the message logger. needs admin to run.
- balance / bal: shows your current ballance in retdollars (R$)
- coinflip / cf: flips a coin for a 50-50 chance of winning or losing. specify the amount you want to bet and either lose it all or double it.
- gift: transfers the desired amount of money to the desired user.
- bless: summons money out of thin air and gives it to someone. requires admin.
- afk: sets you as afk.
- spam: if you're a mod and you're reading this it totally does not spam. if you're not, well then it does spam.
- purge: deletes messages.
- roulette: epick gambleing american roulette
- sexquery: sex stats.
- hierarchy: shows your state in the retucio hierarchy system
- avatar: returns the avatar of a user.
- checkout_help / chelp: commands for slef checkout bot. requires the other bot to be added separately
- setbal: sets the balance of a user. requires admin. also supports negatives and basic math expressions.

if command returns \"uh oh\" means it errored the fuck out.
"""


# aliases
info["bal"] = info["balance"]
info["cf"] = info["coinflip"]
info["chelp"] = info["checkout_help"]