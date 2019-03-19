import json


def read_problem_from_json():
    json_file = open("data.json", "r")
    problem_data = json.load(json_file)

    site_polygon = problem_data["site_polygon"]
    buildings = problem_data["buildings"]

    return site_polygon, buildings
