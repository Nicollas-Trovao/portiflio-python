import os
from sqlalchemy import creat_engine, select
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(DIRETORIO_ATUAL, 'banco_dados.db')
engine = creat_engine(f'sqlite:///{CAMINHO_BANCO}', echo=True)

class base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    idade: Mapped[int] = mapped_column()

    def __repr__(self) -> str:
        return f"usario(id={self.id}, nome={self.nome}, idade={self.idade})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

with Session() as session:
    Usuario1 = Usuario(nome='Raphael', idade=42)
    Usuario2 = Usuario(nome='Leticia', idade=40)
    session.add_all([Usuario1, Usuario2])

    session.commit()

    stmt = select(Usuario)
    Usuarios = session.scalars(stmt).all()

    for usuario in Usuarios:
        print(usuario)