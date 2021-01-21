# echemex
Scripts for processing experimental electrochemistry data

## Overview
This repository contains scripts that convert raw .DTA files from the experimental electrochemistry Gamry Framework software into `numpy` arrays for manipulation in Python.
Currently, only cyclic voltammetry experiments can be converted, but chronoamperometry, chronopotentiometry, electrochemical impedance spectroscopy, linear sweep voltammetry, and other experimental techniques will shortly be included. 
Recommendations and requests for additional functionality are welcome and appreciated.

## Usage
The script can be imported and run in most any Python-aware environment.
A Jupyter notebook, for example, is a well-suited way to use this package.
This approach allows for flexibility in tuning figure outputs and allows for additional manipulations on top of the base package.
Once `echemex` is installed in an appropriate location in PYTHONPATH, it can be imported as normal.

```python
import echemex
```

Relevant experimental files can be pulled in via the appropriate script.
For example, `readcv` is used for reading cyclic voltammetry (CV) data files.
The filepath to the data, cycle number, reference electrode potential, and electrode surface area are all needed as inputs to properly scale and interpret the data.
Outputs are the potential (referenced to the supplied potential), the current density in mA/cm<sup>2</sup>, the scan rate, and the number of cycles. 

```python
file = '/path/to/data.DTA'
cycle = -1 # desired cycle number for plotting, -1 gives all
E_ref = 0 # potential of reference electrode in V, if 0, left to experimental reference
area = 1 # area in cm^2
V, I, scan_rate, n_cycles = echemex.readcv(file, cycle, E_ref, area)
```

After running and populating the `V` and `I` variables, visualization packages such as `matplotlib` and `seaborn` can be used to plot the data.
Below is an example code snippet using `matplotlib`.

```python
import matplotlib.pyplot as plt
```

```python
plt.figure()
plt.plot(V,I,label='The Data')
plt.axhline(y=0)
plt.xlabel('V vs. Ref')
plt.ylabel('j [mA/cm$^2$]')
plt.legend()
```
Units are output as follows: Volts in V vs. Ref, current in mA, current density in mA/cm<sup>2</sup>.
