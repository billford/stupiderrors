#!/usr/bin/python3

from flask import Flask, abort, redirect

app = Flask(__name__)


@app.route('/readme')
def readme():
    return redirect("https://github.com/billford/stupiderrors", code=302)


# noinspection PyUnusedLocal,PyUnusedLocal
@app.route('/', defaults={'path': '', 'statcode': None})
@app.route('/<path:path>/<int:statcode>')
def get_path(path, statcode):
    if statcode != 200:
        return abort(statcode)
    else:
        return "Hey this isn't cool, either that's not a valid exception or you sent a 200, stop that!"
