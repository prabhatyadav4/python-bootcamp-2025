from flask import Flask, render_template  # Import Flask and render_template

app = Flask(__name__)  # Create a Flask app instance

@app.route("/")  # Define route for the home page
def hello_world(): 
    return render_template("index.html")  # Render the index.html template

app.run(debug=True)  # Run the app in debug mode