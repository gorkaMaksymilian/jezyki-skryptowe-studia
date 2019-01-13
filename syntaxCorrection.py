import logging
import default
logger=logging.getLogger(__name__)
logger.setLevel(default.DEFAULT_LOG["level"])
formatter=logging.Formatter(""+default.DEFAULT_LOG["formatter"]+"")
file_handler = logging.FileHandler(""+default.DEFAULT_LOG["file"]+"")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def inputCorrection():
    liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia: ")
    sprawdzanie=liczbaPrzystankow.isdigit()
    if(sprawdzanie == False):
        while (sprawdzanie == False):
            print('!!!Wpisz liczbe!!!')
            logger.info('  User podal litere zamiast liczby')
            liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
            sprawdzanie=liczbaPrzystankow.isdigit()
    
    
    liczbaPrzystankow=int(liczbaPrzystankow)+1
    return liczbaPrzystankow

