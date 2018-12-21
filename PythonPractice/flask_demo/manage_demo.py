# -*- coding: utf-8 -*-

# @Time    : 2018/7/18 10:22
# @Author  : songq001
# @Comment : 

from flask import Flask
from flask_script import Manager, Shell

app = Flask(__name__)

manager = Manager(app)
# migrate = Migrate(app, db)


# def make_shell_context():
# 	return dict(app=app, db=db, User=User, Role=Role)
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!================'


if __name__ == '__main__':
    # app.run()
    manager.run()

