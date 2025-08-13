# Library Manager

## Overview
The Library Manager is a web-based application designed to manage a collection of books. It allows users to view, add, update, and delete book records through a user-friendly interface. The application is built using Python with a Flask backend and a simple HTML/CSS/JavaScript frontend.

## Project Structure
The project is organized into the following directories and files:

```
library-manager
├── backend
│   ├── app.py               # Main entry point for the backend application
│   ├── database.py          # Handles database connection and operations
│   ├── models.py            # Defines the data model for books
│   ├── requirements.txt      # Lists required Python packages
│   └── README.md            # Documentation for the backend
├── frontend
│   ├── static
│   │   ├── css
│   │   │   └── style.css    # CSS styles for the web interface
│   │   └── js
│   │       └── main.js      # JavaScript code for user interactions
│   └── templates
│       └── index.html       # Main HTML template for the web interface
├── data
│   └── library.db           # SQLite database containing book records
├── start_app.bat           # Batch file to start the application
├── log.md                   # Logs of project development prompts
└── README.md                # General documentation for the project
```

## Setup Instructions
1. **Clone the repository** to your local machine.
2. **Navigate to the backend directory** and install the required packages using:
   ```
   pip install -r requirements.txt
   ```
3. **Initialize the database** by running the `database.py` script.
4. **Start the application** by executing the `start_app.bat` file.

## Usage
- Open your web browser and navigate to `http://localhost:5000` to access the Library Manager interface.
- Use the interface to manage your book collection.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.