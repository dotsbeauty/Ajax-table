from flask import Flask, request, render_template, redirect, url_for, jsonify
import json
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        with open('data.json') as f:
            data = json.load(f)
        return jsonify(data)
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'age': request.form.get('age'),
            'gender': request.form.get('gender')
        }
        with open("data.json", "r") as f:
            # obj = f.read()
            inside = json.loads(f.read())
        inside.append(data)
        with open("data.json", 'a+') as f:
            # print("gg")
            if data['name']:
                f.seek(0)
                f.truncate()
                json.dump(inside, f)

        return redirect(url_for('index'))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
