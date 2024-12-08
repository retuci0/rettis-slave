class SharedConstants:
    LOGGING_MESSAGES: bool = True
    females = (
        842116081241030717,
        820202458844364830,
        1092602287765074070
    )
    afk_users = {}
    
    fucking_idiots = (
        928719633660383292, # quota
        1120699957415002212 # guest
    )
    
    @classmethod
    def toggle_logging(cls):
        cls.LOGGING_MESSAGES = not cls.LOGGING_MESSAGES