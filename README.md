# echemex
Scripts for processing experimental electrochemistry data

## Overview
This repository contains scripts that convert raw .DTA files from the experimental electrochemistry Gamry Framework software into `numpy` arrays for manipulation in Python.
Recommendations and requests for additional functionality are welcome and appreciated.

## Installation
Running the following in a terminal should install directly from github.
```console
pip3 install git+https://github.com/miuev/echemex@main
```
Another option is to clone the remote repository locally, change to that directory, and then run `pip install .`.

## Usage
The scripts are meant to facilitate data analysis in a digital laboratory notebook.
A Jupyter notebook, for example, is a well-suited way to use this package.
This approach allows for flexibility in tuning figure outputs and allows for additional manipulations on top of the base package.
Once `echemex` is installed, the tools can be imported with `proc.py`.

```python
from echemex import proc
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
V, I, scan_rate, n_cycles = proc.readcv(file, cycle, E_ref, area)
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
Scripts return data in the following units: Volts in V vs. Ref, current in mA, current density in mA/cm<sup>2</sup>, and time in seconds.
