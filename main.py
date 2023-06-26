from flask import Flask, render_template, redirect, url_for, flash, g, abort
from flask_bootstrap import Bootstrap


def run_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = run_app()


@app.route('/')
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
