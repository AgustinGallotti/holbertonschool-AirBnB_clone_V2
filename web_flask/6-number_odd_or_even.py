#!/usr/bin/python3
""" module """


if __name__ == "__main__":
    from flask import Flask
    from flask import render_template

    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello_hbnb():
        """root folder route"""
        return "Hello HBNB!"

    @app.route('/hbnb', strict_slashes=False)
    def hbnb_route():
        """/hbnb/ folder route"""
        return "HBNB"

    @app.route('/c/<text>', strict_slashes=False)
    def c_route(text):
        """some text in output depending on url after /c/"""
        return "C " + text.replace('_', ' ')

    @app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
    @app.route('/python/(<text>', strict_slashes=False)
    def python_route(text):
        """text depending on url after"""
        return "Python " + text.replace('_', ' ')

    @app.route('/number/<int:n>', strict_slashes=False)
    def n_route(n):
        """depending of the route"""
        return str(n) + " is a number"

    @app.route('/number_template/<int:n>', strict_slashes=False)
    def number_templates(n):
        """depending after of the url"""
        return render_template('5-number.html', n=n)

    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def or_or(n):
        """n is even or odd"""
        if n % 2 == 0:
            orr = "even"
        else:
            orr = "odd"
        return render_template('6-number_odd_or_even.html', n=n, orr=orr)

    app.run(host='0.0.0.0')
