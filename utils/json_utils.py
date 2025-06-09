import os
import json


def add_to_json(new_data, filename):
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            file_data = json.load(file)
            file_data.append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            json.dump(file_data, file, indent=4)
    else:
        with open(filename, "w") as file:
            json.dump([new_data], file, indent=4)


def delete_from_json(match_fn, filename):
    """
    Removes items from the JSON file where match_fn(item) returns True.
    match_fn: function that takes an item and returns True if it should be deleted.
    """
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            file_data = json.load(file)
            new_data = [item for item in file_data if not match_fn(item)]
            file.seek(0)
            json.dump(new_data, file, indent=4)
            file.truncate()


def read_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return None
