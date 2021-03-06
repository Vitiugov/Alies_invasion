class GameStats():
    """Статистика игры и рекорда"""
    
    def __init__(self, ai_settings):
        """Задаем Рекорд и перезагружаем уровень."""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0
        
    def reset_stats(self):
        """Инициализируем статистику, которая может изменяться в течении игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
