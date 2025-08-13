from flask import Flask, jsonify, request
from database import init_db, get_books, add_book, update_book, delete_book

app = Flask(__name__)

@app.before_first_request
def initialize_database():
    init_db()

@app.route('/api/books', methods=['GET'])
def get_all_books():
    books = get_books()
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = add_book(data['title'], data['publication_year'], data['author'], data['genre'])
    return jsonify(new_book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.json
    updated_book = update_book(book_id, data['title'], data['publication_year'], data['author'], data['genre'])
    return jsonify(updated_book)

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    delete_book(book_id)
    return jsonify({'message': 'Book deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)