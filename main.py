import connectTTSS
import findDatabase
import syntaxCorrection
import time



przystanekNazwa=input("Podaj nazwe przystanku:")
#Tu dla unikania problemu ze wpisywaniem np "Dworzec główny" zamiast "Dworzec Główny"
przystanekNazwa=przystanekNazwa.lower()
#Usuwanie spacji przed i po słowie kluczowym np " Bronowice "
przystanekNazwa=przystanekNazwa.strip()

#Szukanie numeru przystanku i zwracanie gotowego URL
slownik=findDatabase.findInDatabase(przystanekNazwa)
urlTTSS=slownik["a"]
nazwa=slownik["b"]

#Sprawdzanie poprawnosci ilosci przystankow
liczbaPrzystankow=syntaxCorrection.inputCorrection()


#Pobieranie i wypisanie danych z TTSS
try:
    while True:
        connectTTSS.connect(urlTTSS,liczbaPrzystankow,nazwa)
        time.sleep(30)
except KeyboardInterrupt:
    pass
    

