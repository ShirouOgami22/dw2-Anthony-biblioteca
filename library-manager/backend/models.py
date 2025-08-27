from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional
from datetime import datetime

Base = declarative_base()

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(90), unique=True, nullable=False)
    autor = Column(String(90), nullable=False)
    ano = Column(Integer, nullable=False)
    genero = Column(String(30), nullable=False)
    isbn = Column(String(30), nullable=True)
    status = Column(String(20), nullable=False, default="disponível")
    data_emprestimo = Column(DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "genero": self.genero,
            "isbn": self.isbn,
            "status": self.status,
            "data_emprestimo": self.data_emprestimo.isoformat() if self.data_emprestimo else None
        }

from pydantic import BaseModel, Field

class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=90)
    autor: str
    ano: int
    genero: str
    isbn: Optional[str] = None
    status: str
    data_emprestimo: Optional[datetime] = None
