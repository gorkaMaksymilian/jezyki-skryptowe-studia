import requests
import logging
import default


logger=logging.getLogger(__name__)
logger.setLevel(default.DEFAULT_LOG["level"])
formatter=logging.Formatter(""+default.DEFAULT_LOG["formatter"]+"")
file_handler = logging.FileHandler(""+default.DEFAULT_LOG["file"]+"")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
url=default.DEFAULT_FIND_DATABASE["url"]
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
                logger.warning('  User podal prawidlowa nazwe przystanku')
                nazwa=x["name"]
                numerPrzystanku=x["shortName"]
                czyWystapil=True
                break
        if czyWystapil==False:
            print("Błędna nazwa przystanku")
            logger.warning('  User podal bledna nazwe przystanku')
            loop=1

    return {'a':"http://www.ttss.krakow.pl/#?stop="+numerPrzystanku+"&mode=departure","b":nazwa}
