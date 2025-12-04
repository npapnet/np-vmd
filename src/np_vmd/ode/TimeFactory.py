import numpy as np
class TimeFactory():
    def __init__(self, tmax, dt):
        self.tmax = tmax
        self.dt = dt
        self.nt = int(tmax/dt) # Number of steps
        self.ti = np.linspace(0., self.nt * dt, self.nt)
        