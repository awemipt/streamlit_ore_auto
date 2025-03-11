import pandas as pd
from dataclasses import dataclass
import numpy as np



def dwt_parser(file: bytes):
    excel_file = pd.ExcelFile(file)
    sheets = excel_file.sheet_names
    res_sheet = sheets.index("Ввод результатов теста")
    
    if res_sheet == -1:
        raise ValueError("Sheet 'Ввод результатов теста' not found")
    df = pd.read_excel(excel_file, sheet_name=sheets[res_sheet])
    sizes = [np.array(list(i)) for i in (df[df.columns[0]][37:52], df[df.columns[0]][61:76], 
    
        df[df.columns[0]][85:100], df[df.columns[0]][109:124], df[df.columns[0]][133:148])]
    retentions = np.array([
        [np.array(list(i)) for i in (df[df.columns[3]][37:52], df[df.columns[3]][61:76], 
        df[df.columns[3]][85:100], df[df.columns[3]][109:124], df[df.columns[3]][133:148])],

        [np.array(list(i)) for i in (df[df.columns[6]][37:52], df[df.columns[6]][61:76], 
        df[df.columns[6]][85:100], df[df.columns[6]][109:124], df[df.columns[6]][133:148])],
        
        [np.array(list(i)) for i in (df[df.columns[9]][37:52], df[df.columns[9]][61:76], 
        df[df.columns[9]][85:100], df[df.columns[9]][109:124], df[df.columns[9]][133:148])]
    ])
    energies = np.array([[df.values[34 + i][2], df.values[34 + i][5], df.values[34 + i][8]]for i in range(0,120,24)])
    for i in range(len(retentions)):
        for j in range(3):
            print(retentions[i][j])
    SG = list(df[df.columns[3]][215:216])[0]

    return retentions, energies, sizes, SG