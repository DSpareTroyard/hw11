from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/part_one')
def page_part_one():
    return render_template('part_one.html')


@app.route('/part_two')
def page_part_two():
    return render_template('part_two.html')


app.run()
