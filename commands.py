import aiohttp
import discord
import requests
import random
import time

from datetime import datetime, timedelta

from dlink_thingy import exploit, verify
from data import ensure_user_balance, load_balances, save_balances, load_sex_counts, save_sex_counts, load_ships, save_ships
from help_texts import info, text
from recipes import recipes
from utils import SharedConstants, is_peasant, safe_eval, send_message

from super_secret_token import TOKEN

from utils import SharedConstants

# holy shit i've been looking at my code and it's so messy
# who the fuck wrote this
# /s

# i will try to follow pep8 guidelines from now on

# for those who don't know what "# MARK" means, it just makes the text following it appear bigger on the vscode minimap, making the code easier to navigate. it does not mean my name is mark.

# also, i don't give a shit about your "ew your bot is bad it uses an outdated way to operate commands" or "imagine using json as database", these comments will just
# further encourage me to do the things above just to piss y'all off

# MARK: help
async def help_command(message: discord.Message) -> None:
    """displays all available commands."""
    args = message.content.split(" ")
    if len(args) != 2:
        await send_message(message, text)
        return
    
    command = args[1].lower().strip()
    try:
        await send_message(message, info[command])
    except KeyError:
        await send_message(message, f"{command} is not an indexed command, you cunt. use `$help` to see all available commands.")




# MARK: sex
async def sex_command(message: discord.Message) -> None:
    """sexes people, unless you're guest and trying to sex a female, in which case you are physically unable to."""
    counts = load_sex_counts()
    
    args = message.content.split(" ")
    if message.author.id == 1120699957415002212:  # just for guest
        for girl in SharedConstants.females:
            if str(girl) in message.content:
                await send_message(message, "nuh uh.")
                return
    
    # sex by replying to someone's message
    mentioned_user = list(message.mentions)
    if message.reference:
        reply = await message.channel.fetch_message(message.reference.message_id)
        author = await message.guild.fetch_member(reply.author.id)
        if author not in mentioned_user:
            mentioned_user.append(author)

    # no user to sex :(
    if (len(args) < 2 or not args[1].strip()) and not message.reference:
        await send_message(message, f"sexed no one (no bitches?)")
        return
    
    if mentioned_user:
        if message.author in mentioned_user:
            await send_message(message, "did you just try to sex yourself")
            return

        for user in mentioned_user:
            counts.setdefault(str(user.id), {"sexed": 0, "been_sexed": 0})
            counts.setdefault(str(message.author.id), {"sexed": 0, "been_sexed": 0})

            counts[str(message.author.id)]["sexed"] += 1
            counts[str(user.id)]["been_sexed"] += 1

        save_sex_counts(counts)

        text = "sexed "
        text += " and ".join([f"<@{user.id}>" for user in mentioned_user])
        await send_message(message, text)
    else:
        await send_message(message, f"sexed {' '.join(args[1:])}")
    
    # funny
    if random.randint(1, 11) == 11:
        amount = random.randint(10, 100)
        await send_message(message, "https://cdn.discordapp.com/attachments/1312208805097898004/1315651481973686333/poundtown-hip-thrust.mov?ex=67582f6c&is=6756ddec&hm=97b04f47923793489e0244d0216d170737efe82215c612d0b7668490625d16c8&")
        await send_message(message, f"you've been rewarded with {amount} R$ because you're a whore!")
        balances = ensure_user_balance(message.author.id)
        balances[str(message.author.id)] += amount
        save_balances(balances)




# MARK: recipe
async def recipe_command(message: discord.Message) -> None:
    """sends recipes for \"stuff\""""
    args = message.content.split(" ")
    
    if len(args) < 2 or not args[1].strip():
        await send_message(message, "you fucking moron you want a recipe for something right you don't want to cook thin air you dumbfuck do you")
        return
    
    recipe_name = args[1].lower().strip()
    if recipe_name == "list":
        recipes_text = "available recipes: "
        for recipe in sorted(list(recipes.keys())):
            recipes_text += recipe + ", "
        recipes_text = recipes_text.strip(", ")
        await send_message(message, recipes_text)
        return
    
    try:
        await send_message(message, recipes[recipe_name])
    except KeyError:
        await send_message(message, "no such recipe is available yet (let me cook)")




# MARK: dlink thingy
async def dlink_command(message: discord.Message) -> None:
    """uses the 9.8 critical score vulnerability discovered on some dlink routers on an ip address."""
    args = message.content.split(" ")
    
    if len(args) < 2 or not args[1].strip():
        await send_message(message, "pass a valid argument you nerd")
        return
    
    session = requests.Session()
    session.verify = False
    session.timeout = 5
    
    url = args[1].strip()
    command = ""
    for word in args[2:]:
        command += word + " "
    command = command.strip()
    
    try:
        request = requests.get(url)
    except Exception as e:
        await send_message(message, "uh oh")
        print(e)
        return
    
    if request.status_code != 200:
        await send_message(message, "invalid ip address. fucking moron.")
        return
    
    await send_message(message, "checking if target is vulnerable")
    if verify(url, session):
        await send_message(message, "yay target is vulnerable :D")
        await send_message(message, "performing the super mr robot secret popbob sex lava cactus dupe machine exploit...")
        await send_message(message, exploit(url, session, command))
    else:
        await send_message(message, "aww target is not vulnerable D:")
        return
    
    


# MARK: ship
async def ship_command(message: discord.Message) -> None:
    """returns a random percentage of so called \"love\" between two people. percentages are persistent."""
    args = message.content.split(" ")
    
    if len(args) > 3 or len(args) == 1:
        await send_message(message, "jesus christ. you're such a fucking dumbass. you goddamn idiot, imbecile, stupid faggot. i really hope you die and rot in hell, you fucking autistic piece of fuck. you have no place in this universe. you're an useless prick. you're a waste of oxygen, space and resources. i fucking hope your dumb stupid fucking ass trips in a staircase and you painfully fall to your death. or even better, you don't die but end up with a full body paralysis, not even being able to ask for an euthanasia. the only reason i have to keep living is to watch you suffer. you deserve no space in humanity. you're nothing more than an arrogant, useless, idiotic fuckstick. please die. please. (you didn't correctly pass all arguments.)")
        return
    
    if len(args) == 2:
        try:
            user1 = message.author.id
            user2 = int(args[1].strip("<@!>"))
        except ValueError:
            await send_message(message, "die nerd")
            return
    else: 
        try:
            user1 = int(args[1].strip("<@!>"))
            user2 = int(args[2].strip("<@!>"))
        except ValueError:
            await send_message(message, "die nerd")
            return
    
    if message.author.id == user1 and message.author.id == user2:
        await send_message(message, "pathetic")
        return
    
    if user1 == user2:
        await send_message(message, "go fuck yourself")
        return

    pair_key = " ".join(sorted([str(user1), str(user2)]))
    ships = load_ships()

    if pair_key in ships:
        percentage = ships[pair_key]
    else:
        percentage = random.randint(0, 100)
        ships[pair_key] = percentage
        save_ships(ships)
        
    user1_mention = f"<@{user1}>"
    user2_mention = f"<@{user2}>"
    
    comment = str()
    if percentage < 10:
        comment = "why am i not suprised"
    elif percentage < 20:
        comment = "not a chance in hell"
    elif percentage < 50:
        comment = "i mean if you took a shower once in a while there might be some chance"
    elif percentage < 75:
        comment = "maybe i was wrong when i said you repelled all women in a 10m radius"
    else:
        comment = "yessir. i can forsee lots of anal sex."
    
    await send_message(message, f"{user1_mention} ❤️ {user2_mention}: {percentage}% \n{comment}")




# MARK: logger
async def toggle_logger_command(message: discord.Message) -> None:
    """toggles the message logger that is triggered every time someone deletes or edits their message."""
    if is_peasant(message.author):
        await send_message(message, "who do you think you are to try and run this command? do you think you're important or something? you're not. fuck off you peasant.")
        return
    
    args = message.content.split(" ")
    try:
        arg = args[1].lower() if args[1] else "a"
    except IndexError:
        arg = "a"

    try:
        match arg:
            case "on" | "1":
                SharedConstants.LOGGING_MESSAGES = True
            case "off" | "0":
                SharedConstants.LOGGING_MESSAGES = False
            case "query" | "get":
                await send_message(message, f"anti racism module is currently {"enabled" if SharedConstants.LOGGING_MESSAGES else "disabled"}")
                return
            case _:
                SharedConstants.toggle_logging()
    except:
        pass    
     
    await send_message(message, f"message logging has been {"enabled" if SharedConstants.LOGGING_MESSAGES else "disabled"}.")        




# MARK: balance
async def balance_command(message: discord.Message):
    """returns the balance of the user or a mentioned user."""
    if len(message.mentions) > 0:
        user_id = message.mentions[0].id
    else:
        user_id = message.author.id
    
    balances = ensure_user_balance(user_id)
    await send_message(message, f"<@{user_id}> has **{balances[str(user_id)]}** retdollars (best currency fr fr)")




# MARK: cf
async def coinflip_command(message: discord.Message):
    """either doubles or loses your bet. martingale strategy goes brrrrr"""
    args = message.content.split(" ")
    if len(args) != 2 or (not args[1].isdigit() and args[1].lower().strip() != "all"):
        await send_message(message, "you moron just use `$cf <amount>` or `$cf all`. fuck you.")
        return

    user_id = message.author.id
    balances = ensure_user_balance(user_id)

    if args[1].lower().strip() == "all":
        bet = balances[str(user_id)]
    else:
        bet = int(args[1])

    if bet <= 0:
        await send_message(message, "no.")
        return

    if balances[str(user_id)] < bet:
        await send_message(message, f"LMAO YOU'RE SO BROKE. YOUR POOR ASS HAS {balances[str(user_id)]} R$ GET A FUCKING JOB")
        return

    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        balances[str(user_id)] += bet
        result = f"gambling is always the solution. your bet of {bet} R$ has been doubled. new balance: {balances[str(user_id)]} R$"
    else:
        balances[str(user_id)] -= bet
        result = f"take the L bozo. you lost it all, {bet} R$ less. new balance: {balances[str(user_id)]} R$. skill FUCKING issue."

    save_balances(balances)
    await send_message(message, result)




# MARK: gift
async def gift_command(message: discord.Message):
    """transfers an amount of money from your balance to another person's one."""
    args = message.content.split(" ")
    if len(args) != 3 or (not args[2].isdigit() and args[2] != "all"):
        await send_message(message, "i'm so tired of insulting you. please use the command correctly.")
        return
    
    # no mention or too many mentions
    giver_id = message.author.id
    recipient_mentions = message.mentions
    if len(recipient_mentions) != 1:
        await send_message(message, "mention just one user you nerd")
        return

    recipient_id = recipient_mentions[0].id
    if args[2] == "all":
        amount = ensure_user_balance(message.author.id)[str(message.author.id)]
    else:
        amount = int(args[2])
    
    # user tried giving himself money
    if recipient_id == giver_id:
        await send_message(message, "not a chance.")
        return

    # user tried to gift 0 R$
    if amount <= 0:
        await send_message(message, f"\"haha i'm so funny look i tried to gift someone 0 R$ please help me i suffer from child abuse\"")
        return

    balances = ensure_user_balance(giver_id)
    ensure_user_balance(recipient_id)

    # not enough money
    if balances[str(giver_id)] < amount:
        await send_message(message, f"you broke motherfucker you only have {balances[str(giver_id)]} R$")
        return

    balances[str(giver_id)] -= amount
    balances[str(recipient_id)] += amount
    save_balances(balances)

    await send_message(message, f"<@{giver_id}> has gifted {amount} R$ to <@{recipient_id}>")




# MARK: bless
async def bless_command(message: discord.Message):
    """summons money out of thin air and gifts it to a person. requires admin. supports negatives and basic math operations (1+1, etc.)."""
    if is_peasant(message.author):
        await send_message(message, "back off peasant.")
        return

    args = message.content.split(" ", 2)
    if len(args) != 3:
        await send_message(message, "usage: `$bless <user> <amount>`. also you're a fucking idiot")
        return

    try:
        amount = float(safe_eval(args[2]))
        if not (amount > -float("inf") and amount < float("inf")): # because waldo
            raise ValueError
    except (ValueError, OverflowError):
        await send_message(message, "invalid amount. usage: `$bless <user> <amount>`.")
        return

    recipient_mentions = message.mentions
    if len(recipient_mentions) != 1:
        await send_message(message, "when will you learn how to count")
        return
    recipient_id = recipient_mentions[0].id

    balances = ensure_user_balance(recipient_id)

    if balances[str(recipient_id)] + amount > SharedConstants.MAX_BALANCE:
        await send_message(message, "this blessing would exceed the maximum allowable balance. no greed.")
        return

    if amount == 0 or abs(amount) >= 1e+9:
        await send_message(message, "so funny.")
        return

    balances[str(recipient_id)] += amount
    save_balances(balances)

    await send_message(message, f"<@{recipient_id}> has been blessed by the almighty lord <@{message.author.id}> with {amount} R$")




# MARK: setbal
async def setbal_command(message: discord.Message) -> None:
    """sets the balance of a user to the desired amount. requires admin"""
    if is_peasant(message.author):
        await send_message(message, "back off peasant.")
        return

    args = message.content.split(" ", 2)
    if len(args) != 3:
        await send_message(message, "usage: `$setbal <user> <amount>`. also you're a fucking idiot")
        return

    try:
        amount = float(safe_eval(args[2]))
        if not (amount > -float("inf") and amount < float("inf")):
            raise ValueError
    except (ValueError, OverflowError):
        await send_message(message, "invalid amount. usage: `$setbal <user> <amount>`.")
        return

    if amount > SharedConstants.MAX_BALANCE:
        await send_message(message, "the balance cannot exceed the maximum allowable limit.")
        return

    recipient_mentions = message.mentions
    if len(recipient_mentions) != 1:
        await send_message(message, "when will you learn how to count")
        return
    recipient_id = recipient_mentions[0].id

    balances = ensure_user_balance(recipient_id)
    balances[str(recipient_id)] = amount
    save_balances(balances)

    await send_message(message, f"the balance of <@{recipient_id}> has been fixed to {amount} R$ by the almighty lord <@{message.author.id}>")




# MARK: afk
async def afk_command(message: discord.Message) -> None:
    """sets you as afk, if you're afk when someone pings you they will be reminded you're afk."""
    content = message.content[len("$afk"):].strip()
    afk_message = "masturbating"
    afk_until = None
    
    if content:
        parts = content.split(" ", 1)
        if parts[0].isdigit():
            afk_minutes = int(parts[0])
            if afk_minutes <= 0:
                await send_message(message, "haha good one so funny \n-# /s, obviously moron")
                return
            afk_message = parts[1] if len(parts) > 1 else "masturbating"
            afk_until = datetime.now() + timedelta(minutes=afk_minutes)
        else:
            afk_message = content
        
    SharedConstants.afk_users[message.author.id] = {"message": afk_message, "until": afk_until}
    time_msg = f" for {afk_minutes} min" if afk_until else ""
    await send_message(message, f"{message.author.mention} is now ~~masturbating~~ afk{time_msg}: {afk_message}")
        
            
        

# MARK: nuke
async def spam_command(message: discord.Message) -> None:
    """spam command because guest hasn't learned about for loops yet."""
    if message.author.id in SharedConstants.fucking_idiots:
        await send_message(message, "no.")
        return
    
    args = message.content.split(" ")
    if len(args) > 1:
        try:
            times = int(args[1])
        except:
            await send_message(message, "pass a valid number dumbass")
            return
    else:
        times = 10000
    
    # i > _ i don't care what pep says
    for i in range(times):
        await send_message(message, "GET NUKED MOFO BIG L OWNED BY GUEST AND RETTI | @everyone @everyone JOIN NOW https://discord.gg/R7G3ECwmVe")
        time.sleep(0.1) # discord ratelimit is 1000 requests per minute, which would be 0.0625 seconds between each request but i raised the cooldown to avoid any ratelimits
        
        
        

# MARK: purge
async def purge_command(message: discord.Message) -> None:
    """deletes the desired amount of messages."""
    if is_peasant(message.author):
        await send_message(message, "back off peasant.")
        return
    
    args = message.content.split(" ")
    if len(args) < 2:
        await send_message(message, "usage: `$purge <amount> (filter)`")
        return
    
    try:
        amount = int(args[1])
        if amount <= 0:
            raise ValueError("very funny")
    except ValueError:
        await send_message(message, "can't be that hard to learn to count, can it")
        return
    
    filter_word = args[2] if len(args) > 2 else None
    
    def check(msg):
        if filter_word:
            return filter_word in msg.content
        return True

    try:
        deleted = await message.channel.purge(limit=amount, check=check)
        await send_message(message, f"ok deleted {len(deleted)} messages", delete_after=3)
    except discord.Forbidden:
        await send_message(message, "aw crap i got no perms D:")
    except discord.HTTPException as e:
        await send_message(message, f"uhh erm uhmm uh erm uh {e}")
    
    
    
    
# MARK: roulette
async def roulette_command(message: discord.Message) -> None:
    """funy gambleing"""
    args = message.content.split()
    if len(args) < 3 or not args[2].isdigit():
        await send_message(message, "use the command properly: `$roulette <bet_type> <amount>`. > `$roulette red 50`, `$roulette 17 100` (wtf no insult?)")
        return

    bet_type = args[1].lower()
    bet_amount = int(args[2])
    user_id = message.author.id

    if bet_amount <= 0:
        await send_message(message, "no.")
        return

    balances = ensure_user_balance(user_id)
    if balances[str(user_id)] < bet_amount:
        await send_message(message, f"YOU'RE SO BROKE. YOUR POOR ASS ONLY HAS {balances[str(user_id)]} R$. GET A JOB.")
        return

    valid_bets = ["red", "black", "odd", "even", "high", "low", "0", "00"] + [str(i) for i in range(1, 37)]
    if bet_type not in valid_bets:
        await send_message(message, "you analphabet (haha anal). bet to something like `red`, `17`, `even`, `low`, etc.")
        return

    payout = {
        "red": 2, "black": 2, "odd": 2, "even": 2,
        "high": 2, "low": 2, "0": 36, "00": 36
    }
    wheel = {
        "red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
        "black": [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
        "green": [0, "00"]
    }

    result = random.choice(wheel["red"] + wheel["black"] + wheel["green"])
    outcome = "red" if result in wheel["red"] else "black" if result in wheel["black"] else "green"

    additional_info = []
    if isinstance(result, int):
        if result % 2 == 0:
            additional_info.append("even")
        else:
            additional_info.append("odd")
        if 1 <= result <= 18:
            additional_info.append("low")
        elif 19 <= result <= 36:
            additional_info.append("high")

    win = False
    if bet_type.isdigit():
        win = int(bet_type) == result
    elif bet_type in ["red", "black", "odd", "even", "high", "low"]:
        if bet_type == outcome:
            win = True
        elif bet_type == "odd" and isinstance(result, int) and result % 2 != 0:
            win = True
        elif bet_type == "even" and isinstance(result, int) and result % 2 == 0:
            win = True
        elif bet_type == "high" and isinstance(result, int) and 19 <= result <= 36:
            win = True
        elif bet_type == "low" and isinstance(result, int) and 1 <= result <= 18:
            win = True

    if win:
        multiplier = payout.get(bet_type, 1)
        winnings = bet_amount * (multiplier - 1)
        balances[str(user_id)] += winnings
        save_balances(balances)
        await send_message(message, f"ok the bouncy sphere landed on {result} ({outcome}, {' '.join(additional_info)}). so i guess you won {winnings} R$. new balance: {balances[str(user_id)]} R$. epick gambleing!!1!!1!")
    else:
        balances[str(user_id)] -= bet_amount
        save_balances(balances)
        await send_message(message, f"skill issue. the rotund tridimensional object landed on {result} ({outcome}, {' '.join(additional_info)}). {bet_amount} R$ less. new: {balances[str(user_id)]} R$")
        
        
        
# MARK: sex stats
async def sex_stats_command(message: discord.Message) -> None:
    """sex stats."""
    counts = load_sex_counts()
    user = message.mentions[0] if message.mentions else message.author
    stats = counts.get(str(user.id), {"sexed": 0, "been_sexed": 0})
    
    sexer_text = str()
    sexed_text = str()
    if stats["sexed"] >= 100:
        sexer_text = "(holy crap bro) "
    elif stats["sexed"] <= 0:
        sexer_text = "(fucking geek go outside) "
    if stats["been_sexed"] > 50:
        sexed_text = "(fucking whore)"
    
    await send_message(message, f"<@{user.id}> has sexed {stats["sexed"]} people {sexer_text}and been sexed {stats["been_sexed"]} times {sexed_text}")




# MARK: avatar
async def avatar_command(message: discord.Message) -> None:
    """get the avatar of a user."""
    args = message.content.strip().split(" ")

    if message.mentions:
        user = message.mentions[0]
    else:
        user = message.author

    async with aiohttp.ClientSession() as session:  # nesting goes brrrrr
        try:
            async with session.get(
                f"https://discord.com/api/v10/users/{user.id}",
                headers={"Authorization": "Bot " + TOKEN}
            ) as response:
                if response.status == 200:
                    user_data = await response.json()
                    avatar_hash = user_data.get("avatar")

                    if avatar_hash:
                        size = "512"
                        for arg in args:
                            if arg.isdigit() and arg in ["32", "64", "128", "256", "512"]: # just allow these resolutions because i said so, if a different one is passed, fallback to 512
                                size = arg
                                break

                        avatar_url = f"https://cdn.discordapp.com/avatars/{user.id}/{avatar_hash}.png?size={size}"

                        async with session.get(avatar_url) as avatar_response:
                            if avatar_response.status != 200:
                                await send_message(message, "sowwy mastew i faiwed yow TwT it wownt happwen agwain i pwomise O.o")
                                return

                        await send_message(message, f"{user.display_name}'s shitty pfp: {avatar_url}")
                        return

                raise aiohttp.ClientError("nuke greenland")  # :)

        except aiohttp.ClientError:
            await send_message(message, "sowwy mastew i faiwed yow TwT it wownt happwen agwain i pwomise O.o") # please ignore this, i don't want to talk about it
            return




# MARK: hierarchy
async def state_command(message: discord.Message) -> None:
    """send your state in the rettibot hierarchy."""
    await send_message(message, f"a literal god: {message.author.id == SharedConstants.the_almighty_retucio_user_id}")
    await send_message(message, f"dildo: {message.author.id in SharedConstants.dildos}")
    await send_message(message, f"peasant: {message.author.id in SharedConstants.fucking_idiots}")