from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("يتم الاتصال بقاعدة مناجو دي بي الان...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("تم الاتصال ب قاعدة مانجو دي بي بنجاح.")
except:
    LOGGER(__name__).error("فشل الاتصال ب قاعدة منجو دي بي .")
    exit()
