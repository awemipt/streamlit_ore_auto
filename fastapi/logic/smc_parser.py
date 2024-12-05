import pandas as pd
def smc_parser(file: bytes):
    excel_file = pd.ExcelFile(file, engine='openpyxl')
    sheets = excel_file.sheet_names
    res_sheet = sheets.index("Исходные данные")
    if res_sheet == -1:
        raise ValueError("Sheet 'Исходные данные' not found")
    df = pd.read_excel(excel_file, sheet_name=sheets[res_sheet])
    res = {key: value for key, value in zip(df[df.columns[1]][9:14], df[df.columns[2]][9:14])}
    SG =  df[df.columns[2]][15].values[0]
    print(SG)
    print(res)
    return df