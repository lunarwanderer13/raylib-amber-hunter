from pyray import *

class Timer:
    def __init__(self, time: float) -> None:
        self.start_time: float = time
        self.time: float = time

    def update(self) -> None:
        self.time -= get_frame_time()

    def reset(self) -> None:
        self.time = self.start_time
