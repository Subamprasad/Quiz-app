class Observer:
    def time_up(self):
        raise NotImplementedError

class QuizObserver(Observer):
    def __init__(self, on_time_up_callback):
        self.on_time_up_callback = on_time_up_callback

    def time_up(self):
        self.on_time_up_callback() 