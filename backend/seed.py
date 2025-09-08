from database import SessionLocal
from models import Livro
from datetime import datetime

def seed():
    session = SessionLocal()
    if session.query(Livro).count() > 0:
        print("Seed already applied.")
        session.close()
        return
    genres = ["Fiction", "Non-Fiction", "Science", "History", "Fantasy", "Biography", "Mystery", "Romance", "Adventure", "Children"]
    livros = []
    for i in range(1, 51):
        livros.append(Livro(
            titulo=f"Book {i}",
            autor=f"Author {chr(65 + (i % 26))}",
            ano=1990 + (i % 35),
            genero=genres[i % len(genres)],
            isbn=f"ISBN{i:05d}",
            status="disponível"
        ))
    session.add_all(livros)
    session.commit()
    session.close()
    print("Seed applied: 50 books.")

if __name__ == "__main__":
    seed()
