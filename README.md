# Flask Random Joke App

This is a simple Flask web application that displays a random joke from a text file. It includes a button to refresh the page and show another random joke.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/edaehn/flask-random-joke.git
    ```

2. Change into the project directory:

    ```bash
    cd flask-random-joke
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to http://127.0.0.1:5000/joke to view a random joke. Click the "Get Another Joke" button to refresh the page and display a new joke.

## Folder Structure

- `templates/`: Contains HTML templates, including `joke.html`.
- `static/`: Stores static files like stylesheets.
- `app.py`: The main Flask application file.
- `jokes.txt`: Text file containing a list of jokes.

## Dependencies

- [Flask](https://flask.palletsprojects.com/): Python web framework used for building the web application.

## License

This project is licensed under the [Creative Commons CC BY-SA](https://creativecommons.org/share-your-work/cclicenses/#:~:text=CC%20BY%2DSA,modified%20material%20under%20identical%20terms).
