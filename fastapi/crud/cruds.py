from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import SMC



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

async def write_DWT(db: AsyncSession, data):
    pass