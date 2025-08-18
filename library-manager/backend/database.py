import sqlite3

def connect_db():
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, '..', 'data', 'library.db')
    conn = sqlite3.connect(db_path)
    return conn

def initialize_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            publication_year INTEGER NOT NULL,
            author TEXT NOT NULL,
            genre TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, publication_year, author, genre):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, publication_year, author, genre)
        VALUES (?, ?, ?, ?)
    ''', (title, publication_year, author, genre))
    conn.commit()
    conn.close()

def get_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def get_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()
    conn.close()
    return book

def update_book(book_id, title, publication_year, author, genre):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE books
        SET title = ?, publication_year = ?, author = ?, genre = ?
        WHERE id = ?
    ''', (title, publication_year, author, genre, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()