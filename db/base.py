from databases import Database
from sqlalchemy import create_engine, MetaData

from core.config import DATABASE_URL

EE_DATABASE_URL="postgresql://root:root@localhost:32700/employment_exchange"
database = Database(EE_DATABASE_URL)#DATABASE_URL
metadata = MetaData()
engine = create_engine(
    DATABASE_URL
)