import requests


def strona_dziala(strona, file_name):
    response = requests.get(strona)

    if response.status_code == 200:
       with open(file_name, "w") as file:
           return file.write(strona + "\n")

    else:
       return print("Strona nie została znaleziona")

www = "http://wp.plplp"
adres_strony = []

strona_dziala(www, "strona.txt")
