from flask import Flask, render_template, request


def app_factory():
    app = Flask(__name__)

    from routes import user_routes
    app.register_blueprint(user_routes.bp)
    
    return app

if __name__ == '__main__':
    app = app_factory()
    app.run(debug=True)

