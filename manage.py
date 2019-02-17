from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from app.models import Blogpost
from app import db


app = create_app('development')
# app = create_app('test')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(db=db)

if __name__ == '__main__':
    manager.run()

