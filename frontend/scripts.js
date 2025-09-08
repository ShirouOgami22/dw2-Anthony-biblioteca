const API_URL = "http://127.0.0.1:8000";

// Accessibility: focus trap for modal
document.addEventListener('keydown', (e) => {
    if (e.altKey && e.key.toLowerCase() === 'n') {
        e.preventDefault();
        openBookModal();
    }
});
document.addEventListener('keydown', (e) => {
    if (e.key=== 'Escape') {
       document.getElementById('modal').hidden = true;
    }
});
document.getElementById('new-book-btn').addEventListener('click', openBookModal);
document.getElementById('search').addEventListener('input', loadBooks);
document.getElementById('filter-genre').addEventListener('change', loadBooks);
document.getElementById('filter-year').addEventListener('input', loadBooks);
document.getElementById('filter-status').addEventListener('change', loadBooks);

function openBookModal() {
    const modal = document.getElementById('modal');
    modal.innerHTML = renderBookForm();
    modal.hidden = false;
    modal.querySelector('input,select').focus();
    modal.querySelector('.close').onclick = () => modal.hidden = true;
    modal.querySelector('form').onsubmit = handleBookFormSubmit;
}

function renderBookForm(book) {
    return `<div class="modal-content">
        <button class="close" aria-label="Close">&times;</button>
        <br><br>
        <form>
            <label>Title<br><input name="titulo" required minlength="3" maxlength="90" value="${book!=null ? book.titulo : ''}"></label><br><br>
            <label>Author<br><input name="autor" required value="${book!=null ? book.autor : ''}"></label><br><br>
            <label>Year<br><input name="ano" type="number" min="1900" max="${new Date().getFullYear()}" required value="${book!=null ? book.ano : ''}"></label><br><br>
            <label>Genre<br><input name="genero" required value="${book!=null ? book.genero : ''}"></label><br><br>
            <label>ISBN<br><input name="isbn" value="${book!=null ? book.isbn || '' : ''}"></label><br><br>
            <label>Status<br><select name="status" required><option value="disponível" ${!book!=null||book.status==="disponível"?'selected':''}>Available</option><option value="emprestado" ${book&&book.status==="emprestado"?'selected':''}>Loaned</option></select></label><br><br>
            <br><br><button type="submit">${book!=null ? 'Update' : 'Add'} Book</button>
        </form>
    </div>`;
}

async function handleBookFormSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const data = Object.fromEntries(new FormData(form));
    data.ano = parseInt(data.ano);
    data.status = data.status || "disponível";
    // Prevent duplicate title (front)
    const books = await fetchBooks();
    if (!form.closest('.modal-content').querySelector('button[type="submit"]').textContent.includes('Update') && books.some(b => b.titulo === data.titulo)) {
        alert('Duplicate title!');
        return;
    }
    const method = form.closest('.modal-content').querySelector('button[type="submit"]').textContent.includes('Update') ? 'PUT' : 'POST';
    const url = method === 'POST' ? `${API_URL}/livros` : `${API_URL}/livros/${books.find(b => b.titulo === data.titulo).id}`;
    const res = await fetch(url, {
        method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!res.ok) {
        alert('Error: ' + (await res.text()));
        return;
    }
    document.getElementById('modal').hidden = true;
    loadBooks();
}

async function fetchBooks() {
    const res = await fetch(`${API_URL}/livros`);
    return res.ok ? res.json() : [];
}

async function loadBooks() {
    const search = document.getElementById('search').value;
    const genero = document.getElementById('filter-genre').value;
    const ano = document.getElementById('filter-year').value;
    const status = document.getElementById('filter-status').value;
    let url = `${API_URL}/livros?`;
    if (search) url += `search=${encodeURIComponent(search)}&`;
    if (genero) url += `genero=${encodeURIComponent(genero)}&`;
    if (ano) url += `ano=${encodeURIComponent(ano)}&`;
    if (status) url += `status=${encodeURIComponent(status)}&`;
    const res = await fetch(url);
    const books = res.ok ? await res.json() : [];
    renderBooks(books);
    renderGenreOptions(books);
}

function renderBooks(books) {
    const list = document.getElementById('books-list');
    list.innerHTML = books.map(book => `
        <div class="card" tabindex="0">
            <div><b>${book.titulo}</b></div>
            <div>${book.autor} (${book.ano})</div>
            <div>${book.genero}</div>
            <div class="status ${book.status}">${book.status}</div>
            <button onclick="editBook(${book.id})">Edit</button>
            <button onclick="deleteBook(${book.id})">Delete</button>
            <button onclick="${book.status==='disponível' ? `loanBook(${book.id})` : `returnBook(${book.id})`}">${book.status==='disponível' ? 'Loan' : 'Return'}</button>
        </div>
    `).join('');
}

function renderGenreOptions(books) {
    const genres = Array.from(new Set(books.map(b => b.genero)));
    const select = document.getElementById('filter-genre');
    select.innerHTML = '<option value="">All</option>' + genres.map(g => `<option value="${g}">${g}</option>`).join('');
}

window.editBook = async function(id) {
    const books = await fetchBooks();
    const book = books.find(b => b.id === id);
    openBookModal(book);
}

window.deleteBook = async function(id) {
    if (!confirm('Delete this book?')) return;
    await fetch(`${API_URL}/livros/${id}`, { method: 'DELETE' });
    loadBooks();
}

window.loanBook = async function(id) {
    await fetch(`${API_URL}/livros/${id}/emprestar`, { method: 'POST' });
    loadBooks();
}

window.returnBook = async function(id) {
    await fetch(`${API_URL}/livros/${id}/devolver`, { method: 'POST' });
    loadBooks();
}

document.addEventListener('DOMContentLoaded', loadBooks);
