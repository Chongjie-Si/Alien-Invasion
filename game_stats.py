class GameStat:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        self.game_active = False
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0

        self.high_score = 0
