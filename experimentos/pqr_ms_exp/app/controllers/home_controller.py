from flask import jsonify

class HomeController:
    def home(self):
        mock_data = {
            "id": 1,
            "usuario": "Juan Pérez",
            "motivo_consulta": "Consulta sobre escalabilidad en Azure"
        }
        return jsonify(mock_data)
