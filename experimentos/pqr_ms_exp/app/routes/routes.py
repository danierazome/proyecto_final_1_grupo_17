from flask import Blueprint
from app.controllers.home_controller import HomeController
from app.controllers.health_controller import HealthController

def init_app(app):
    service_name = "Users"

    home_controller = HomeController()
    health_controller = HealthController(service_name)
    
    bp = Blueprint('main', __name__)
    
    @bp.route('/')
    def home():
        return home_controller.home()
    
    @bp.route('/health')
    def health():
        return health_controller.health()
    
    app.register_blueprint(bp)