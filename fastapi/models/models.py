from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, ARRAY, ForeignKey, LargeBinary, JSON
from sqlalchemy.sql import func
from sqlalchemy.schema import DefaultClause
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
schema = 'public'

class SMC(Base):
    __tablename__ = 'SMC'
    __table_args__ = {'schema': schema}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    comment = Column(String,index=True )
    a = Column(Float, index=True)
    b = Column(Float, index=True)
    dwt = Column(Float, index=True)
    smc = Column(Boolean, index=True)
    wirm_bond = Column(Float, index=True)
    wirm_non_std = Column(Float, index=True)
    
    
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)


class DWT_RESULT(Base):
    __tablename__ = 'DWT_RESULTS'
    __table_args__ = {'schema': schema}

    id = Column(Integer, primary_key=True, index=True)

     
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    data = Column(JSON)
    initial_weight = Column(Float, index=True)
    input_energy = Column(Float, index= True)
    sample_name = Column(String, index=True)