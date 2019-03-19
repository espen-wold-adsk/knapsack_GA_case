import requests

ENDPOINT = "https://y6fyditnqd.execute-api.eu-west-1.amazonaws.com/Test/genetic-fitness-prod-report_fitness"

def post_genome_to_highscore(genome, name):
    headers = {
        "Content-Type": "application/json",
    }
    queryStringParamaters = {
        "solution": {"genome": genome}, "name": name}

    requests.post(
        ENDPOINT,
        headers=headers,
        queryStringParamaters=queryStringParamaters)