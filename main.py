import commands
import datetime
import discord
import traceback

from colorama import Fore

from utils import SharedConstants, has_prefix
from super_secret_token import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"uhh hi i guess")

@client.event
async def on_disconnect() -> None:
    print(f"ok bye")

@client.event
async def on_message(message: discord.Message) -> None:
    try:
        # ignore message if the sender is the bot
        if message.author == client.user:
            return
                    
        # funny responses i guess
        if "kys" in message.content.lower():
            await message.reply("ok i'll keep myself safe :D")
        if "mate" in message.content.lower():
            await message.reply("so you call these things \"chips\" instead of crispity crunchy munchie crackerjack snacker nibbler snap crack n pop westpoolchestershireshire queen's jovely jubily delights? that's rather bit cringe, innit bruv")
        if "nuh uh" in message.content.lower():
            await message.reply("yuh uh")
        
        # afk thingy
        if message.author.id in SharedConstants.afk_users:
            del SharedConstants.afk_users[message.author.id]
            await message.channel.send(f"welcum back <@{message.author.id}>, how did the masturbation go sir")
            
        # mentioning an afk person
        for mentioned_user in message.mentions:
            if mentioned_user.id in SharedConstants.afk_users:
                afk_data = SharedConstants.afk_users[mentioned_user.id]
                afk_msg = afk_data["message"]
                expiration = afk_data["until"]
                
                if expiration and datetime.datetime.now() > expiration:
                    del SharedConstants.afk_users[mentioned_user.id]
                else:
                    await message.channel.send(f"{mentioned_user.mention} is masturbating or supposedly: {afk_msg}")
        
        # ignore normal messages
        if not message.content.startswith("$"):
            return
        
        # to find out who the fuck is spamming the bot
        # i refuse to use logging module
        print(f"{Fore.RESET}[LOG] {Fore.GREEN}{message.author.display_name} ({message.author.name}) {Fore.RESET}used {Fore.CYAN}{message.content} {Fore.RESET}on {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")

        # commands
        if has_prefix(message, "$help"):
            await commands.help_command(message)

        if has_prefix(message, "$sex"):
            await commands.sex_command(message)
        
        if has_prefix(message, "$recipe"):
            await commands.recipe_command(message)
            
        if has_prefix(message, "$rape"):
            await commands.dlink_command(message)
        
        if has_prefix(message, "$ship"):
            await commands.ship_command(message)
        
        if has_prefix(message, "$togglelogger"):
            await commands.toggle_logger_command(message)
        
        if has_prefix(message, "$balance") or has_prefix(message, "$bal"):
            await commands.balance_command(message)
        
        if has_prefix(message, "$coinflip") or has_prefix(message, "$cf"):
            await commands.coinflip_command(message)
        
        if has_prefix(message, "$gift"):
            await commands.gift_command(message)
        
        if has_prefix(message, "$bless"):
            await commands.bless_command(message)
        
        if has_prefix(message, "$afk"):
            await commands.afk_command(message)
        
        if has_prefix(message, "$spam"):
            await commands.spam_command(message)
        
        if has_prefix(message, "$purge"):
            await commands.purge_command(message)
        
        if has_prefix(message, "$roulette"):
            await commands.roulette_command(message)
        
        if has_prefix(message, "$sexquery"):
            await commands.sex_stats_command(message)
            
    except Exception as e:  # let the users know it broke
        if not isinstance(e, KeyboardInterrupt):
            tb = traceback.format_exc()
            print(f"uhhhh we just got a(n) {type(e).__name__}: {e}\n{tb}")
            await message.channel.send("uh oh")
    
@client.event
async def on_message_delete(message: discord.Message) -> None:
    """log deleted messages."""
    if not SharedConstants.LOGGING_MESSAGES or message.author == client.user:
        return
    
    print(f"{Fore.RESET}[LOG] logged a message {Fore.RED}deletion{Fore.RESET} in {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")
    
    # attachments
    content = message.content
    if message.attachments:
        for attachment in message.attachments:
            await message.channel.send(f"<@{message.author.id}> imagine trying to delete {attachment.url}")
    
    # ignore attachment only messages
    if not content.strip():
        return

    if len(content) > 3000:
        await message.channel.send(f"<@{message.author.id}> fuck you")
        return
    
    await message.channel.send(f"<@{message.author.id}> DELETED A MESSAGE! LMAO. YOU REALLY THOUGHT DELETING \"{content}\" WOULD WORK? HA. NO. STUPID FUCK. I HOPE YOU DIE.")

@client.event
async def on_message_edit(old_message: discord.Message, message: discord.Message) -> None:
    """log edited messages."""
    if not SharedConstants.LOGGING_MESSAGES or message.author == client.user:
        return
    
    print(f"{Fore.RESET}[LOG] logged a message {Fore.BLUE}edit{Fore.RESET} in {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")
    
    # attachments
    content = old_message.content
    if message.attachments:
        for attachment in message.attachments:
            await message.channel.send(f"<@{message.author.id}> imagine trying to delete {attachment.url}")
            
    if not content.strip():
        return

    if len(content) >= 2000:
        await message.channel.send(f"<@{message.author.id}> fuck you")
        return
    
    await message.reply(f"<@{message.author.id}> edited this message because he has severe autism \nold content: \"{content}\"")


if __name__ == "__main__":
    client.run(TOKEN)