from flask import Flask, jsonify, request
from database import initialize_db, get_books, add_book, update_book, delete_book, get_book

app = Flask(__name__)
initialize_db()

@app.route('/')
def home():
    return jsonify({"message": "Library Manager API is running"})

@app.route('/api/books', methods=['GET'])
def get_all_books():
    books = get_books()
    # Convert to list of dicts for JSON
    books_list = [
        {
            'id': b[0],
            'title': b[1],
            'publication_year': b[2],
            'author': b[3],
            'genre': b[4]
        } for b in books
    ]
    return jsonify(books_list)

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.json
    add_book(data['title'], data['publication_year'], data['author'], data['genre'])
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    data = request.json
    update_book(book_id, data['title'], data['publication_year'], data['author'], data['genre'])
    return jsonify({'message': 'Book updated successfully'})

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    delete_book(book_id)
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)