import asyncio
import discord
import re
import time

from discord.ext import commands

from items import ITEMS

class SharedConstants:
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(intents=intents, command_prefix="$")

    LOGGING_MESSAGES: bool = False # defaulted to false because it's fucking dumb

    last_message_time = 0

    females: tuple = (
        842116081241030717, # girl 1
        820202458844364830, # girl 2
        1092602287765074070 # moono
    )

    afk_users: dict = {}

    the_almighty_retucio_user_id: int = 806597513943056464

    fucking_idiots: tuple = (
        # 928719633660383292,  # quota
        1120699957415002212, # guest
        1311591141950488630  # idiotic fuckstick of lou
    )

    dildos: tuple = (
        1007985339278827610, # waldo my beloved
    )

    MAX_BALANCE = max(ITEMS.values()) * sum(1 / (i if i > 0 else 1) for i in (1,) + tuple(i * (i-1) for i in range(2, 20 + 1))) # set max balance to the highest price times euler's because why the fuck not

    @classmethod
    def toggle_logging(cls) -> None:
        cls.LOGGING_MESSAGES = not cls.LOGGING_MESSAGES


def is_peasant(member: discord.Member) -> bool:
    """make sure user has a bare minimum of three braincells."""
    return (
        member.id != SharedConstants.the_almighty_retucio_user_id and member.id not in SharedConstants.dildos and
        (member.id in SharedConstants.fucking_idiots or not member.guild_permissions.administrator)
    )

def has_prefix(message: discord.Message, prefix: str) -> bool:
    """better way to detect a prefix than just using `startswith()`."""
    return message.content.lower() == prefix or message.content.lower().startswith(prefix + " ")

async def send_message(message: discord.Message, content: str, message_to_reply: discord.Message = None, delete_after: int = None) -> None:
    """wrapper for the message.channel.send() function."""
    if len(content) > 1700:
        await send_message(message, "hell naw")
        return

    time_since_last_message = time.time() - SharedConstants.last_message_time
    if time_since_last_message < 0.2:
        await asyncio.sleep(0.2 - time_since_last_message)

    if message_to_reply:
        await message.reply(content)
    else:
        await message.channel.send(content, delete_after=delete_after if delete_after else None)
    SharedConstants.last_message_time = time.time()

def safe_eval(expression: str) -> float:
    """safely evaluate a mathematical expression. because my braindead ass thought it would be great idea to just handle math expressions with eval() without any sanitization."""
    if not re.match(r"^[0-9+\-*/^().\s]+$", expression):
        raise ValueError("that's not a math expression is it.")

    expression = re.sub(r"(^|(?<=\s))0+(?=\d)", "", expression) # strip zeros on the left because otherwise python thinks they're octal numbers
    expression = expression.replace("^", "**")

    try:
        result = eval(expression, {"__builtins__": None}, {})
        if not isinstance(result, (int, float)):
            raise ValueError("result is not a number.")
        return result
    except Exception:
        raise ValueError("invalid mathematical expression.")