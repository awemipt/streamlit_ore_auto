from pydantic import BaseModel, ConfigDict

class SMC_REPORT(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    A: list[float]
    b: float
    SG: float
    DWI: float
    SCSE: float 
    t_a: float
    M_ia: float
    M_ic: float
    M_ih: float