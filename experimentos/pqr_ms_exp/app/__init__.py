from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        from .routes import routes
        routes.init_app(app)

    return app
