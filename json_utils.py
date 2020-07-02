import json
import glob
import os

def dump_json_to_file(data: dict, folder_name: str = ".", file_name: str = "data.json", **kwargs) -> None:
    """
    Produces a formatted .json file from a dictionary at a given path.

    @args:
        - data: the `dict` of data to save as a .json formatted file
        - folder_name (optional): either `full path` or `relative` path
                       of the folder to save the file in (default: current directory)
        - file_name (optional): the name of new .json file (default: `data.json`)

    @returns:
        None
    """
    if not os.path.isdir(folder_name):
        raise ValueError(f"`{folder_name}` is not a valid directory!")
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, **kwargs)


def merge_all_json_in_folder(dir_name: str, merged_file_name: str = "merged_data.json") -> None:
    """
    Merges all json files in a given directory into a single formatted .json file.

    @args:
        - dir_name: The full path or relative path of the directory
                    containing the .json files to merge
        - merged_file_name (optional): the name of the file containing the merged data
                                       (default `merged_data.json`)
    """
    data = []
    json_wildcard_path = os.path.join(dir_name, "*.json")
    for f in glob.glob(json_wildcard_path):
        with open(f, "r", encoding="utf-8") as input_file:
            data.append(json.load(input_file))

    results_file_path = os.path.join(dir_name, merged_file_name)
    with open(results_file_path, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file)
