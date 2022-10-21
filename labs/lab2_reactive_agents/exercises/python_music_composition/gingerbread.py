
import platform
import sys
import time
import numpy as np


from classes import Agent, Composition, ID_START


class Gingerbread(Composition):
    def __init__(self, BPM=60):
        Composition.__init__(self, BPM=BPM)
        self.min = -3
        self.max = 8
        self.range = self.max-self.min
        # your code here
        self.stepDur = -0.1
        self.stepNote = 0.1
        self.Temp = 0

    def map(self, value_in, min_out, max_out):
        value_out = (value_in-self.min)/(self.range)
        value_out = min_out + value_out * (max_out-min_out)
        return np.clip(value_out, min_out, max_out)

    def next(self):
        # your code here
        self.amp = 1

        self.dur = self.map(self.stepDur, 0.5, 1)
        self.midinote = int(
            self.map(self.stepNote, 30, 90))
        self.Temp = self.stepDur
        self.stepDur = self.stepNote
        self.stepNote = 1-self.Temp+abs(self.stepNote)
        self.id += 1


if __name__ == "__main__":
    n_agents = 1
    composer = Gingerbread()
    agents = [_ for _ in range(n_agents)]
    agents[0] = Agent(57120, "/note_effect", composer)

    input("Press any key to start \n")
    for agent in agents:
        agent.start()
    try:  # USE CTRL+C to exit
        while True:
            time.sleep(10)
    except:
        for agent in agents:
            agent.kill()
            agent.join()
        sys.exit()

# %%
