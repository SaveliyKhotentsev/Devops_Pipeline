VERSION = '1.0.0'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route('/version')
def version():
   return VERSION


@app.route('/health')
def health():
   return {'status': 'OK'}

if __name__ == '__main__':
  app.run(debug=True)
