from flask import request, jsonify
import jwt
import datetime
from app.services.redis_service import RedisService

class AuthController:
    SECRET_KEY = 'your_secret_key'
    
    def __init__(self):
        self.redis_service = RedisService()

    def login(self):
        auth_data = request.json
        username = auth_data.get('username')
        password = auth_data.get('password')


        if username == 'admin' and password == 'password':
            token = jwt.encode({
                'user': username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, self.SECRET_KEY, algorithm="HS256")

            self.redis_service.set(f"token:{username}", token, ex=1800)  # Expira en 1800 segundos (30 minutos)

            return jsonify({'token': token})

        return jsonify({'message': 'Invalid credentials'}), 401

    def protected(self):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            decoded_token = jwt.decode(token, self.SECRET_KEY, algorithms=["HS256"])
            username = decoded_token['user']

            redis_token = self.redis_service.get(f"token:{username}")
            if redis_token and redis_token.decode('utf-8') == token:
                return jsonify({'message': 'Token is valid!'})

            return jsonify({'message': 'Token is not valid or revoked!'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401
