import numpy as np
from scipy.optimize import curve_fit

def fit_function(energy, A, b):
    return A * (1 - np.exp(-b * energy))


def get_A_b_params(ore):
    model_predict = []
    params, _ = curve_fit(fit_function, ore.energy, ore.t10,maxfev=5000)
    
    A, b = params
    model_predict.append((A, b))
    energy_fit = np.linspace(min(ore.energy), max(ore.energy), 100)
    t10_fit = fit_function(energy_fit, A, b)
    return A, b