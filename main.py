import commands
import copy
import datetime
import discord
import traceback

from colorama import Fore

from utils import SharedConstants, has_prefix, send_message
from super_secret_token import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = SharedConstants.client

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
            await send_message(message, f"welcum back <@{message.author.id}>, how did the masturbation go sir")

        # mentioning an afk person
        for mentioned_user in message.mentions:
            if mentioned_user.id in SharedConstants.afk_users:
                afk_data = SharedConstants.afk_users[mentioned_user.id]
                afk_msg = afk_data["message"]
                expiration = afk_data["until"]

                if expiration and datetime.datetime.now() > expiration:
                    del SharedConstants.afk_users[mentioned_user.id]
                else:
                    await send_message(message, f"{mentioned_user.mention} is masturbating or supposedly: {afk_msg}")

        # ignore normal messages
        if not message.content.startswith("$"):
            return

        content = copy.copy(message)
        content.content = content.content.lower()

        # commands
        if has_prefix(content, "$help"):
            await commands.help_command(message)

        elif has_prefix(content, "$sex"):
            await commands.sex_command(message)

        elif has_prefix(content, "$recipe"):
            await commands.recipe_command(message)

        elif has_prefix(content, "$rape"):
            await commands.dlink_command(message)

        elif has_prefix(content, "$ship"):
            await commands.ship_command(message)

        elif has_prefix(content, "$togglelogger"):
            await commands.toggle_logger_command(message)

        elif has_prefix(content, "$balance") or has_prefix(message, "$bal"):
            await commands.balance_command(message)

        elif has_prefix(content, "$coinflip") or has_prefix(message, "$cf"):
            await commands.coinflip_command(message)

        elif has_prefix(content, "$gift"):
            await commands.gift_command(message)

        elif has_prefix(content, "$bless"):
            await commands.bless_command(message)

        elif has_prefix(content, "$afk"):
            await commands.afk_command(message)

        elif has_prefix(content, "$spam"):
            await commands.spam_command(message)

        elif has_prefix(content, "$purge"):
            await commands.purge_command(message)

        elif has_prefix(content, "$roulette"):
            await commands.roulette_command(message)

        elif has_prefix(content, "$sexquery"):
            await commands.sex_stats_command(message)

        elif has_prefix(content, "$avatar"):
            await commands.avatar_command(message)

        elif has_prefix(content, "$hierarchy"):
            await commands.state_command(message)

        elif has_prefix(content, "$ball") or has_prefix(content, "$bals") or has_prefix(content, "$balls"):
            await send_message(message, "what if i put my balls in yo jaws")
        
        elif has_prefix(content, "$setbal") or has_prefix(content, "$setbalance"):
            await commands.setbal_command(message)

        else:
            return

        # to find out who the fuck is spamming the bot
        # i refuse to use logging module
        try:
            print(f"{Fore.RESET}[LOG] {Fore.GREEN}{message.author.display_name} ({message.author.name}) {Fore.RESET}used {Fore.CYAN}{message.content} {Fore.RESET}on {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")
        except AttributeError:
            pass

    except OverflowError:
        await send_message("ok you had your fun")
        SharedConstants.fucking_idiots.append(message.author.id)

    except Exception as e:  # let the users know it broke
        if not isinstance(e, KeyboardInterrupt):
            tb = traceback.format_exc()
            print(f"uhhhh we just got a(n) {type(e).__name__}: {e}\n{tb}")
            await send_message(message, "uh oh")

@client.event
async def on_message_delete(message: discord.Message) -> None:
    """log deleted messages. CURRENTLY BROKEN WITH EMBEDS AND ATTACHMENTS"""
    if not SharedConstants.LOGGING_MESSAGES or message.author == client.user:
        return

    print(f"{Fore.RESET}[LOG] logged a message {Fore.RED}deletion{Fore.RESET} in {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")

    # attachments
    content = message.content
    if message.attachments:
        for attachment in message.attachments:
            await send_message(message, f"<@{message.author.id}> imagine trying to delete {attachment.url}")

    # ignore attachment only messages
    if not content.strip():
        return

    await send_message(message, f"<@{message.author.id}> DELETED A MESSAGE! LMAO. YOU REALLY THOUGHT DELETING \"{content}\" WOULD WORK? HA. NO. STUPID FUCK. I HOPE YOU DIE.")

@client.event
async def on_message_edit(old_message: discord.Message, message: discord.Message) -> None:
    """log edited messages."""
    if not SharedConstants.LOGGING_MESSAGES or message.author == client.user:
        return

    content = old_message.content
    if not content.strip():
        return
    if content == message.content and old_message.attachments == message.attachments and old_message.embeds == message.embeds:
        return

    try:
        print(f"{Fore.RESET}[LOG] logged a message {Fore.BLUE}edit{Fore.RESET} in {Fore.MAGENTA}{message.guild.name}{Fore.RESET}")
    except:
        return

    # attachments
    if message.attachments:
        for attachment in message.attachments:
            await send_message(message, f"<@{message.author.id}> imagine trying to delete {attachment.url}")

    try:
        await send_message(message, f"<@{message.author.id}> edited this message because he has severe autism \nold content: \"{content}\"", message)
    except discord.errors.HTTPException:
        await send_message(message, "imagine trying to get me to log a message longer than i can send. rot in hell bitch.")


if __name__ == "__main__":
    client.run(TOKEN)
