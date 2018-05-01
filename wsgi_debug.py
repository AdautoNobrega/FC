import os
os.environ['DEBUG'] = '1'

from fcamara.app import app


if __name__ == '__main__':
    print('Iniciando Servidor...')
    app.run()
