from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    
    app.config.from_object("settings.app_config")

    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # @app.errorhandler(500)
    # def handle_500(error):
    #     app.logger.error(error)
    #     return ("bad stuff", 500)

    return app