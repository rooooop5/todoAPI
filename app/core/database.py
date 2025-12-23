from sqlmodel import SQLModel, Session, create_engine

# -------the database url--------
url = 'postgresql+psycopg://saswatam@localhost:5432/tasks'


# ------creating an engine------
engine = create_engine(url)


# ------creating a table on starturp------
def _init_table():
    SQLModel.metadata.create_all(engine)


# -----creating a session------
def get_session():
    with Session(engine) as session:
        yield session
