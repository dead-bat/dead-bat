import os
from flask import Flask

def create_app(test_config=None):
	# create and configure application
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'wcfc.sqlite'),
	)

	if test_config is None:
		# load instance config if it exists (for testing)
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load test config if passed
		app.config.from_mapping(test_config)

	# verify there is an instance/ directory
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# and the traditional hello page
	@app.route('/hello')
	def hello():
		return "Hello, World!"

	from . import db
	db.init_app(app)

	from . import auth
	app.register_blueprint(auth.bp)

	return app