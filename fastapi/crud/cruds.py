from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import SMC, DWT_RESULT, SMC_REPORT, SMC_RAW_DATA



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

async def get_SMC_report(db: AsyncSession, file_name: str):
    query = select(SMC_REPORT).where(SMC_REPORT.file_name == file_name)
    result = await db.execute(query)
    return result.fetchone()
async def get_SMC_raw_data(db: AsyncSession, file_name: str):
    query = select(SMC_RAW_DATA).where(SMC_RAW_DATA.file_name == file_name[:-7])
    result = await db.execute(query)
    return result.fetchone()
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