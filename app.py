# Import the Flask class, render_template, and request from the flask module
from flask import Flask, render_template, request

# Import the random module for generating random values
import random

# Create an instance of the Flask class, usually named 'app'
app = Flask(__name__)

# Define a route for the root URL ('/'). When someone accesses the root URL, the function below is executed.
@app.route('/')
def hello_world():
    # Use the render_template function to render an HTML template named 'index.html'
    # The template is rendered with the provided title and message variables
    return render_template('index.html', title='Home', message='Hello, World!')

# Define a function to get a random joke from a file
def get_random_joke():
    # Open the 'jokes.txt' file in read mode
    with open('jokes.txt', 'r') as file:
        # Read all lines from the file and store them in a list
        jokes = file.readlines()
    # Return a randomly chosen joke from the list
    return random.choice(jokes)

# Define a route for the '/joke' URL
@app.route('/joke')
def joke():
    # Call the get_random_joke function to retrieve a random joke
    joke = get_random_joke()
    # Render the 'joke.html' template with the retrieved joke
    return render_template('joke.html', joke=joke)

# Define a route for the '/greeting' URL, allowing both GET and POST requests
@app.route('/greeting', methods=['GET', 'POST'])
def greeting():
    # Check if the request method is POST
    if request.method == 'POST':
        # If it is a POST request, retrieve the 'username' from the form data
        username = request.form['username']
        # Return a personalized greeting using the submitted username
        return render_template('hello.html', username=username)
        return f'Hello, {username}!'

    # If it's a GET request, render the 'login.html' template
    return render_template('greeting.html')

# The following block ensures that the app is only run when this script is executed directly, not when it's imported as a module
if __name__ == '__main__':
    # Run the Flask app in debug mode, which provides additional information for debugging
    app.run(debug=True)

# Define another route for the '/about' URL. When someone accesses this URL, the following function is executed.
@app.route('/about')
def about():
    # Return a different string as the response when the '/about' URL is accessed
    return 'This is the about page.'

# Define a route for the '/user/<username>' URL. The '<username>' part is a variable that can take any value.
# When someone accesses this URL with a specific username, the following function is executed.
@app.route('/user/<username>')
def show_user_profile(username):
    # Return a string that includes the provided username in the response
    return f'Hello {username}!'

# The following block ensures that the app is only run when this script is executed directly, not when it's imported as a module
if __name__ == '__main__':
    # Run the Flask app in debug mode, which provides additional information for debugging
    app.run(debug=True)