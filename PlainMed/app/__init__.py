from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.mod_index.controllers import mod_index as index_module
from app.mod_auth.controllers import mod_auth as authentication_module

# Register blueprints
app.register_blueprint(index_module)
app.register_blueprint(authentication_module)

db.create_all()