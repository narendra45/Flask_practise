import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

cmd = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(cmd, db)

@cmd.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@cmd.cli.command()
def test():
"""Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)