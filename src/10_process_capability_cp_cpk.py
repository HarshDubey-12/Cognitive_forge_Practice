# Auto-generated from: 10_Process_Capability_Cp_Cpk.ipynb
# Run as a script or import functions from this module.

import numpy as np

np.random.seed(0)

process = np.random.normal(50,2,1000)
USL = 55
LSL = 45

mean = np.mean(process)
std = np.std(process)

Cp = (USL-LSL)/(6*std)
Cpk = min((USL-mean)/(3*std),(mean-LSL)/(3*std))

Cp, Cpk

print('Cp:', Cp, 'Cpk:', Cpk)

