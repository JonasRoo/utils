import json
import glob
import os

def dump_json_to_file(data: dict, folder_name: str, file_name: str, **kwargs):
    if not os.path.isdir(folder_name):
        raise ValueError(f"`{folder_name}` is not a valid directory!")
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, **kwargs)


def merge_all_json_in_folder(dir_name: str, merged_file_name: str = None) -> None:
    data = []
    json_wildcard_path = os.path.join(dir_name, "*.json")
    for f in glob.glob(json_wildcard_path):
        with open(f, "r", encoding="utf-8") as input_file:
            data.append(json.load(input_file))

    results_file_name = merged_file_name or "merged_data.json"
    results_file_path = os.path.join(dir_name, results_file_name)
    with open(results_file_path, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file)
