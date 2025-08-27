from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import database
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = database.SessionLocal

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/livros")
def get_livros(search: Optional[str] = None, genero: Optional[str] = None, ano: Optional[int] = None, status: Optional[str] = None):
    session = db()
    query = session.query(models.Livro)
    if search:
        query = query.filter((models.Livro.titulo.ilike(f"%{search}%")) | (models.Livro.autor.ilike(f"%{search}%")))
    if genero:
        query = query.filter(models.Livro.genero == genero)
    if ano:
        query = query.filter(models.Livro.ano == ano)
    if status:
        query = query.filter(models.Livro.status == status)
    livros = query.all()
    session.close()
    return [livro.to_dict() for livro in livros]

@app.post("/livros")
def create_livro(livro: models.LivroCreate):
    session = db()
    # Check for duplicate title
    if session.query(models.Livro).filter(models.Livro.titulo == livro.titulo).first():
        session.close()
        raise HTTPException(status_code=400, detail="Duplicate title")
    new_livro = models.Livro(**livro.dict())
    session.add(new_livro)
    session.commit()
    session.refresh(new_livro)
    session.close()
    return new_livro.to_dict()

@app.put("/livros/{id}")
def update_livro(id: int, livro: models.LivroCreate):
    session = db()
    db_livro = session.query(models.Livro).get(id)
    if not db_livro:
        session.close()
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in livro.dict().items():
        setattr(db_livro, key, value)
    session.commit()
    session.refresh(db_livro)
    session.close()
    return db_livro.to_dict()

@app.delete("/livros/{id}")
def delete_livro(id: int):
    session = db()
    db_livro = session.query(models.Livro).get(id)
    if not db_livro:
        session.close()
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(db_livro)
    session.commit()
    session.close()
    return {"ok": True}

@app.post("/livros/{id}/emprestar")
def emprestar_livro(id: int):
    session = db()
    db_livro = session.query(models.Livro).get(id)
    if not db_livro:
        session.close()
        raise HTTPException(status_code=404, detail="Book not found")
    if db_livro.status == "emprestado":
        session.close()
        raise HTTPException(status_code=400, detail="Book already loaned")
    db_livro.status = "emprestado"
    db_livro.data_emprestimo = datetime.utcnow()
    session.commit()
    session.refresh(db_livro)
    session.close()
    return db_livro.to_dict()

@app.post("/livros/{id}/devolver")
def devolver_livro(id: int):
    session = db()
    db_livro = session.query(models.Livro).get(id)
    if not db_livro:
        session.close()
        raise HTTPException(status_code=404, detail="Book not found")
    if db_livro.status != "emprestado":
        session.close()
        raise HTTPException(status_code=400, detail="Book is not loaned")
    db_livro.status = "disponível"
    db_livro.data_emprestimo = None
    session.commit()
    session.refresh(db_livro)
    session.close()
    return db_livro.to_dict()
