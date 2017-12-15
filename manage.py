from flask_script import Manager
from app import create_app
from app.models import Classify

app = create_app()

# 初始化全局变量
app.jinja_env.globals['classifys'] = Classify.getClassifys
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

