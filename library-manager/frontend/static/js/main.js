// This file contains JavaScript code for the frontend, handling user interactions and making AJAX requests to the backend.

document.addEventListener('DOMContentLoaded', function() {
    loadBooks();

    document.getElementById('addBookForm').onsubmit = function(event) {
        event.preventDefault();
        addBook();
    };
});

function loadBooks() {
    fetch('/api/books')
        .then(response => response.json())
        .then(data => {
            const bookList = document.getElementById('bookList');
            bookList.innerHTML = '';
            data.forEach(book => {
                const li = document.createElement('li');
                li.textContent = `${book.title} by ${book.author} (${book.year}) - Genre: ${book.genre}`;
                bookList.appendChild(li);
            });
        })
        .catch(error => console.error('Error loading books:', error));
}

function addBook() {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const year = document.getElementById('year').value;
    const genre = document.getElementById('genre').value;

    fetch('/api/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, author, year, genre })
    })
    .then(response => {
        if (response.ok) {
            loadBooks();
            document.getElementById('addBookForm').reset();
        } else {
            console.error('Error adding book:', response.statusText);
        }
    })
    .catch(error => console.error('Error adding book:', error));
}