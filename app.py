from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html')


@app.route('/part_one/')
def page_part_one():
    return render_template('part_one.html')


@app.route('/part_two/')
def page_part_two():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>/')
def page_card(x):
    candidate = utils.get_candidate(x)
    return render_template('card.html', candidate=candidate)


app.run()
