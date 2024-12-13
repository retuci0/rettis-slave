import asyncio
import discord
import time

class SharedConstants:
    LOGGING_MESSAGES: bool = True
    
    last_message_time = 0
    
    females: tuple = (
        842116081241030717, # girl 1
        820202458844364830, # girl 2
        1092602287765074070 # moono
    )
    
    afk_users: dict = {}
    
    the_almighty_retucio_user_id: int = 806597513943056464
    
    fucking_idiots: tuple = (
        928719633660383292,  # quota
        1120699957415002212, # guest
        1311591141950488630  # idiotic fuckstick of lou
    )
    
    @classmethod
    def toggle_logging(cls) -> None:
        cls.LOGGING_MESSAGES = not cls.LOGGING_MESSAGES


def is_peasant(member: discord.Member) -> bool:
    """make sure user has a bare minimum of three braincells."""
    return (
        member.id != SharedConstants.the_almighty_retucio_user_id and
        (member.id in SharedConstants.fucking_idiots or not member.guild_permissions.administrator)
    )

def has_prefix(message: discord.Message, prefix: str) -> None:
    """better way to detect a prefix than just using `startswith()`."""
    return message.content == prefix or message.content.startswith(prefix + " ")

async def send_message(message: discord.Message, content: str):
    """Wrapper for the message.channel.send() function with rate limit prevention."""
    if len(content) > 1500:
        await send_message(message, "hell naw")
        return

    time_since_last_message = time.time() - SharedConstants.last_message_time
    if time_since_last_message < 0.2:
        await asyncio.sleep(0.2 - time_since_last_message)

    await message.channel.send(content)
    SharedConstants.last_message_time = time.time()