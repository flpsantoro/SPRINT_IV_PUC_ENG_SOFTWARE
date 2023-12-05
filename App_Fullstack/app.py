from flask import Flask


def create_app():
    app = Flask(__name__)

    from routes.views import views
    from routes.upload import upload_blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(upload_blueprint, url_prefix='/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
