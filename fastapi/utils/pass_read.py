import traceback
import aiofiles
import json

async def read_json_async(file_path: str):
    try:
        async with aiofiles.open(file_path, 'r') as file:
            content = await file.read()
            data = json.loads(content)
        return data
    except Exception as e:
        print(traceback.format_exc())
