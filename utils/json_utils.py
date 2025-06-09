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

def update_json_by_id(new_data, file_name):
    if os.path.exists(file_name):
        with open(file_name, "r+") as file:
            file_data = json.load(file)
            updated = False
            for idx, item in enumerate(file_data):
                if item.get("id") == new_data["id"]:
                    file_data[idx] = new_data
                    updated = True
                    break
            if updated:
                file.seek(0)
                json.dump(file_data, file, indent=4)
                file.truncate()
            return updated
    return False

def read_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return None
