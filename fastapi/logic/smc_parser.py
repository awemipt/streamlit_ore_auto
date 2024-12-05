import pandas as pd
from dataclasses import dataclass
@dataclass
class SMC_RESULT:
    energy: list[float]
    t10: list[float]
    SG: float

def smc_parser(file: bytes):
    excel_file = pd.ExcelFile(file, engine='openpyxl')
    sheets = excel_file.sheet_names
    res_sheet = sheets.index("Исходные данные")
    if res_sheet == -1:
        raise ValueError("Sheet 'Исходные данные' not found")
    df = pd.read_excel(excel_file, sheet_name=sheets[res_sheet])
    res = {key: value for key, value in zip(df[df.columns[1]][9:14], df[df.columns[2]][9:14])}

    SG =  list(df[df.columns[1]][14:15])[0]
    
    print(SG)
    print(res)
    energy, t10 = zip(*res.items())
    res = SMC_RESULT(energy=energy, t10=t10, SG=SG)
    return res, SG