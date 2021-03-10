import time
from collections import deque


class FPS:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time_list = deque(maxlen=15)
        self.speed_list = deque(maxlen=16) # added

    def start(self):
        self.start_time = time.perf_counter()
        return self

    def stop(self):
        end_time = time.perf_counter()
        self.elapsed_time_list.append(end_time - self.start_time)
        self.speed_list.append(1/(end_time - self.start_time)) # added

    def get_average_time(self):
        average_time = sum(self.elapsed_time_list) / len(self.elapsed_time_list)
        return average_time

    def get_fps(self):
        fps = 1 / self.get_average_time()
        fps_new = sum(self.speed_list) / len(self.speed_list) #added
        #return fps
        return fps_new
