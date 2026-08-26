from flask import Flask

from importlib.metadata import version
__version__ = version("myapp")

app = Flask(__name__)


@app.route('/')
def hello_world():
   return 'Hello, world'


@app.route('/version')
def version():
   return __version__


@app.route('/health')
def health():
   return {'status': 'OK'}


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

