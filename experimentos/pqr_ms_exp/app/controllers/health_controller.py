from flask import jsonify

class HealthController:
    def __init__(self, service_name):
        self.service_name = service_name

    def health(self):
        return jsonify(message=f"Everything ok with the service {self.service_name}")
