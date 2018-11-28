import requests

url="http://www.ttss.krakow.pl/internetservice/geoserviceDispatcher/services/stopinfo/stops?left=-648000000&bottom=-324000000&right=648000000&top=324000000"
przystanki = requests.get(url)

def findInDatabase(przystanekNazwa):
    
    loop=0
    czyWystapil=False
    nazwa=""
    
    while(czyWystapil==False):
        if loop==1:
            przystanekNazwa=input("Podaj nazwe przystanku:")
            przystanekNazwa=przystanekNazwa.strip()
            przystanekNazwa=przystanekNazwa.lower()
        for x in przystanki.json()["stops"]:
            if x["name"].lower() == przystanekNazwa:
                print('Znaleziono przystanek: '+x["name"])
                nazwa=x["name"]
                numerPrzystanku=x["shortName"]
                czyWystapil=True
                break
        if czyWystapil==False:
            print("Błędna nazwa przystanku")
            loop=1

    return {'a':"http://www.ttss.krakow.pl/#?stop="+numerPrzystanku+"&mode=departure","b":nazwa}
