
import sys
import time


from classes import Agent, Composition, ID_START


class Simple_Next(Composition):
    def __init__(self, BPM=60):
        Composition.__init__(self, BPM=BPM)
        self.nodeId = 60
        self.direction = -1

    def next(self):
        pass
        if (self.id == ID_START):
            self.id = 0
            self.midinote = self.nodeId
            self.dur = 1
            self.amp = 1

        if self.nodeId == 60 or self.nodeId == 84:
            self.direction *= -1

        self.midinote = self.nodeId
        self.nodeId += self.direction
        self.id += 1

        if self.id == 48:
            self.id = 0

        # your code here


if __name__ == "__main__":
    n_agents = 1
    composer = Simple_Next()
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
