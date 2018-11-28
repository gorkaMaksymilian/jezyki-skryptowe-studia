def inputCorrection():
    liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
    sprawdzanie=liczbaPrzystankow.isdigit()
    if(sprawdzanie == False):
        while (sprawdzanie == False):
            print('!!!Wpisz liczbe!!!')
            liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
            sprawdzanie=liczbaPrzystankow.isdigit()
    
        
    liczbaPrzystankow=int(liczbaPrzystankow)
    if(liczbaPrzystankow>6 or liczbaPrzystankow <= 0):
        while (liczbaPrzystankow>6 or liczbaPrzystankow <= 0):
            print('!!!Popraw liczbe przystanków!!!\n')
            liczbaPrzystankow=input("Podaj liczbe przystanków do wyswietlenia (>0 && <6): ")
            liczbaPrzystankow=int(liczbaPrzystankow)
    
    liczbaPrzystankow=int(liczbaPrzystankow)+1
    return liczbaPrzystankow

