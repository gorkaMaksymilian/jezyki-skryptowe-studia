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
    
    newTag = soup.new_tag("div",id=counter)
    soup.body.append(newTag)
    newA = soup.new_tag("a")
    newA.string=numerElement
    newTag.append(newA)

    newA = soup.new_tag("a")
    newA.string=przystanekElement
    newTag.append(newA)


    newA = soup.new_tag("a")
    newA.string=czasElement
    newTag.append(newA)
 
    
    file = codecs.open("index.html", "w", "utf-8")
    file.write(u""+str(soup))
    file.close()

