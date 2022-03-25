import json


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    pass


def get_candidates_by_skill(skill_name):
    pass
