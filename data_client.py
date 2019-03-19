import requests
import json

ENDPOINT = "https://y6fyditnqd.execute-api.eu-west-1.amazonaws.com/Test/genetic-fitness-prod-report_fitness"


def post_genome_to_highscore(genome, name):
    headers = {"Content-Type": "application/json"}
    data = {"solution": {"genome": genome}, "name": name}

    response = requests.post(url=ENDPOINT, headers=headers, data=json.dumps(data))
