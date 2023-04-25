import requests
import spacy
from bs4 import BeautifulSoup

#Variables auxiliares
totalcount = 0
numpag = 1
pagina = ''

while numpag <= 10:
    
    
    #Obtengo la pagina con Requests
    web = requests.get(pagina+ str(numpag))
        

    
    #Leo las paginas con Request
    html = web.content.decode()
    
    
    
    #La proceso con Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('p')
    cadena = ""
    for b in a:
        cadena +=" "+ b.text

        
        
    #La convierto en un objeto de Spacy        
    nlp = spacy.load('es_core_news_sm')
    text = cadena
    doc = nlp(text) 
    


    #Tokenizacion
    tokens =[]
    for t in doc:
        tokens.append(t.orth_)
        
        

    #Normalizacion
    lex = []
    for t in doc:
        if   (not t.is_punct and 
             not t.is_stop):
            lex.append(t.orth_)

            
            
    #Lematizacion
    palabras = []
    for t in lex:
        if len(t)>= 3 and t.isalpha():
            palabras.append(t.lower())

    otras_pv = ["texto"]
    palabras2 =[]
    for texto in palabras:
        if texto not in otras_pv:
            palabras2.append(texto)
            
            
            
    
    
    
            
    #Aqui empieza el contador
    contador = 0
    for palabra in palabras2:
        if palabra == "cristina":
            contador = contador+1

    print("En la pagina ", str(numpag), "se menciona ________", contador, " veces")
    
    totalcount=totalcount+contador
    numpag=numpag+1

numpag=numpag-1
print("En ", numpag, " paginas, se menciona ", totalcount, " veces a _______")
