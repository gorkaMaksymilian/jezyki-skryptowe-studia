import connectTTSS
import findDatabase
import syntaxCorrection
import time
import sys
import logging
import default

logger=logging.getLogger(__name__)
logger.setLevel(default.DEFAULT_LOG["level"])
formatter=logging.Formatter(""+default.DEFAULT_LOG["formatter"]+"")
file_handler = logging.FileHandler(""+default.DEFAULT_LOG["file"]+"")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


sys.tracebacklimit=0
logger.info('  Uruchomienie programu')
logger.info('  Sprawdzenie poprawnosci przystanku')
przystanekNazwa=input("Podaj nazwe przystanku:")
#Tu dla unikania problemu ze wpisywaniem np "Dworzec główny" zamiast "Dworzec Główny"
przystanekNazwa=przystanekNazwa.lower()
#Usuwanie spacji przed i po słowie kluczowym np " Bronowice "
przystanekNazwa=przystanekNazwa.strip()

#Szukanie numeru przystanku i zwracanie gotowego URL
slownik=findDatabase.findInDatabase(przystanekNazwa)
logger.info('  Sprawdzenie poprawnosci ilosci przystankow')
urlTTSS=slownik["a"]
nazwa=slownik["b"]

#Sprawdzanie poprawnosci ilosci przystankow
liczbaPrzystankow=syntaxCorrection.inputCorrection()

logger.info('  Nawiazywanie sesji')
#Pobieranie i wypisanie danych z TTSS
try:
    while True:
        connectTTSS.connect(urlTTSS,liczbaPrzystankow,nazwa)
        time.sleep(30)
except KeyboardInterrupt:
    pass
logger.info('  Zakonczenie sesji')
logger.info('  Zakonczono program')

