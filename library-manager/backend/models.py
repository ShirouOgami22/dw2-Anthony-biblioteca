class Book:
    def __init__(self, title, publication_year, author, genre):
        self.title = title
        self.publication_year = publication_year
        self.author = author
        self.genre = genre

    def __repr__(self):
        return f"<Book(title={self.title}, publication_year={self.publication_year}, author={self.author}, genre={self.genre})>"