import os

os.environ['DEBUG'] = '1'
os.environ['STATICSERVER'] = '1'

from fcamara.app import app

if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
