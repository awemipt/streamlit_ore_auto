from pydantic import BaseModel

class SMC_REPORT(BaseModel):
    A: list[float]
    b: float
    SG: float
    DWI: float
    SCSE: float 
    t_a: float
    M_ia: float
    M_ic: float
    M_ih: float

