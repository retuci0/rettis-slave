class SharedConstants:
    LOGGING_MESSAGES: bool = True
    females = (
        842116081241030717,
        820202458844364830,
        1092602287765074070
    )
    afk_users = {}
    
    @classmethod
    def toggle_logging(cls):
        cls.LOGGING_MESSAGES = not cls.LOGGING_MESSAGES