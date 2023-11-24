import json

class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open("high_score.json", "w") as file:
            json.dump(self.high_score, file)

    def load_high_score(self):
        try:
            with open("high_score.json", "r") as file:
                self.high_score = json.load(file)
        except FileNotFoundError:
            self.high_score = 0