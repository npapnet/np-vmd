Title: Two-Degree-of-Freedom Harmonic Oscillator Using Sympy
============================================================

This tutorial demonstrates how to solve a two-degree-of-freedom harmonic 
oscillator problem using SymPy, a Python library for symbolic mathematics.

We will use the Laplace transform to solve the system's equations of motion.

Step 1: Introduction to the Problem
-----------------------------------

The equations of motion for a two-degree-of-freedom system can be written as:

.. math::

   \mathbf{M_{mat}}\ddot{\mathbf{x}} + \mathbf{C_{mat}}\dot{\mathbf{x}} + \mathbf{K_{mat}}\mathbf{x} = \mathbf{F}

Where:

- :math:`\mathbf{M_{mat}}` is the mass matrix, 
- :math:`\mathbf{C_{mat}}` is the damping matrix, 
- :math:`\mathbf{K_{mat}}` is the stiffness matrix, and 
- :math:`\mathbf{F}` is the force vector.

Step 2: Setting Up the Environment
----------------------------------

the first step is:

- importing the necessary libraries and also
- defining the physical parameters of the system.


.. code-block:: python

   import sympy as sp
   import matplotlib.pyplot as plt

   m1, m2, c1, c2, k1, k2 = 9, 1, 2, 2, 24, 3
   F1 = 10
   w1_exc = 0.5

Step 3: Defining the Equations of Motion
----------------------------------------

In the next step we need to define the equation of the system.
Sympy's symbolic variables are used to define the equations of motion.

Notice how:

- the `sp.Function` class is use to define the dependent variables :math:`x_1(t)` and :math:`x_2(t)`.
- How derivatives are defined using the `diff` method. For example, :math:`\dot{x_1(t)}` is defined as :code:`x1(t).diff(t)`.	

After that we define the equations of motion using the `sp.Eq` class.

.. math:: 
    
   \ddot{x_1(t)} + \frac{1}{m_1} \left( (c_1+c_2)\dot{x_1(t)} - c_2\dot{x_2(t)} + (k_1+k_2)x_1(t) - k_2x_2(t) - F_1\sin(w_1t) \right) = 0

   \ddot{x_2(t)} + \frac{1}{m_2} \left( -c_2\dot{x_1(t)} + c_2\dot{x_2(t)} - k_2x_1(t) + k_2x_2(t) \right) = 0

.. code-block:: python

   t, s = sp.symbols('t s')
   x1 = sp.Function('x1')
   x2 = sp.Function('x2')

   diff_eq1 = sp.Eq(x1(t).diff(t, 2) + 1/m1*( (c1+c2)*x1(t).diff(t) - c2*x2(t).diff(t)  + (k1+k2)*x1(t) - k2*x2(t) - F1*sp.sin(w1_exc*t)), 0)
   diff_eq2 = sp.Eq(x2(t).diff(t, 2) + 1/m2*(    -c2 *x1(t).diff(t) + c2*x2(t).diff(t)  -      k2*x1(t) + k2*x2(t)), 0)

Step 4. Applying Initial Conditions
-----------------------------------

This is one of the  most important steps in solving differential equations and arriving 
at a numerical result, i.e. the setup of initial conditions.

Initial conditions are the values of the dependent variables and their derivatives at a given time.

In sympy it is possible to define them because we already defined 
the dependent variables and (indirectly) their derivatives. See below

.. code-block:: python

   initial_conditions = {x1(0)                   :  1, 
                         x1(t).diff(t).subs(t, 0): 0,
                         x2(0)                   :  3, 
                         x2(t).diff(t).subs(t, 0): 0}

.. note:: The selection of initial conditions

   The selection of the initial conditions is that of a mode-shape, and the system will have a very predicable response.
   the other modeshape is :math:`[\frac{-1}{3},-1]`. Any other combination will produce a linear combination (superposition) of 
   the two modeshapes at different weights.

Step 4. Utilizing the Laplace Transform
---------------------------------------

The Laplace transform is a mathematical tool that converts differential equations to algebraic equations for easier solving.

In sympy the Laplace transform is defined using the `sp.laplace_transform` function.

.. note::
   
   The `noconds=True` argument is used to return only the algebraic equation, without the conditions.

.. code-block:: python

   lap_eq1 = sp.laplace_transform(diff_eq1.lhs - diff_eq1.rhs, t, s, noconds=True)
   lap_eq2 = sp.laplace_transform(diff_eq2.lhs - diff_eq2.rhs, t, s, noconds=True)

Step 5. Solving the System of Equations
---------------------------------------

The next step is to solve the algebraic system obtained from the Laplace transform using SymPy’s `linsolve` function.

.. code-block:: python

   laplace_sols = sp.linsolve([lap_eq1.subs(initial_conditions), lap_eq2.subs(initial_conditions), s, noconds=True)


Step 6: Applying the Inverse Laplace Transform
----------------------------------------------

To revert the solutions back to the time domain the  inverse Laplace transform :code:`sp.inverse_laplace_transform` is used.

.. code-block:: python

   sol = [sp.inverse_laplace_transform(eq, s, t)  for eq in laplace_sols.args[0]]

Step 7: Extracting and Plotting the Solutions
---------------------------------------------

The solutions for :math:`x_1(t)` and :math:`x_2(t)` are ready now
to be extracted and then plotted them using sympy or matplotlib.

.. code-block:: python

   x1_solution = sol[0].subs(initial_conditions)
   x2_solution = sol[1].subs(initial_conditions)

   p = sp.plot(x1_solution, x2_solution, (t, 0, 30), show=False)
   p[0].line_color = 'blue'
   p[1].line_color = 'red'
   p.title = 'Solutions of x1(t) and x2(t)'
   p.xlabel = 't'
   p.ylabel = 'Functions'
   p.show()

Complete Code
-------------

Provide the entire script as a single block for reference and ease of use.

.. code-block:: python

   #%% [imports]
   import sympy as sp
   import matplotlib.pyplot as plt

   # Define constants and variables
   m1, m2, c1, c2, k1, k2 = 9, 1, 2, 2, 24, 3
   F1 = 10
   w1_exc = 0.5
   t, s = sp.symbols('t s')
   # x1, x2 = sp.symbols('x1 x2', cls=sp.Function) # alternative syntax
   x1 = sp.Function('x1')
   x2 = sp.Function('x2')
   # Differential equations
   diff_eq1 = sp.Eq(x1(t).diff(t, 2) + 1/m1*( (c1+c2)*x1(t).diff(t) - c2*x2(t).diff(t)  + (k1+k2)*x1(t) - k2*x2(t) - F1*sp.sin(w1_exc*t)), 0)
   diff_eq2 = sp.Eq(x2(t).diff(t, 2) + 1/m2*(    -c2 *x1(t).diff(t) + c2*x2(t).diff(t)  -      k2*x1(t) + k2*x2(t)), 0)
   #%%
   # Initial conditions
   initial_conditions = {x1(0):  1, x1(t).diff(t).subs(t, 0): 0,
                        x2(0):  3, x2(t).diff(t).subs(t, 0): 0}
   #%%
   # Laplace transform
   lap_eq1 = sp.laplace_transform(diff_eq1.lhs - diff_eq1.rhs, t, s, noconds=True)
   lap_eq2 = sp.laplace_transform(diff_eq2.lhs - diff_eq2.rhs, t, s, noconds=True)
   #%%
   # Solve the linear system
   # laplace_sols = sp.linsolve([lap_eq1, lap_eq2], sp.laplace_transform(x1(t), t, s, noconds=True),
                                             # sp.laplace_transform(x2(t), t, s, noconds=True))
   laplace_sols = sp.linsolve([lap_eq1.subs(initial_conditions), lap_eq2.subs(initial_conditions)], sp.laplace_transform(x1(t), t, s, noconds=True),
                                             sp.laplace_transform(x2(t), t, s, noconds=True))
   laplace_sols 
   sol = [sp.inverse_laplace_transform(eq, s, t)  for eq in laplace_sols.args[0]]
   #%%
   # Extracting the solutions
   x1_solution = sol[0].subs(initial_conditions)
   x2_solution = sol[1].subs(initial_conditions)
   #%%
   # Plotting the solutions
   p = sp.plot(x1_solution, x2_solution, (t, 00, 30), show=False)
   p[0].line_color = 'blue'
   p[1].line_color = 'red'
   p.title = 'Solutions of x1(t) and x2(t)'
   p.xlabel = 't'
   p.ylabel = 'Functions'
   # p.legend = True
   p.show()

Conclusion
----------

This tutorial demonstrated how to solve a two-degree-of-freedom harmonic oscillator problem using SymPy, a Python library for symbolic mathematics.

A two-degree-of-freedom system is a system with damping, forced excitation and initial conditions case is examined, and
easily we can do:

- free vibrations with damping
- forced vibrations with no damping, starting from rest (no initial conditions)
- forced vibrations with damping, starting from rest (no initial conditions)
- forced vibrations with damping, with  initial conditions 

The final case examined in this tutorial (which is also the most generic). 

