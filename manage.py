from app import create_app, db
from app.models import POI
from flask.ext.script import Manager, Shell
import config
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

def make_shell_context():
	return dict(app=app, db=db, POI=POI)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()