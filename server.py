from sanic import Sanic
from constants import *
from table import Base
import api_v1
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

app = Sanic(SERVICENAME)
engine = create_engine(DB_CONN_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
app.db = engine
api_v1.setup_api(app)


if 'conference' not in inspect(engine).get_table_names():
    Base.metadata.create_all(app.db)

app.run()
