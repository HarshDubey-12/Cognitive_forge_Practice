"""Compute process capability indices Cp and Cpk."""
import numpy as np


def compute_cp_cpk(process, USL=55, LSL=45):
    mean = np.mean(process)
    std = np.std(process, ddof=0)
    Cp = (USL - LSL) / (6 * std)
    Cpk = min((USL - mean) / (3 * std), (mean - LSL) / (3 * std))
    return Cp, Cpk


if __name__ == "__main__":
    np.random.seed(0)
    process = np.random.normal(50, 2, 1000)
    Cp, Cpk = compute_cp_cpk(process)
    print("Cp:", Cp, "Cpk:", Cpk)
