History
=======



TODO List
=========

Scope
------------
This document outlines the proposed improvements to the `tdof_mck_forced_Response.py` example. These improvements aim to enhance the handling of harmonic motion and the response to multiple excitations in a two-degree-of-freedom (TDOF) mechanical system.

Improvement 1: Using HarmonicMotion Class
-----------------------------------------
**TODO**: Replace `convert_harmonic_to_cos` and `convert_harmonic_to_sin` functions with the `HarmonicMotion` class for more efficient and accurate harmonic motion handling.

.. code-block:: python

    # Current Implementation
    from np_vmd.misc import convert_harmonic_to_cos, convert_harmonic_to_sin

    # Proposed Implementation
    from np_vmd.misc import HarmonicMotion
    # Code demonstrating the use of HarmonicMotion class

Improvement 2: Handling Multiple Excitations
--------------------------------------------
**TODO**: Address the issue of a system having more than one excitation. The response should be a superposition of responses for each excitation separately.

Proposed Solution:

1. Create a `TotalResponse` class that handles the response of the system to a single excitation.

2. Create a `MultiExcitationResponse` class that manages multiple excitations by delegating the work to the `TotalResponse` class for each excitation.

.. code-block:: python

    # Example of the TotalResponse class
    class TotalResponse:
        def __init__(self, ...):
            # Initialization code

    # Example of the MultiExcitationResponse class
    class MultiExcitationResponse:
        def __init__(self, ...):
            # Initialization code

Conclusion
----------
Implementing these improvements will enhance the capabilities of the TDOF system analysis by providing more robust handling of harmonic motion and accommodating multiple excitations effectively.

Further Work
------------
- Implement and test the `HarmonicMotion` class in the context of the TDOF system.
- Develop and validate the `TotalResponse` and `MultiExcitationResponse` classes.
