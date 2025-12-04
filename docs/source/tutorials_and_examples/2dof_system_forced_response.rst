Analyzing a TDOF Vibrational System Using Python
================================================

Introduction
------------
This tutorial demonstrates how to analyze the forced response of a TDOF (Two Degrees of Freedom) vibrational system using Python. The analysis is carried out using two main classes: `TDOF_modal` and `MDOFResponse1Excitation`.

Prerequisites
-------------
- Python with NumPy and SciPy libraries.
- Basic understanding of mechanical vibrations and modal analysis.

Step 1: System Setup
--------------------
First, we import necessary libraries and define the system parameters.

.. code-block:: python

    import numpy as np
    import scipy
    from np_vmd.tdof_MCK import TDOF_modal, MDOFResponse1Excitation

    # Define system parameters
    m1, m2 = 1000, 300  # Masses
    k1, k2 = 4e5, 5e5  # Stiffnesses
    c1, c2 = 2000, 2500  # Damping coefficients
    F1_N = 1000  # Force amplitude
    w_Exc_radps = 30  # Excitation frequency in rad/s

    # Initialize TDOF system
    tmck = TDOF_modal(
        np.array([[m1, 0], [0, m2]]),
        K=np.array([[k1, -k1], [-k1, k1 + k2]]),
        C=np.array([[c1, -c1], [-c1, c1 + c2]])
    )
    tmck.set_iv(x0s=np.array([[0, 0]]).T, dx0s=np.array([[0, 0]]).T)
    tmck.set_excitation(
        B=None,
        F=None,
        Fparams=[(F1_N, w_Exc_radps, 0), (0, 0, 0)]
    )

Step 2: Eigenvalues and Eigenvectors
------------------------------------
Next, we calculate and print the eigenvalues and eigenvectors of the system.

.. code-block:: python

    # Eigenvalues and eigenvectors
    print("Eigenvalues and Eigenfrequencies:")
    print(f"Eigenvalues: {tmck.ls}")
    print(f"Eigenfrequencies: {tmck.wns}")

    # Using scipy to compute eigenvectors from K and M
    Kl, kV = scipy.linalg.eig(tmck.mK, tmck.mM)
    print("Modeshapes:")
    print(f"Modeshapes (from K - l M): {kV}")
    print(f"Modeshapes (from K~): {tmck.vs}")

Step 3: Setting up and calculating the system response
------------------------------------------------------
We then compute the response of the system under the given excitation.

.. code-block:: python

    r_mdof = MDOFResponse1Excitation(mdof_sys=tmck, node=0, Fmag=F1_N, w_exc_radps=w_Exc_radps, phi_exc_rad=0)

We can also provide (optionally) non zero initial conditions. (although the code currently does not support non zero initial conditions for the MDOF system)

.. code-block:: python

    r_mdof.set_iv(x0s=np.array([[0, 0]]).T, dx0s=np.array([[0, 0]]).T)

At this point we are ready to calculate the system response, (although this is optional, because whenever we call an output function there is an option to update the response)

.. code-block:: python

    r_mdof.calc_response()


Step 4: Viewing the system response
-----------------------------------

We can also provide non zero .

.. code-block:: python

    r_mdof.print_all_modal_responses(update=True)

We can also plot the tdof system forced system response.

.. code-block:: python

    # Plotting the system response
    import matplotlib.pyplot as plt
    ts = np.linspace(0, 10, 1000)
    plt.plot(ts, r_mdof.jth_response_func(j=0)(ts), label="x1")
    plt.plot(ts, r_mdof.jth_response_func(j=1)(ts), label="x2")
    plt.legend()
    plt.show()

Conclusion
----------
This tutorial walked you through the steps to analyze a TDOF vibrational system using Python. We explored system parameterization, eigenvalue analysis, and the system's response to external excitation.

Further Steps
-------------
- Explore different system parameters and their effects on the system's response.
- Implement additional features such as varying excitation frequencies and amplitudes.
