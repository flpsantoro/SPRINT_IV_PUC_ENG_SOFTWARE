from _testcapi import test_config
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.update(
        TESTING=False,
    )

    if test_config:
        app.config.update(test_config)

    from routes.views import views

    app.register_blueprint(views, url_prefix='/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
