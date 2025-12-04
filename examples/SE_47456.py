#%%
import numpy as np
import matplotlib.pyplot as plt
from np_vmd.tdof_MCK import TDOF_modal
from numpy.linalg import eig

# examples 4.2.6
''' With out damping
'''
m1,m2  = 1,1
k1=k3=10
k2=10
c1 = 0
c2 = 0
tmck = TDOF_modal(np.array([[m1,0],[0,m2]]), K=np.array([[k1+k2,-k2],[-k2,k2+k3]]), C= np.array([[c1+c2,-c2],[-c2,c2]]))
#%%

modes = tmck.Smat
# print(tmck.Linv)
# calculate B tilde
eig_mode1= modes[:,0].reshape(2,1) # eigenmode 1
eig_mode1=  modes[:,1].reshape(2,1) # eigenmode 2

tmck.set_iv(x0s = eig_mode1,# np.array([[x1_0, x2_0]]).T, 
        dx0s = np.array([[0,0]]).T)

print(tmck.Ktilde)
# tmck.update_damping( np.array([0.1, 0.05]))
print(tmck.zs)
print(tmck.wns)



ts = np.linspace(0, 10, 1000)
xs = tmck.calc_x_hom_response(ts)

plt.plot(ts, xs[0,:], '.',label = 'x_1')
plt.plot(ts, xs[1,:], label = 'x_2')
plt.xlabel('time [s]')
plt.ylabel('Displacement [m]')
plt.show()
# print(tmck.calc_C_from_Z(np.diag([0.1, 0.05])).mC)



# %%
