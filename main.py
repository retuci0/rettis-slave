import commands
import datetime
import discord

from colorama import Fore

from shared_constants import SharedConstants
from super_secret_token import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f"uhh hi i guess")

@client.event
async def on_message(message: discord.Message) -> None:
    try:
        # ignore message if the sender is the bot
        if message.author == client.user:
            return
        
        # to find out who the fuck is spamming the bot
        if message.content.startswith("$"): # funny colors because i'm autistic
            print(f"{Fore.RESET}[LOG] {Fore.GREEN}{message.author.display_name} ({message.author.name}) {Fore.RESET}used {Fore.CYAN}{message.content} {Fore.RESET}on {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")
        
        # afk thingy
        if message.author.id in SharedConstants.afk_users:
            del SharedConstants.afk_users[message.author.id]
            await message.channel.send(f"welcum back <@{message.author.id}>, how did the masturbation go sir")
            
        for mentioned_user in message.mentions:
            if mentioned_user.id in SharedConstants.afk_users:
                afk_data = SharedConstants.afk_users[mentioned_user.id]
                afk_msg = afk_data['message']
                expiration = afk_data['until']
                
                if expiration and datetime.datetime.now() > expiration:
                    del SharedConstants.afk_users[mentioned_user.id]
                else:
                    await message.channel.send(f"{mentioned_user.mention} is masturbating or supposedly: {afk_msg}")

        # commands
        if message.content.startswith("$help"):
            await commands.help_command(message)

        if message.content.startswith("$sex"):
            await commands.sex_command(message)
        
        if message.content.startswith("$recipe"):
            await commands.recipe_command(message)
            
        if message.content.startswith("$rape"):
            await commands.dlink_command(message)
        
        if message.content.startswith("$ship"):
            await commands.ship_command(message)
        
        if message.content.startswith("$togglelogger"):
            await commands.toggle_logger_command(message)
        
        if message.content.startswith("$balance"):
            await commands.balance_command(message)
        
        if message.content.startswith("$cf") or message.content.startswith("$coinflip"):
            await commands.coinflip_command(message)
        
        if message.content.startswith("$gift"):
            await commands.gift_command(message)
        
        if message.content.startswith("$bless"):
            await commands.bless_command(message)
        
        if message.content.startswith("$afk"):
            await commands.afk_command(message)
        
        if message.content.startswith("$spam"):
            await commands.spam_command(message)
        
        if message.content.startswith("$purge"):
            await commands.purge_command(message)
            
    except Exception as e:  # let the users know it broke
        if type(e) != KeyboardInterrupt:
            print("uhhhh " + str(e))
            await message.channel.send("uh oh")
    
@client.event
async def on_message_delete(message: discord.Message) -> None:
    """message logger."""
    if not SharedConstants.LOGGING_MESSAGES or message.author == client.user:
        return
    
    print(f"{Fore.RESET}[LOG] logged a message in {Fore.RED}{message.guild.name}{Fore.RESET}")
    
    # attachments
    content = message.content
    if message.attachments:
        for attachment in message.attachments:
            await message.channel.send(f"<@{message.author.id}> imagine trying to delete {attachment.url}")
            
    if not content.strip():
        return
    
    await message.channel.send(f"<@{message.author.id}> DELETED A MESSAGE! LMAO. YOU REALLY THOUGHT DELETING \"{content}\" WOULD WORK? HA. NO. STUPID FUCK. I HOPE YOU DIE.")

client.run(TOKEN)