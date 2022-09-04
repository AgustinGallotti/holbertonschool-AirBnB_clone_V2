#!/usr/bin/python3
""" route """


if __name__ == '__main__':
	from flask import Flask

	app = Flask(__name__)

	@app.route('/', strict_slashes=False)
	def routte():
		"""root folder route"""
		return "Hello HBNB!"

	@app.route('/hbnb', strict_slashes=False)
	def hbnb():
		"""hbnbb"""
		return "HBNB"

	app.run(host='0.0.0.0:5000')
