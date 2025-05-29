import os
import json

def write_json(new_data, filename):
    if os.path.exists(filename):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data.append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            json.dump(file_data, file, indent = 4)
    else:
        with open(filename, 'w') as file:
            json.dump([new_data], file, indent = 4)