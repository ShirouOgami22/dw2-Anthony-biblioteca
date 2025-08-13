# Library Manager Backend

This is the backend component of the Library Manager project, which is built using Python and Flask. The backend handles all the server-side logic, including database interactions and API endpoints for the frontend.

## Project Structure

- **app.py**: The main entry point for the backend application. It sets up the Flask web server, defines routes for handling requests, and connects to the SQLite database.
- **database.py**: Manages the database connection and operations. It includes functions to initialize the database and perform CRUD operations on the books.
- **models.py**: Defines the data model for the books. It includes a class `Book` that represents the structure of a book in the database, with properties for title, publication year, author, and genre.
- **requirements.txt**: Lists the required Python packages for the project, such as Flask and SQLite.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd library-manager/backend
   ```

2. **Install the required packages**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. **Initialize the database**:
   Run the following command to set up the SQLite database:
   ```
   python database.py
   ```

4. **Run the application**:
   Start the Flask server by executing:
   ```
   python app.py
   ```

## Usage

Once the server is running, you can access the API endpoints to manage the library's books. The frontend will interact with these endpoints to display and manipulate book data.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.