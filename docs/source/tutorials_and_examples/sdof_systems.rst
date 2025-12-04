SDOF Systems
============

The SDOF (Single Degree of Freedom) systems module in [Your Package Name] allows for the analysis of systems with a single degree of freedom. This section provides a guide on using the SDOF systems module, including quick examples and detailed tutorials.

Quick Examples
--------------

To get a feel for how the SDOF systems module works, here are a few quick examples.

Example 1: Basic Usage
^^^^^^^^^^^^^^^^^^^^^^

Import the basic sdof module and numpy and plotting capabilities

.. code-block:: python

    import np_vmd.sdof_funcs as sdof_funcs
    import numpy as np
    import matplotlib.pyplot as plt

Define a system SDOF system with

- m = 10 kg
- c = 50 kg/s
- k = 1000 N/m

and print the system properties.

.. code-block:: python

    sysA = sdof_funcs.SDOF_system(m=10,c=50, k=1000)
    print(f"----- System Parameters --------")
    print(f"wn     :  {sysA.wn}")
    print(f"zeta   :  {sysA.zeta}")
    print(f"wd     :  {sysA.wd}")
    print(f"T      :  {sysA.T}")
    print(f"Td     :  {sysA.Td}")



Example 2: calculate the Free Response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Continuing from above:

- define a time vector t  
- obtain the free response (displacement) 
- plot the free response

.. code-block:: python

    t = np.linspace (0, 3*sysA.T, 1000)
    fdic = sysA.free_response_at_t_funcs(x0=0.1, v0=1)

    # Plotting example
    plt.figure(figsize=(12,5))
    plt.plot(t, fdic['x'](t))
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.grid()

For plotting the velocity respone:

- plot the free response using the fdic obtained above. 

.. code-block:: python

    # Plotting velocity example
    plt.figure(figsize=(12,5))
    plt.plot(t, fdic['v'](t))
    plt.xlabel('t [s]')
    plt.ylabel('v [m/s]')
    plt.grid()


For a more detailed guide on using the SDOF module, please refer to the following tutorials.

Detailed Tutorials
------------------

Here we walk through detailed examples of common analyses you can perform with the SDOF module.

Example 1: Detailed Analysis of an SDOF System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Detailed tutorial content

