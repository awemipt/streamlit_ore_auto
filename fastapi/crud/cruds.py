from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import SMC, DWT_RESULT, SMC_REPORT, SMC_RAW_DATA, DWT_REPORT, DWT_RAW_DATA 
from models.message_models import SMC_REPORT as SMC_REPORT_MESSAGE
from sqlalchemy.exc import NoResultFound

async def create_SMC(db: AsyncSession, data):
    db_SMC = SMC(
        **data
    )
    db.add(db_SMC)
    await db.commit()
    await db.refresh(db_SMC)
    return db_SMC

async def get_SMC(db: AsyncSession , limit, offset ):
    query = select(SMC).limit(limit).offset(offset)
    result = await db.execute(query)
    return result

async def create_DWT_RESULT(db: AsyncSession, data):
    db_DWT = DWT_RESULT(
        **data
    )
    db.add(db_DWT)
    await db.commit()
    await db.refresh(db_DWT)
    return db_DWT

async def get_DWT_samples(db: AsyncSession):
    query = select(DWT_RESULT.sample_name).distinct()
    result = await db.execute(query)
    samples = [row[0] for row in result.fetchall()]
    return samples


async def get_SMC_reports_list(db: AsyncSession):
    query = select(SMC_REPORT.file_name).distinct()
    result = await db.execute(query)
    samples = [row[0] for row in result.fetchall()]
    return samples

async def get_SMC_report(db: AsyncSession, file_name: str) -> SMC_REPORT:
    try:
        query =  select(SMC_REPORT).filter(SMC_REPORT.file_name == file_name)
        result = await db.execute(query)
        report = result.scalar_one_or_none() 
        report_dict = {
            'id': report.id,
            'M_ic': report.M_ic,
            'M_ih': report.M_ih,
            'M_ia': report.M_ia,
            'SCSE': report.SCSE,
            't_a': report.t_a,
            'DWI': report.DWI,
            'A': report.A,
            'b': report.b,
            'SG': report.SG,
            'file_name': report.file_name
        }
  
        return report_dict
    except NoResultFound:
        # Если запись не найдена
        return None

async def get_SMC_raw_data(db: AsyncSession, file_name: str):
    
    return None


async def create_SMC_report(db: AsyncSession, data):
    db_SMC_report = SMC_REPORT(
        **data
    )
    db.add(db_SMC_report)
    await db.commit()
    await db.refresh(db_SMC_report)
    return db_SMC_report

async def create_SMC_raw_data(db: AsyncSession, data):
    db_SMC_raw_data = SMC_RAW_DATA(
        **data
    )
    db.add(db_SMC_raw_data)
    await db.commit()
    await db.refresh(db_SMC_raw_data)
    return db_SMC_raw_data


async def create_DWT_report(db: AsyncSession, data):
    db_DWT_report = DWT_REPORT(
        **data
    )
    db.add(db_DWT_report)
    await db.commit()
    await db.refresh(db_DWT_report)
    return db_DWT_report

async def create_DWT_raw_data(db: AsyncSession, data):
    db_DWT_raw_data = DWT_RAW_DATA(
        **data
    )
    db.add(db_DWT_raw_data)
    await db.commit()
    await db.refresh(db_DWT_raw_data)
    return db_DWT_raw_data

async def get_DWT_reports_list(db: AsyncSession):
    query = select(DWT_REPORT.file_name).distinct()
    result = await db.execute(query)
    samples = [row[0] for row in result.fetchall()]
    return samples

async def get_DWT_report(db: AsyncSession, file_name: str) -> DWT_REPORT:
    try:
        query =  select(DWT_REPORT).filter(DWT_REPORT.file_name == file_name)
        result = await db.execute(query)
        report = result.scalar_one_or_none() 
        report_dict = {
            'id': report.id,
            'M_ic': report.M_ic,
            'M_ih': report.M_ih,
            'M_ia': report.M_ia,
            'SCSE': report.SCSE,
            't_a': report.t_a,
            'DWI': report.DWI,
            'A': report.A,
            'b': report.b,
            'SG': report.SG,
            'file_name': report.file_name
        }
  
        return report_dict
    except NoResultFound:
        # Если запись не найдена
        return None