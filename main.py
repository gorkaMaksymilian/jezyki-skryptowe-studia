import connectTTSS
import findDatabase
import syntaxCorrection
import time
import logging
import sys
sys.tracebacklimit=0
logging.basicConfig(filename='main.log',level='INFO',format='%(asctime)s: %(levelname)s: %(message)s')

logging.info('  Uruchomienie programu')
logging.info('  Sprawdzenie poprawnosci przystanku')
przystanekNazwa=input("Podaj nazwe przystanku:")
#Tu dla unikania problemu ze wpisywaniem np "Dworzec główny" zamiast "Dworzec Główny"
przystanekNazwa=przystanekNazwa.lower()
#Usuwanie spacji przed i po słowie kluczowym np " Bronowice "
przystanekNazwa=przystanekNazwa.strip()

#Szukanie numeru przystanku i zwracanie gotowego URL
slownik=findDatabase.findInDatabase(przystanekNazwa)
logging.info('  Sprawdzenie poprawnosci ilosci przystankow')
urlTTSS=slownik["a"]
nazwa=slownik["b"]

#Sprawdzanie poprawnosci ilosci przystankow
liczbaPrzystankow=syntaxCorrection.inputCorrection()

logging.info('  Nawiazywanie sesji')
#Pobieranie i wypisanie danych z TTSS
try:
    while True:
        connectTTSS.connect(urlTTSS,liczbaPrzystankow,nazwa)
        time.sleep(30)
except KeyboardInterrupt:
    pass
logging.info('  Zakonczenie sesji')
logging.info('  Zakonczono program')

