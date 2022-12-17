from starlette.config import Config

config = Config('.env')
DATABASE_URL = config("EE_DATABASE_URL", cast=str, default='')
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="2b2b197649061838c0c3811612xb117d5f562ff181f2ed68c7847471af22f83ce")