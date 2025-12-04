# %% [markdown]
# This is code related to a mass spring system example  from RAo 6th edition
# This involves examples:
# - 5.1 Find the natural frequencies and mode shapes of a spring-mass system
#
# %%
import numpy as np
import matplotlib.pyplot as plt
from np_vmd.tdof_MCK import TDOF_modal

# # examples 4.5.1.
# ''' With damping
# '''
# m1,m2  = 9,1
# k1=24
# k2=3
# c1 = 2.4
# c2 = 0.3
# Mmat = np.array([[m1,0],[0,m2]])
# Kmat = np.array([[k1+k2,-k2],[-k2,k2]])
# Cmat =  np.array([[c1+c2,-c2],[-c2,c2]])
# tmck = TDOF_modal(Mmat, K=Kmat, C=Cmat)

# # ================== FOrce excitation ============
# # print(tmck.Linv)
# # calculate B tilde
# tmck.set_iv(x0s = np.array([[1, 0]]).T, dx0s = np.array([[0,0]]).T)

# print(tmck.Ktilde)
# tmck.update_damping( np.array([0.1, 0.05]))
# print(tmck.zs)
# print(tmck.wns)


# ts = np.linspace(0, 50, 1000) # time vector
# xs = tmck.calc_x_hom_response(ts) # positions

# fig, axs = plt.subplots(2,1, sharex=True, sharey=True)
# axs[0].plot(ts, xs[0,:], label = 'x_1')
# axs[1].plot(ts, xs[1,:], label = 'x_2')
# axs[0].legend()
# axs[1].legend()
# plt.xlabel('time [s]')
# axs[0].set_ylabel('$x_1$')
# axs[1].set_ylabel('$x_2$')
# plt.show()
# #%%
# # print(tmck.calc_C_from_Z(np.diag([0.1, 0.05])).mC)
# # %%
# # tmck.zs
# # a = tmck.calc_C_from_Z(np.diag([0.1,0.05]))
# # print (a.mC)
# # %%
# # # examples 4.5.1.
# # ''' With damping and forced
# # '''
# # m1,m2  = 9,1
# # k1=24
# # k2=3
# # c1 = 0.6
# # c2 = 0.075
# # tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))

# # # ================== FOrce excitation ============
# # # print(tmck.Linv)
# # # calculate B tilde
# # tmck.set_iv(x0s = np.array([[1, 0]]).T, dx0s = np.array([[0,0]]).T)

# # print(tmck.zs)

# # ts = np.linspace(0, 50, 1000)
# # xs = tmck.calc_x_hom_response(ts)

# # plt.plot(ts, xs[0,:], label = 'x_1')
# # plt.plot(ts, xs[1,:], label = 'x_2')
# # plt.show()
# # # %%  [markdown]
# # # # checking results
# # m1,m2  = 9,1
# # k1=24
# # k2=3
# # c1 = 2.4
# # c2 = 0.3
# # tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))
# # print(tmck.zs)

# # print(tmck.calc_C_from_Z(np.diag(tmck.zs)).mC)
# # # %%
# # %%
import sympy as sp

# e x a m p l e 5.3 rao p523
m, k, w = sp.symbols("m k w")
# %%
m1 = 10
m2 = 1
k1 = 30
k2 = 5
k3 = 0
Mmat = sp.Matrix([[m1, 0], [0, m2]])
Kmat = sp.Matrix([[k1 + k2, -k2], [-k2, k2 + k3]])
# %%
eig_prob = -(w**2) * Mmat + Kmat
# %%

w1 = sp.solve(list(eig_prob.eigenvals().keys())[0], w)
w2 = sp.solve(list(eig_prob.eigenvals().keys())[1], w)
# %%
print(w1)
# %%
m, k, w = sp.symbols("m k w")

# %%
