from dataclasses import dataclass
import numpy as np
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import DWT_RESULT       

@dataclass
class ore53:
    
    energy = np.array([0.4,0.25,0.1])
    t10 = np.array([26.89, 17.99, 8.66])


@dataclass
class ore37_5:
    
    energy = np.array([1,0.25,0.1])
    t10 = np.array([38.33, 13.74, 7.22])




@dataclass
class ore26_5:
    
    energy = np.array([2.5,1,0.25])
    t10 = np.array([57.07, 32.28, 10.17])



@dataclass
class ore19:
    
    energy = np.array([2.49,1,0.25])
    t10 = np.array([53.08, 27.46, 7.94])


@dataclass
class ore13_2:
    
    energy = np.array([2.5,1,0.25])
    t10 = np.array([46.01, 20.74, 7.91])


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
            retentions = np.array(list(data['Retention comulitive percentage (%)'].values())[:-1], dtype=float)
            
            closest_idx = np.abs(sizes - target_size).argmin()
            retention_at_t10 = retentions[closest_idx]
            retentions_at_t10.append({"energy": energy, "retention_at_t10": retention_at_t10})
    return retentions_at_t10
        

