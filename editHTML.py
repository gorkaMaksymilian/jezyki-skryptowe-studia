import bs4
import codecs


def createIndex():
    scaffolding='<!DOCTYPE html><html><head><link rel="stylesheet" type="text/css" href="mystyle.css"><meta http-equiv="refresh" content="35"><title>Projekt</title></head><body></body></html>'
    basicHTML=open("index.html","w")
    basicHTML.write(scaffolding)
    basicHTML.close()

def insertData(numerElement,przystanekElement,czasElement,counter,nazwa):
    with open("index.html",encoding="utf-8") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt,features="lxml")
        
    przystanekElement=u""+przystanekElement
    czasElement=u""+czasElement
     
    if counter=="2":
        newDisplay = soup.new_tag("h1")
        newDisplay.string="Wybrany przystanek: "+nazwa
        soup.body.append(newDisplay)
    
    newA = soup.new_tag("p")
    newA.string=numerElement
    soup.body.append(newA)

    newA = soup.new_tag("p")
    newA.string=przystanekElement
    soup.body.append(newA)


    newA = soup.new_tag("p")
    newA.string=czasElement
    soup.body.append(newA)
 
    
    file = codecs.open("index.html", "w", "utf-8")
    file.write(u""+str(soup))
    file.close()

