import json
import pprint




with open("sample.json", "r", encoding="UTF-8") as file:
    decodeMove = json.load(file)

print(decodeMove)

pprint.pprint(decodeMove)