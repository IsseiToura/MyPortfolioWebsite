from flask import Flask
from .issei_gpt.routes import issei_gpt_bp

def create_app():
    app = Flask(__name__)
    
    from . import views
    app.register_blueprint(views.main_bp)
    app.register_blueprint(issei_gpt_bp)

    return app
