from flask import jsonify

class HomeController:
    def home(self):
        return jsonify(message="Hello, World!")
