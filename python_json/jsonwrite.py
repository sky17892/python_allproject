import json

with open("./python_json/myinfo.json", "r", encoding="utf-8") as f:
    data123 = json.load(f)

print(data123)
