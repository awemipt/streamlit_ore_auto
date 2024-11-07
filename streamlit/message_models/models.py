from pydantic import BaseModel, Field, ValidationError
from typing_extensions import Annotated
positive_float =  Annotated[float, Field(strict=True, gt=1)]
from datetime import datetime

bool_ =  Annotated[bool, Field(strict=True)]
name_str = Annotated[str, Field(strict=True, min_length=1)]
comment_str = Annotated[str, Field(strict=True, min_length=1, max_length=500)]

class SendSmcModel(BaseModel):
    name: name_str
    a:  positive_float
    b: positive_float
    dwt: positive_float
    smc: bool_
    comment: comment_str
    wirm_bond: positive_float
    wirm_non_std: positive_float

class Metadata(BaseModel):
    username : name_str
    created_timestamp : positive_float
