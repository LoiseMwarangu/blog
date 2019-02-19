from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from app.models import Blogpost , Users
from app import db


app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

app = create_app('test')
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Users=Users,Blogpost=Blogpost)

if __name__ == '__main__':
    manager.run()

