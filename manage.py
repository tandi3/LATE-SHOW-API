from flask.cli import FlaskGroup
from server.app import create_app
from server.models import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
