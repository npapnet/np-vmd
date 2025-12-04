# Machine Dynamics and Vibrations 

This is a package for helping with the lecture of npapnet at the Mechanical Engineering department. 

Contains code for:

- SDOF system
  - Free response
    - Undamped
    - Damped
  - Forced HArmonic response
    - Undamped
    - Damped 
- TDOF systems
- MDOF systems

# Usage

## installation

Navigate to the folder of the pypkg and use

> python -m pip install --editable .


**Do not use** the deprecated `python setup.py develop`.

# TODO 

Issues:
- 20240116: [ ] update rst documentation with new configuration of tdof_mck and the response classes. 
- 20240116: [ ] Inman: check forced response of system (no iv)
- 20240116: [ ] Inman: check forced response of system (with iv)
- 20240116: [ ] Gagnon: check forced response of system (single excitation - with iv)
- 20240116: [ ] Gagnon: check forced response of system (only iv - no excitation) 
- 20240116: [ ] Gagnon: check forced response of system (only iv - multipleexcitation)

## History 
- 20240116: [x] Inman: check free response of system
- 20240116: [X] Gagnon: check forced response of system (single excitation - no iv)
