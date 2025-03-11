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
def cumsum(retentions, start=0):
    ans = []
    tmp = start
    for retention in retentions:
        ans.append(tmp)
        tmp += retention
        
    return ans



def get_ore_params(retentions, energies, sizes, SG):

    sizes_10 = [size[0] / 10 for size in sizes] 

    retentions = retentions.transpose(1, 0, 2)
    retentions_at_t10 = DWT_RESULT(energy=[], t10=[], SG=SG)
    retentions_to_graph = []
    sizes_to_graph = []
    for target_size, size_list, retention_list, energy_list in zip(sizes_10, sizes, retentions, energies):
        size_list = list(size_list)[::-1]
        
        for energy, retention in zip(energy_list, retention_list):

            
            retention  = cumsum(retention[::-1], start=(100-sum(retention)))
            print(f"{energy= },\n {retention=}, \n{target_size=}, \n{size_list=}")
            print(np.abs(size_list - target_size))
            retentions_to_graph.append(retention)
            sizes_to_graph.append(size_list)
            closest_idx = np.abs(size_list - target_size).argmin()
            max_idx = closest_idx + 1
            min_idx = closest_idx - 1
            if size_list[min_idx] <= target_size <= size_list[closest_idx]:
                print("\n\n\n---------HERE----------\n\n\n")
                retention_at_t10 = retention[min_idx] + (retention[closest_idx] - retention[min_idx])* (target_size - size_list[min_idx])/(size_list[closest_idx] - size_list[min_idx])
            else:
                 
                print(f"\n\n\n---------THERE----------\n\n\n {target_size - size_list[closest_idx]}")
                retention_at_t10 = retention[closest_idx] + (retention[max_idx] - retention[closest_idx])* (target_size - size_list[closest_idx])/(size_list[max_idx] - size_list[closest_idx])
            
                
            print(f"{closest_idx=}")
            # retention_at_t10 = retention[closest_idx]
            print(f"{retention_at_t10},")
            retentions_at_t10.energy.append(energy)
            retentions_at_t10.t10.append(retention_at_t10)

            print(f"\n\n\n\n{retentions_at_t10.t10=}\n\n\n")
    return retentions_at_t10, retentions_to_graph, sizes_to_graph

def calculate_params_from_ab(A, b, SG):
    DWI = 92.56 * SG * (A*b) ** (-.977)
    SCSE = 52.74 * (A*b) ** (-.441)
    t_a = 2.6132 * (DWI) ** (-1)
    M_ia = 390 * (A *b) **  (-.813)
    M_ic = 303.5 * (A *b) ** (-1)
    M_ih = 577 * (A *b) ** (-1)
    return DWI, SCSE, t_a, M_ia, M_ic, M_ih