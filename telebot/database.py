from sqlalchemy import create_engine, text, MetaData, Table
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    # echo=True,
    pool_size=5,
    max_overflow=10,
)

metadata = MetaData()


Orders = Table('products_orders', metadata, autoload_with=engine)
Customuser = Table('products_customuser', metadata, autoload_with=engine)



