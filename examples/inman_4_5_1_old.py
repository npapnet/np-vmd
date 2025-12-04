#%%[markdown]
# # Inman 4.5.1
#  this is based on the example 4.5.1 from Inman's book
# the example is a 2 DOF system with damping

# - a TDOF_modal object is defined
# - the initial conditions are set
# - the damping is updated
# - the Free response (homogeneous solution) is calculated ()
# - the damping ratios (zetas) are printed
# - the mode shapes are printed
# - the response is plotted


#%%
import numpy as np
import matplotlib.pyplot as plt
from np_vmd.tdof_MCK import TDOF_modal

# examples 4.5.1.
''' With damping
'''
m1,m2  = 9,1
k1=24
k2=3
c1 = 2.4
c2 = 0.3
tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))

# ================== FOrce excitation ============
# print(tmck.Linv)
# calculate B tilde
tmck.set_iv(x0s = np.array([[1, 0]]).T, dx0s = np.array([[0,0]]).T)

print(tmck.Ktilde)
tmck.update_damping( np.array([0.1, 0.05]))
print(tmck.zs)
print(tmck.wns)



ts = np.linspace(0, 50, 1000)
xs = tmck.calc_x_hom_response(ts)

plt.plot(ts, xs[0,:], label = 'x_1')
plt.plot(ts, xs[1,:], label = 'x_2')
plt.legend
plt.show()
# print(tmck.calc_C_from_Z(np.diag([0.1, 0.05])).mC)
# %%
tmck.zs
a = tmck.calc_C_from_Z(np.diag([0.1,0.05]))
print (a.mC)
# %%
# examples 4.5.1.
''' With damping and forced
'''
m1,m2  = 9,1
k1=24
k2=3
c1 = 0.6
c2 = 0.075
tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))

# ================== FOrce excitation ============
# print(tmck.Linv)
# calculate B tilde
tmck.set_iv(x0s = np.array([[1, 0]]).T, dx0s = np.array([[0,0]]).T)

print(tmck.zs)

ts = np.linspace(0, 50, 1000)
xs = tmck.calc_x_hom_response(ts)

plt.plot(ts, xs[0,:], label = 'x_1')
plt.plot(ts, xs[1,:], label = 'x_2')
plt.show()
# %%  [markdown]
# # checking results
m1,m2  = 9,1
k1=24
k2=3
c1 = 2.4
c2 = 0.3
tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))
print(tmck.zs)

print(tmck.calc_C_from_Z(np.diag(tmck.zs)).mC)
# %%