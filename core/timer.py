import threading
import time

class Timer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Timer, cls).__new__(cls)
            cls._instance._observers = []
            cls._instance._timer_thread = None
            cls._instance._running = False
        return cls._instance

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for obs in self._observers:
            obs.time_up()

    def start(self, seconds):
        self._running = True
        def run():
            time.sleep(seconds)
            if self._running:
                self.notify_observers()
        self._timer_thread = threading.Thread(target=run)
        self._timer_thread.start()

    def stop(self):
        self._running = False
        if self._timer_thread:
            self._timer_thread.join() 