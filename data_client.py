import requests
import json

ENDPOINT = "https://y6fyditnqd.execute-api.eu-west-1.amazonaws.com/Test/genetic-fitness-prod-report_fitness"


def post_genome_to_highscore(genome, name):
    headers = {"Content-Type": "application/json"}
    data = {"solution": {"genome": genome}, "name": name}

    response = requests.post(url=ENDPOINT, headers=headers, data=json.dumps(data))


import json


def read_problem_from_json():
    json_file = open("data.json", "r")
    problem_data = json.load(json_file)

    site_polygon = problem_data["site_polygon"]
    buildings = problem_data["buildings"]

    return site_polygon, buildings
