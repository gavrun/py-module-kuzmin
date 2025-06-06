import json

filename = 'person.json'

info = {
    "Full name": "Ivanov Ivan Petrovich",
    "Rating": {
        "Knowledge": 90,
        "Skills": 85,
        "Skills": 80
    },
    "Possibilities": ["Accuracy", "Stress resistance"],
    "Age": 35.5,
    "Hobby": None
}

# Writing a structure in a file in json format
with open(filename, "w", encoding="utf-8") as fh:
    fh.write(json.dumps(info, ensure_ascii=False, indent=4))


# Reading from a JSON-format file
info_2 = []
with open(filename, encoding="utf-8") as fh:
    info_2 = json.loads(fh.read())

print(info_2)
