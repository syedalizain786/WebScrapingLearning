import json

def read_json(filename):
    try:
        with open(filename,'r') as jsonfile:
            x=jsonfile.read()
            data=json.loads(x)
        print(data)
        print(data[1]['id'])

        # for d in data:
        #     print(d['id'])
    except Exception as e:
        print(f"Error :{e}")


def write_json(filename):
    jsondata={
        "id": 4,
        "name": "shah",
        "email": "abc.com"
    }
    try:
        # Load existing JSON data
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []  # If file doesn't exist, start with an empty list

    # Append new data to the existing data list
    data.append(jsondata)

    # Write updated data back to the file
    with open(filename, 'w') as file:
        json.dump(data, file,indent=2)


write_json('data.json')

read_json('data.json')
