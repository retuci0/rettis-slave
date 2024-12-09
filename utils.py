import discord

class SharedConstants:
    LOGGING_MESSAGES: bool = True
    
    females: tuple = (
        842116081241030717,
        820202458844364830,
        1092602287765074070
    )
    
    afk_users: dict = {}
    
    the_almighty_retucio_user_id: int = 806597513943056464
    
    fucking_idiots: tuple = (
        928719633660383292, # quota
        1120699957415002212 # guest
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
    return message.content == prefix or message.content.startswith(prefix + " ")