# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, 'r') as input_file:
        data_from_json = json.load(input_file)
    sum_of_product = round(sum(item["score"]*item["weight"] for item in data_from_json), 3)
    return sum_of_product
print(task())

