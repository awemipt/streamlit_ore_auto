from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import SMC, DWT_RESULT



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
