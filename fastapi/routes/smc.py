from fastapi import APIRouter, HTTPException
import aiofiles
import asyncio
import os
from utils import read_json_async
# from LogstashJsonSocketHandler import get_logger
# logger = get_logger(__name__)
from config import base_config
router = APIRouter()


@router.post('/')
async def input(data: dict):
    pass
    