class ScoreManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScoreManager, cls).__new__(cls)
            cls._instance.score = 0
        return cls._instance

    def add(self, points):
        self.score += points

    def reset(self):
        self.score = 0

    def get_score(self):
        return self.score 