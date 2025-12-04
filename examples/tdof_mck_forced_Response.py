# %%[markdown]
# # Scope
#
# This file is an example used to compare the results for a
# **TDOF** system using modal analysis.
#
#
# This notebook is to compare the results of the following
# https://www.youtube.com/watch?v=sqdd0ja1PXM&t=1s
# %%
import numpy as np
import scipy
import matplotlib.pyplot as plt

from np_vmd.misc import convert_harmonic_to_cos, convert_harmonic_to_sin

# from np_vmd.misc import HarmonicMotion
# TODO use HarmonicMotion class instead <- convert_harmonic_to_cos, convert_harmonic_to_sin
from np_vmd.sdof_funcs import SDOF_system
from np_vmd.tdof_MCK import TDOF_modal, MdofForcedResponseSingleExcitation

# %%
m1, m2 = 1000, 300
k1, k2 = 4e5, 5e5
c1, c2 = 2000, 2500
F1_N = 1000
w_Exc_radps = 30
tmck = TDOF_modal(
    np.array([[m1, 0], [0, m2]]),
    K=np.array([[k1, -k1], [-k1, k1 + k2]]),
    C=np.array([[c1, -c1], [-c1, c1 + c2]]),
)
tmck.set_iv(x0s=np.array([[0, 0]]).T, dx0s=np.array([[0, 0]]).T)
tmck.set_excitation(
    B=None,
    # B=np.array([[0,0],[0,1]]),
    F=None,
    Fparams=[(F1_N, w_Exc_radps, 0), (0, 0, 0)],
)
# %%

print("============Matrices")
print(tmck.mM)
print(tmck.mC)
print(tmck.mK)
# %%
print("============EigenValues and EigenVectors")
# step 2. (7:42)
print(f"eigenvalues      : {tmck.ls}")
print(f"eigenfrequencies : {tmck.wns}")
# step 3 (12:00)
# K adn Ktilde have different eigenvectors
Kl, kV = scipy.linalg.eig(tmck.mK, tmck.mM)
print(f"modeshapes   (from K - l M) :")
print(f"{kV}")
print(f"modeshapes   (from K~) :")
print(f" {tmck.vs}")

# Freemat
# M = [1000 0 ; 0 300];
# K = 100000*[4 -4; -4, 9];
# [v,l] = eig(K,M)
# v1 = v(:,1)
# v2 = v(:,2)

# %%
# %% Step 4.
print("============4. Pstar matrix")  # different notation
# step 2. (15:42)
print(f"S      :")
print(f" {tmck.Smat}")

# result for  Smat is      :
#  [[-0.03059288  0.00800473]
#  [-0.01461457 -0.0558547 ]]
# %% Step 5. ============================================
print("============5. Zs")  # different notation
# step 2. (15:42)
print(f"Z = Smat^T*C*Smat      :")
print(f" {tmck.zs}")
print(f" {tmck.Smat.T.dot(tmck.mC.dot(tmck.Smat))}")

# result for tmck.zs =  [0.03613476 0.14122421]
# result for  Z is      :
#  [[1.04457692e+00, 0.00000000e+00]
#  [5.55111512e-16, 1.59554231e+01]]
# %% Step 6.1 ============================================

# TODO create tests
print("============6.1 Fs")  # different notation


r_mdof = MdofForcedResponseSingleExcitation(
    mdof_sys=tmck, node=0, Fmag=F1_N, w_exc_radps=w_Exc_radps, phi_exc_rad=0
)


Fmag_pc = tmck.Smat.T.dot(tmck._f_params[:, 0])  # Fmagnitude in principal coordinates
w_exc = tmck._f_params[:, 1]  # Fmagnitude in principal coordinates
# step 2. (15:42)
print(f"F = Smat^T*F      :")
print(f" {Fmag_pc}")
print(f" {r_mdof.Fmag_pc}")

# result for =   [-30.5928797    8.00473059]
# %% Step 6.2 ============================================

# %%
lst_pc_decoupled_cs = []  # list of principal coordinate decoupled systems
lst_pc_response_params = []  # list of principal coordinate responses
lst_pc_response_funcs = []  # list of principal coordinate responses
for i in range(2):
    _tmpsys = SDOF_system.from_wn_mz(wn=tmck.wns[i], m=1, zeta=tmck.zs[i])
    _tmp_resp_parms = _tmpsys.response_params(x0=0, v0=0, F0=Fmag_pc[i], w=w_Exc_radps)
    lst_pc_decoupled_cs.append(_tmpsys)
    lst_pc_response_params.append(_tmp_resp_parms)
    lst_pc_response_funcs.append(_tmp_resp_parms.get("x_lambda"))
for i in range(2):
    print(f"Principal coordinate: {i + 1}======================")
    print(f"  - wn: {tmck.wns[i]:.3g}")
    print(f"  - z : {tmck.zs[i]:.3g}")
    print(f"  - F : {Fmag_pc[i]:.3g}")
    print(f"  Response:")
    print(
        f"           Xss: {lst_pc_response_params[i].get('Xss'):.3g} phi_ss: {lst_pc_response_params[i].get('phi_ss'):.3g}"
    )
    print(
        f"           Xtr: {lst_pc_response_params[i].get('X_tra'):.3g} phi_tr: {lst_pc_response_params[i].get('phi_tra'):.3g}"
    )
# %%
print("From new class<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
r_mdof.print_all_modal_responses(update=True)
# results are
# Principal coordinate: 1======================
#   - wn: 14.5
#   - z : 0.0361
#   - F : -30.6
#   Response:
#            Xss: -0.0442 phi_ss: 0.173
#            Xtr: 0.0469 phi_tr: 0.38
# Principal coordinate: 2======================
#   - wn: 56.5
#   - z : 0.141
#   - F : 8
#   Response:
#            Xss: 0.00342 phi_ss: 0.15
#            Xtr: 0.00347 phi_tr: -2.92
# %% Step 6.d ============================================
for j in range(2):
    print(lst_pc_response_params[j].get("form"))
# 0.046914*cos(14.454*t-0.38045) -0.044222*cos(30*t-0.17339)
# 0.0034652*cos(56.49*t+2.9213) +0.00342*cos(30*t-0.15028)
print("From new class<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(r_mdof.ith_modal_response_str(j=0, update=True))
print(r_mdof.ith_modal_response_str(j=1, update=True))
# ckech correctness of second frequency (its zero and I believe it hsould be 30)
# %% Step 7 ============================================

xs_pc = [x.get("Xss") for x in lst_pc_response_params]
phis_pc = [x.get("phi_ss") for x in lst_pc_response_params]
angle_2dArray = np.array([[np.cos(x), np.sin(x)] for x in phis_pc])
xs_mag_orig = tmck.Smat.dot(np.diag(xs_pc)).dot(angle_2dArray)

print(tmck.Smat)
# [[-0.03059288  0.00800473]
#  [-0.01461457 -0.0558547 ]]
print(xs_pc)
# [-0.044222480393594145, 0.003420017320299711]
print(phis_pc)
# [0.17339271361497388, 0.15028189271655545]
print(angle_2dArray)
# [[0.98500511, 0.17252518],
#  [0.98872891, 0.14971685]]
print(xs_mag_orig)
# [[1.35967429e-03, 2.37506803e-04],
#  [4.47730527e-04, 8.29022273e-05]]
print("From new class<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(r_mdof.xs_ABmag_orig)
# %%
# convert xs_mag_orig to X*cos(w*t+phi)
Xs = []
phis = []
for i in range(len(xs_mag_orig)):
    A = xs_mag_orig[i][0]
    B = xs_mag_orig[i][1]
    X, phi = convert_harmonic_to_cos(A, B)
    Xs.append(X)
    phis.append(phi)

x_cos_repr = np.column_stack([Xs, phis])  # Xcos representation
xs_mag_cos = np.array([[X * np.cos(phi), X * np.sin(phi)] for X, phi in zip(Xs, phis)])

print("============X*cos(w*t+phi)=========")
print(xs_mag_cos)
# ============X*cos(w*t+phi)=========
# [[ 1.35967429e-03 -2.37506803e-04]
#  [ 4.47730527e-04 -8.29022273e-05]]

# %% Step 8 ============================================
# convert each line of xs_mag_cos to lambda t:X*sin(w*t+phi)
# to get the response functions
lst = [lambda t: l[0] * np.cos(w_Exc_radps * t + l[1]) for l in xs_mag_cos]
lst[0](0)

# %%

ts = np.linspace(0, 10, 1000)
plt.plot(ts, r_mdof.jth_response_func(j=0)(ts), label="x1")
plt.plot(ts, r_mdof.jth_response_func(j=1)(ts), label="x2")
# plt.xlim(0,2)
# %%
# TODO There is a problem here: I might have more than one excitation.
# so the result should be superposition of responses for each excitation separately
#
# to me it seems that the solution to that is the following:
# - create a total response class that deals with one excitation
# - Create a class that deals with multiple excitations by delegating the work to
#   the total response class of 1 exciation
