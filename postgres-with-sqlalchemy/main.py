from db import models
from db.database import engine

models.Base.metadata.create_all(bind=engine)