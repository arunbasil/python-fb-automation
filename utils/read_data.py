
import csv
import json


def read_csv_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data



def read_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
