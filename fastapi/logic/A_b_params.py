import numpy as np
from scipy.optimize import curve_fit
from dataclasses import dataclass
def fit_function(energy, A, b):
    return A * (1 - np.exp(-b * energy))
@dataclass
class DWT_RESULT:
    energy: list[float]
    t10: list[float]
    SG: float

def get_A_b_params(ore):
    model_predict = []
    params, _ = curve_fit(fit_function, ore.energy, ore.t10,maxfev=5000)
    
    A, b = params
    model_predict.append((A, b))
    energy_fit = np.linspace(min(ore.energy), max(ore.energy), 100)
    t10_fit = fit_function(energy_fit, A, b)
    return A, b


def get_A_b_params_dwt(ore):
    return 1, 2

def get_ore_params(retentions, energies, sizes, SG):

    sizes_10 = [size[0] / 10 for size in sizes] 

    retentions = retentions.transpose(1,0, 2)
    retentions_at_t10 = DWT_RESULT(energy=[], t10=[], SG=SG)

    for target_size, size_list, retention_list, energy_list in zip(sizes_10, sizes, retentions, energies):
        for energy, retention in zip(energy_list, retention_list):
            print(f"{energy= }, {retention=}, {target_size=}, {size_list=}")
            print(np.abs(size_list - target_size))
            closest_idx = np.abs(size_list - target_size).argmin()
            print(f"{closest_idx=}")
            retention_at_t10 = retention[closest_idx]
            print(f"{retention_at_t10},")
            retentions_at_t10.energy.append(energy)
            retentions_at_t10.t10.append(retention_at_t10)
    return retentions_at_t10

def calculate_params_from_ab(A, b, SG):
    DWI = 92.56 * SG * (A*b) ** (-.977)
    SCSE = 52.74 * (A*b) ** (-.441)
    t_a = 2.6132 * (DWI) ** (-1)
    M_ia = 390 * (A *b) **  (-.813)
    M_ic = 303.5 * (A *b) ** (-1)
    M_ih = 577 * (A *b) ** (-1)
    return DWI, SCSE, t_a, M_ia, M_ic, M_ih