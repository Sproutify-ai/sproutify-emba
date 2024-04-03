from flask_script import Manager
from flask_migrate import MigrateCommand
from sproutify import app, db

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()