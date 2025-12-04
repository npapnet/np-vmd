#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy import signal

## This class has migrated from math.solver.ode.py

class SolverFactory():

    def __init__(self):
        pass

    def Euler(self, func, X0, t):
        dt = t[1] - t[0]
        nt = len(t)
        X  = np.zeros([nt, len(X0)])
        X[0] = X0
        for i in range(nt-1):
            X[i+1] = X[i] + func(X[i], t[i]) * dt
        return X

    def RK4(self, func, X0, t):
        ''' solve Initial value problem with RK4

        func over time t with in
        '''
        dt = t[1] - t[0]
        nt = len(t)
        X  = np.zeros([nt, len(X0)])
        X[0] = X0
        for i in range(nt-1):
            k1 = func(X[i], t[i])
            k2 = func(X[i] + dt/2. * k1, t[i] + dt/2.)
            k3 = func(X[i] + dt/2. * k2, t[i] + dt/2.)
            k4 = func(X[i] + dt    * k3, t[i] + dt)
            X[i+1] = X[i] + dt / 6. * (k1 + 2. * k2 + 2. * k3 + k4)
        return X

    def w_odeint(self, func, X0, t):
        ''' solve Initial value problem with odeint

        func over time t with in
        '''
        X_odeint = integrate.odeint(func, X0, t)
        # %time x_odeint, y_odeint = X_odeint[:,0], X_rk4[:,1]
        x_odeint, y_odeint = X_odeint[:,0], X_odeint[:,1]
        return X_odeint
    
    def ss_lsim(self, t, u, A, B, C, D, X0 ):
        """ State representation Solution : requires signal 

        Args:
            t ([type]): time array 
            u ([type]): array with intensity of external stimulus 
            A (n x n): A matrix (\dot{X} = A*X+ B*u)
            B (n x 1): B  matrix (\dot{X} = A*X+ B*u)
            C (1 x m):  matrix (Y = C*X+ D*U)
            D (1 x 1):  matrix (Y = C*X+ D*U)
            X0 ([type]): Initial conditions

        Returns:
            [type]: (time, response, states)
        """    
        # (2) State Space
        sys2 = signal.StateSpace(A,B,C,D)
        # sys2 = signal.lti(A,B,C,D)

        tout, yout, xout = signal.lsim2(sys2, U=u, T=t, X0=X0)
        # plt.plot(xout[:,0],xout[:,2],'.')
        return (tout, yout, xout)

    def plotEuler(self, func, X0, t):
        res = self.Euler(func, X0, t)
        plt.plot(res[:,0],res[:,1],'.', label='Euler')

    def plotRK4(self, func, X0, t):
        res = self.RK4(func, X0, t)
        plt.plot(res[:,0],res[:,1],'.', label='RK4')

    def plotOdeint(self, func, X0, t):
        res = self.w_odeint(func, X0, t)
        plt.plot(res[:,0],res[:,1],'.', label='odeint')

# %%
