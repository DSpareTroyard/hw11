from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def page_index():
    test = "test test"
    return render_template('index.html', test=test)


app.run()
