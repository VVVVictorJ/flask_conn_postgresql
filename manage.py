import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config.default import Config
from myapp.models import User 
from app import app, db

app.config.from_object(Config())
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()

