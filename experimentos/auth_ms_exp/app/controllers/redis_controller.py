from flask import request, jsonify
from app.services.redis_service import RedisService

class RedisController:

    def __init__(self):
        self.redis_service = RedisService()

    def store_in_cache(self):
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if key and value:
            self.redis_service.set(key, value)
            return jsonify({'status': 'success', 'message': 'Data stored in Redis'}), 200
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400

    def get_from_cache(self, key):
        value = self.redis_service.get(key)
        if value:
            return jsonify({'status': 'success', 'value': value.decode('utf-8')}), 200
        return jsonify({'status': 'error', 'message': 'Key not found'}), 404
