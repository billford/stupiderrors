#!/usr/bin/python3

from flask import Flask, abort, redirect
app = Flask(__name__)

@app.route('/readme')
def readme():
    return redirect("https://github.com/billford/stupiderrors", code=302)

@app.route('/', defaults={'path': '', 'statCode': None} )
@app.route('/<path:path>/<int:statCode>')
def get_path(path, statCode):
    if statCode != 200 :
        return abort(statCode)
    else:
        return "Hey this isn't cool, either that's not a valid exception or you sent a 200, stop that!"
