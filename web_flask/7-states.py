#!/usr/bin/python3
"""
    module
"""


if __name__ == '__main__':
    from models import storage
    from models.state import State
    from flask import Flask
    import flask

    app = Flask(__name__)

    @app.route('/states_list/', strict_slashes=False)
    def states_list():
        """lsit of stats from db"""
        dictt = storage.all(State)
        return render_template('7-states_list.html', states=dictt)

    app.run(host='0.0.0.0')

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        storage.close()
