from flask import Flask  # Import the Flask class

app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define the route for the home page
def hello_world(): 
    return "<p>Hello</p>"  # Return a simple HTML response

app.run(debug=True)  # Run the app in debug mode