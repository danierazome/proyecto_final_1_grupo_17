# app/routes.py

from flask import Blueprint
from app.controllers.home_controller import HomeController
from app.controllers.health_controller import HealthController
from app.controllers.auth_controller import AuthController
from app.controllers.redis_controller import RedisController

def init_app(app):
    service_name = "auth"

    home_controller = HomeController()
    health_controller = HealthController(service_name)
    auth_controller = AuthController()
    redis_controller = RedisController()

    bp = Blueprint('main', __name__)

    # Rutas Home
    @bp.route('/')
    def home():
        return home_controller.home()

    # Ruta de Health Check
    @bp.route('/health')
    def health():
        return health_controller.health()

    # Rutas de Autenticación
    @bp.route('/auth/login', methods=['POST'])
    def login():
        return auth_controller.login()

    @bp.route('/auth/protected', methods=['GET'])
    def protected():
        return auth_controller.protected()

    # Rutas de Redis
    @bp.route('/cache/store', methods=['POST'])
    def store_in_cache():
        return redis_controller.store_in_cache()

    @bp.route('/cache/get/<key>', methods=['GET'])
    def get_from_cache(key):
        return redis_controller.get_from_cache(key)

    app.register_blueprint(bp)
