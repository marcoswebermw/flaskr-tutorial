import os

from flask import Flask

def create_app(test_config=None):
    # Criar e configurar o app.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flasqr.sqlite'),
            )

    if test_config is None:
        # Quando não for um teste, carrega a instancia de config, se existir.
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega a configuração para testes se ela for passada.
        app.config.from_mapping(test_config)

    # Garantindo que a instancia do diretório existe.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        # Poderia ser um 'pass'.
        ...

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    def teste():
        return 'testando'
    return app


