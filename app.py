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
    candidate = utils.get_candidate("candidates.json", x)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>/')
def page_search(candidate_name):
    candidates = utils.get_candidates_by_name("candidates.json", candidate_name)
    return render_template('search.html', candidate_name=candidate_name, candidates=candidates)


@app.route('/skill/<skill_name>')
def page_skill(skill_name):
    candidates = utils.get_candidates_by_skill("candidates.json", skill_name)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name)


app.run()
