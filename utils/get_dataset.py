from inspect_ai.dataset import json_dataset

def get_dataset(harm_category):
    string_to_path = "datasets/" + harm_category + ".jsonl"
    return json_dataset(string_to_path)