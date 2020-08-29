import json


film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors" : ("Dawid Skibiński", "Klaudia Kistowska"),
    "budget" : None,
    "credits" : {
            "director" : "Klaudia Kistowska",
            "writer" : "EssDaniels",
            "animator" : "Samada"

    }
}


print(json.dumps(film, ensure_ascii=False, indent=4))



with open("sample.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4)

print(film)