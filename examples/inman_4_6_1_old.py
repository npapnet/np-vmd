#%%
import numpy as np
import matplotlib.pyplot as plt
from np_vmd.tdof_MCK import TDOF_modal

# examples 4.6.1.
''' With damping and forced
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


# tmck.update_damping( np.array([0.1, 0.05]))
print(tmck.zs)
# print(tmck.wns)

print(tmck.Ctilde)
print(tmck.Ktilde)


# %%
Z=np.diag(tmck.zs)
tmck.Pmat.T.dot(tmck.Ctilde).dot(tmck.Pmat)
# %%
tmck.calc_C_from_Z(tmck.zs).mC
# %%

# %%
