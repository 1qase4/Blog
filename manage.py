from flask_script import Manager
from app import create_app

app = create_app()
manager = Manager(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    manager.run()
