import logging
logging.basicConfig(filename='main.log',level='INFO',format='%(asctime)s: %(levelname)s: %(message)s')

def inputCorrection():
    liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
    sprawdzanie=liczbaPrzystankow.isdigit()
    if(sprawdzanie == False):
        while (sprawdzanie == False):
            print('!!!Wpisz liczbe!!!')
            logging.warning('  User podal litere zamiast liczby')
            liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
            sprawdzanie=liczbaPrzystankow.isdigit()
    
        
    liczbaPrzystankow=int(liczbaPrzystankow)
    if(liczbaPrzystankow>6 or liczbaPrzystankow <= 0):
        while (liczbaPrzystankow>6 or liczbaPrzystankow <= 0):
            print('!!!Popraw liczbe przystanków!!!\n')
            logging.warning('  User nie podal poprawnej liczby przystanku')
            liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
            liczbaPrzystankow=int(liczbaPrzystankow)
    
    liczbaPrzystankow=int(liczbaPrzystankow)+1
    return liczbaPrzystankow

