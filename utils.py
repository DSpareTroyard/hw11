import json


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_candidate(path, candidate_id):
    candidates = load_candidates_from_json(path)
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(path, candidate_name):
    candidates = load_candidates_from_json(path)
    candidates_search = []
    for candidate in candidates:
        if candidate_name.lower() in candidate['name'].lower():
            candidates_search.append(candidate)

    return candidates_search


def get_candidates_by_skill(path, skill_name):
    candidates = load_candidates_from_json(path)
    candidates_search = []
    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(", ")
        if skill_name.lower() in candidate_skills:
            candidates_search.append(candidate)

    return candidates_search
