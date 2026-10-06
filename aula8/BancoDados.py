from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Usuario(Base):
    _tablename_ = 'ususarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def _repr_(self):
        return f"usuario(id={self.id}, nome={self.nome}, idade={self.idade})"

Base.metadata.creat_all(engine)

Session = sessionmker(bind=engine)
session = Session()

usuario1 = Usuario(nome='Raphael', idade=42)
usuario2 = Usuario(nome='Leticia', idade=40)
session.add(usuario1)
session.add(usuario2)

session.commit()

usuario = session.querry(Usuario).all()

for usuario in usuarios:
    print(usuario)

