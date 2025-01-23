from sqlalchemy import Column, Float, Integer, String, DateTime,  Boolean, ARRAY, ForeignKey, LargeBinary, JSON
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

class SMC_RESULT(Base):
    __tablename__ = 'SMC_RESULTS'
    __table_args__ = {'schema': schema}

    id = Column(Integer, primary_key=True, index=True)

     
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    data = Column(JSON)
    initial_weight = Column(Float, index=True)
    input_energy = Column(Float, index= True)
    sample_name = Column(String, index=True)
    SG = Column(Float, index=True)

class DWT_EXCEL(Base):
    __tablename__ = 'DWT_EXCEL'
    __table_args__ = {'schema': schema}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    data = Column(JSON)
    file_name = Column(String, index=True)


class SMC_EXCEL(Base):
    __tablename__ = 'SMC_EXCEL'
    __table_args__ = {'schema': schema}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    data = Column(JSON)
    file_name = Column(String, index=True)

class SMC_RAW_DATA(Base):
    __tablename__ = 'SMC_RAW_DATA'
    __table_args__ = {'schema': schema} 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    file = Column(LargeBinary)
    file_name = Column(String, index=True)

class SMC_REPORT(Base):
    __tablename__ = 'SMC_REPORT'
    __table_args__ = {'schema': schema} 
    id = Column(Integer, primary_key=True, index=True)
    M_ic = Column(Float, index=True)
    M_ih = Column(Float, index=True)
    M_ia = Column(Float, index=True)
    SCSE = Column(Float, index=True)
    t_a = Column(Float, index=True)
    DWI = Column(Float, index=True)
    A = Column(Float, index=True)
    b = Column(Float, index=True)
    SG = Column(Float, index=True)
    file_name = Column(String, index=True)


class SMC_DATA_FOR_GRAPH(Base):
    __tablename__ = 'SMC_DATA_FOR_GRAPH'
    __table_args__ = {'schema': schema} 

    id = Column(Integer, primary_key=True, index=True)


class DWT_RAW_DATA(Base):
    __tablename__ = 'DWT_RAW_DATA'
    __table_args__ = {'schema': schema} 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    created_timestamp = Column(Float, index=True)
    file = Column(LargeBinary)
    file_name = Column(String, index=True)

class DWT_REPORT(Base):
    __tablename__ = 'DWT_REPORT'
    __table_args__ = {'schema': schema} 
    id = Column(Integer, primary_key=True, index=True)
    M_ic = Column(Float, index=True)
    M_ih = Column(Float, index=True)
    M_ia = Column(Float, index=True)
    SCSE = Column(Float, index=True)
    t_a = Column(Float, index=True)
    DWI = Column(Float, index=True)
    A = Column(Float, index=True)
    b = Column(Float, index=True)
    SG = Column(Float, index=True)
    file_name = Column(String, index=True)


class DWT_DATA_FOR_GRAPH(Base):
    __tablename__ = 'DWT_DATA_FOR_GRAPH'
    __table_args__ = {'schema': schema} 

    id = Column(Integer, primary_key=True, index=True)