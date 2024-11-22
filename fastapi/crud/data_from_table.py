from dataclasses import dataclass
import numpy as np
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import DWT_RESULT       




async def get_t10_data(db: AsyncSession, sample_name: str):
    query = select(DWT_RESULT).where(DWT_RESULT.sample_name == sample_name)
    result = await db.execute(query)
    dwt_data_list = result.scalars()
    retentions_at_t10 = []
    for dwt_data in dwt_data_list:
        if dwt_data:
            data = dwt_data.data
            energy = dwt_data.input_energy
            size = data['Size (mm)']['0']
            sizes = np.array(list(data['Size (mm)'].values())[:-1], dtype=float)
            target_size = float(size) / 10
            retentions = np.array(list(data['Retention percentage (%)'].values())[:-1], dtype=float)
            
            closest_idx = np.abs(sizes - target_size).argmin()
            retention_at_t10 = retentions[closest_idx]
            retentions_at_t10.append({"energy": energy, "retention_at_t10": retention_at_t10})
    return retentions_at_t10
        

