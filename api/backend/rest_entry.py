from flask import Flask
from flask import make_response
from flask import jsonify
import random

supportive_quotes = [
    "You are capable of amazing things.",
    "Believe in yourself and all that you are.",
    "Keep going, you are doing great!",
    "Every day is a new beginning.",
    "You have the power to create change.",
    "Your potential is limitless."
]

def create_app():
    app = Flask(__name__)


    # Base route - home
    @app.route("/", methods=['GET'])
    def say_hello():
        response = make_response("<h1>Hello from your First Flask App</h1>")
        response.status_code = 200
        return response
    
    # get some fake data
    @app.route('/api/data', methods=['GET'])
    def get_data():
        sample_data = {"message": "Hello, World!", "status": "success"}
        response = make_response(jsonify(sample_data))
        response.status_code = 200
        return response
    
    # a dynamic route, takes a parameter
    @app.route('/user/<username>')
    def user_profile(username):
        response = make_response(f"<h1>Profile page of user: {username}</h1>")
        response.status_code = 200
        return response 
    
    # New route: Random supportive quote
    @app.route('/api/quote', methods=['GET'])
    def get_supportive_quote():
        quote = random.choice(supportive_quotes)
        response = make_response(jsonify({"quote": quote}))
        response.status_code = 200
        return response

    # Don't forget to return the app object (back to the
    # backend_app function in this case)
    return app

